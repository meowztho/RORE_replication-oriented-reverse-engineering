#!/usr/bin/env python3
"""Project-native validation gate for CoreReplica.

Validates deterministic plugin/governance invariants already encoded in project
authorities, self-tests representative known-bad mutants, then runs the Python
regression suite.
"""

import csv
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = [
    "corereplica-orchestration",
    "corereplica-reference",
    "corereplica-product",
    "corereplica-design",
    "corereplica-build",
    "corereplica-verify",
    "corereplica-market",
    "corereplica-release",
]
REQUIRED_DOCS = [
    "docs/USER_VISION.md",
    "docs/DECISION_COMPENDIUM.md",
    "docs/SYSTEM_MAP.yaml",
    "docs/CAPABILITY_GRAPH.yaml",
    "docs/SYSTEM_INTEGRATION.yaml",
    "docs/ARCHITECTURE_GUARDRAILS.yaml",
    "docs/PRODUCT_REALIZATION.yaml",
    "docs/PROJECT_PLAN.yaml",
    "docs/ACCEPTANCE.yaml",
    "docs/PROJECT_INDEX.yaml",
    "docs/CONTEXT_HANDOFF.md",
    "skills/corereplica-orchestration/references/WORKSPACE_AND_STANDALONE.md",
    "skills/corereplica-orchestration/references/SOURCE_USE_AND_DISTRIBUTION_POLICY.md",
    "skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md",
    "skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md",
    "skills/corereplica-reference/references/RUNTIME_CORROBORATION.md",
    "skills/corereplica-reference/references/ADVERSARIAL_LIMIT_PROBING.md",
    "skills/corereplica-reference/references/EXTERNAL_RESEARCH_AND_CORROBORATION.md",
    "skills/corereplica-verify/references/SIDE_EFFECT_SAFE_VERIFICATION.md",
    "SOURCE_PROVENANCE.md",
    "LICENSE",
    "LICENSE-UPSTREAM",
    "LICENSE-REVERSE-SKILL",
    "THIRD_PARTY_NOTICES.md",
]
FORBIDDEN_STATUS_FIELDS = {"clone", "done", "verified", "implementation_status"}
FORBIDDEN_PACKAGE_PARTS = {"__pycache__", ".pytest_cache", ".mypy_cache", "node_modules", ".venv", "venv"}
FORBIDDEN_PACKAGE_SUFFIXES = {".pyc", ".pyo"}


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def error(errors, message):
    errors.append(message)


def check_requirement_fields(fields):
    bad = sorted(FORBIDDEN_STATUS_FIELDS.intersection(f.lower() for f in fields))
    return [] if not bad else ["Product requirements contain forbidden state fields: %s" % ", ".join(bad)]


def check_verifier_text(text):
    low = text.lower()
    errors = []
    if "read-only" not in low:
        errors.append("Verifier lost read-only contract")
    if "do **not** fix source implementation" not in low:
        errors.append("Verifier no longer explicitly forbids self-fixing")
    if "## step 5: fix loop" in low or "fix loop" in low:
        errors.append("Verifier contains a fix loop")
    if "route the finding" not in low:
        errors.append("Verifier no longer routes findings to implementation owner")
    return errors


def check_release_text(text):
    low = text.lower()
    errors = []
    for phrase in ("reversible preparation", "exact gated transition", "explicit current approval"):
        if phrase not in low:
            errors.append("Release gate missing phrase: %s" % phrase)
    return errors


def check_orchestration_text(text):
    errors = []
    if "REFERENCE TRUTH != PRODUCT TRUTH != IMPLEMENTATION STATE != VERIFICATION TRUTH != RELEASE APPROVAL" not in text:
        errors.append("Orchestration lost truth-layer separation")
    if "Do not preload all siblings" not in text:
        errors.append("Orchestration lost JIT/progressive disclosure rule")
    if "recon -> architect -> design -> build -> backend -> test -> diff" in text.lower():
        errors.append("Mandatory upstream pipeline reintroduced")
    for phrase in (
        "binary/distribution package",
        "preferred companion, not a hard runtime dependency",
        "CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY",
    ):
        if phrase not in text:
            errors.append("Orchestration missing invariant: %s" % phrase)
    return errors


def check_reference_qualification_text(text):
    low = text.lower()
    errors = []
    required = (
        "parseable output is not identity proof",
        "multiple plausible matches → unresolved",
        "population completeness",
        "independent corroboration requires",
        "materially independent failure modes",
        "parser safety",
        "unresolved_source_precedence",
        "current-view reconciliation",
        "representative relevant failure mode",
    )
    for phrase in required:
        if phrase not in low:
            errors.append("Reference evidence qualification missing: %s" % phrase)
    return errors



def check_reverse_engineering_text(reference_text, workflow_text, product_text, orchestration_text):
    errors = []
    for phrase in (
        "recover as much useful technical knowledge as practical",
        "extract / unpack / decode / decompile",
        "Evidence → Finding → Path",
        "REVERSE_ENGINEERING_WORKFLOW.md",
        "Reconstruction coverage challenge",
        "Replica trait handoff",
    ):
        if phrase not in reference_text:
            errors.append("Reference reverse-engineering contract missing: %s" % phrase)
    for phrase in (
        "Broad triage before narrow depth",
        "Static analysis",
        "Dynamic/runtime analysis",
        "Hypothesis-driven replanning",
        "Coverage and gap loop",
    ):
        if phrase not in workflow_text:
            errors.append("Reverse-engineering JIT workflow missing: %s" % phrase)
    for phrase in (
        "CoreReplica owns **reference recovery**, not durable project compilation",
        "APC owns compilation",
    ):
        if phrase not in orchestration_text:
            errors.append("CoreReplica/APC boundary missing: %s" % phrase)
    if "Do not generate APC-style System Map/Plan/Acceptance/Blueprint artifacts here" not in product_text:
        errors.append("Product lane can still duplicate APC compilation authorities")
    return errors

def check_runtime_corroboration_text(reference_text, runtime_text, workflow_text, orchestration_text):
    errors = []
    ref_low = reference_text.lower()
    runtime_low = runtime_text.lower()
    for phrase in (
        "runtime_corroboration.md",
        "runtime-sensitive",
    ):
        if phrase not in ref_low:
            errors.append("Reference runtime-corroboration contract missing: %s" % phrase)
    for phrase in (
        "claim-sensitive",
        "not a blanket requirement to launch every target",
        "static_sufficient",
        "runtime_sensitive",
        "representative authorized real run",
        "runtime_unchecked",
        "present",
        "referenced",
        "reachable",
        "exercised",
        "effective",
        "cross-version/cross-environment evidence",
    ):
        if phrase not in runtime_low:
            errors.append("Runtime corroboration JIT missing: %s" % phrase)
    for phrase in (
        "RUNTIME_CORROBORATION.md",
        "runtime-sensitive claim",
        "PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE",
    ):
        if phrase not in workflow_text:
            errors.append("Reverse-engineering workflow runtime boundary missing: %s" % phrase)
    if "RUNTIME_CORROBORATION.md" not in orchestration_text:
        errors.append("Orchestration does not route runtime corroboration JIT")
    return errors


def check_adversarial_limit_text(text):
    low = text.lower()
    errors = []
    for phrase in (
        "proof of mechanism",
        "not exploit maximization",
        "one primary variable",
        "state-machine and logic probing",
        "timing, concurrency and drift",
        "parser, loader and normalization differentials",
        "failure and recovery probing",
        "does **not** automatically become target product truth",
    ):
        if phrase not in low:
            errors.append("Adversarial limit-probing contract missing: %s" % phrase)
    return errors


def check_external_research_and_comparative_re(reference_text, workflow_text, qualification_text, external_text):
    errors = []
    reference_low = reference_text.lower()
    for phrase in (
        "external_research_and_corroboration.md",
        "public/internet research",
        "llm/decompiler-generated summaries",
    ):
        if phrase not in reference_low:
            errors.append("Reference external-research contract missing: %s" % phrase)
    for phrase in (
        "format-first dispatch",
        "nested packages/archives/bundles",
        "Bind the working analysis state",
        "Mechanism fan-out and enforcement-site coverage",
        "Comparative and cross-version analysis",
        "semantic anchors",
        "derived semantic hypotheses",
    ):
        if phrase not in workflow_text:
            errors.append("Comparative/analysis workflow missing: %s" % phrase)
    for phrase in (
        "MODEL_ASSISTED_HYPOTHESIS",
        "Raw evidence vs normalized candidate views",
    ):
        if phrase not in qualification_text:
            errors.append("Evidence qualification missing: %s" % phrase)
    for phrase in (
        "discovery and corroboration lane",
        "TARGET_CORROBORATED",
        "research packet",
        "Version and time discipline",
    ):
        if phrase not in external_text:
            errors.append("External research JIT missing: %s" % phrase)
    return errors


def check_package_hygiene(paths):
    errors = []
    for rel in paths:
        parts = set(rel.replace("\\", "/").split("/"))
        if parts.intersection(FORBIDDEN_PACKAGE_PARTS):
            errors.append("Generated/dependency directory must not ship: %s" % rel)
        if any(rel.endswith(suffix) for suffix in FORBIDDEN_PACKAGE_SUFFIXES):
            errors.append("Generated bytecode must not ship: %s" % rel)
    return errors


def repository_paths():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for filename in filenames:
            out.append(os.path.relpath(os.path.join(dirpath, filename), ROOT))
    return out


def structural_checks():
    errors = []
    package_paths = repository_paths()
    errors.extend(check_package_hygiene(package_paths))
    if "skills/corereplica-orchestration/references/CLEAN_ROOM_POLICY.md" in package_paths:
        error(errors, "Stale parallel source policy CLEAN_ROOM_POLICY.md must not ship")
    for rel in REQUIRED_DOCS:
        if not os.path.isfile(os.path.join(ROOT, rel)):
            error(errors, "Missing required authority/support file: %s" % rel)

    try:
        manifest = json.loads(read("plugin.json"))
    except Exception as exc:
        return ["plugin.json unreadable: %s" % exc]

    try:
        import yaml  # optional validation dependency
    except ImportError:
        yaml = None
    if yaml is not None:
        for rel in REQUIRED_DOCS:
            if rel.endswith(".yaml") and os.path.isfile(os.path.join(ROOT, rel)):
                try:
                    yaml.safe_load(read(rel))
                except Exception as exc:
                    error(errors, "Invalid YAML %s: %s" % (rel, exc))

    if manifest.get("name") != "corereplica":
        error(errors, "plugin name must be corereplica")
    if not re.match(r"^\d+\.\d+\.\d+$", str(manifest.get("version", ""))):
        error(errors, "plugin version must be strict semver")
    interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
    short = interface.get("shortDescription", "")
    if not short or len(short) > 30:
        error(errors, "shortDescription must be 1..30 characters")

    skills_root = os.path.join(ROOT, "skills")
    found = sorted(
        d for d in os.listdir(skills_root)
        if os.path.isfile(os.path.join(skills_root, d, "SKILL.md"))
    )
    if found != sorted(SKILLS):
        error(errors, "skill set mismatch: %r" % found)

    for name in SKILLS:
        rel = "skills/%s/SKILL.md" % name
        text = read(rel)
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            error(errors, "%s has invalid frontmatter" % rel)
            continue
        fm = m.group(1)
        if "name: %s" % name not in fm:
            error(errors, "%s frontmatter name mismatch" % rel)
        if "description:" not in fm:
            error(errors, "%s missing description" % rel)

    for rel in (
        "skills/corereplica-reference/assets/feature-observations.csv",
        "skills/corereplica-product/assets/requirements.csv",
    ):
        with open(os.path.join(ROOT, rel), newline="", encoding="utf-8") as fh:
            fields = [f.lower() for f in next(csv.reader(fh))]
        if rel.endswith("requirements.csv"):
            errors.extend(check_requirement_fields(fields))
        else:
            bad = sorted({"priority"}.union(FORBIDDEN_STATUS_FIELDS).intersection(fields))
            if bad:
                error(errors, "Reference observations contain target/state fields: %s" % ", ".join(bad))
            if "evidence_kind" not in fields:
                error(errors, "Reference observations missing evidence_kind proof-scope field")

    errors.extend(check_orchestration_text(read("skills/corereplica-orchestration/SKILL.md")))
    errors.extend(check_verifier_text(read("skills/corereplica-verify/SKILL.md")))
    errors.extend(check_release_text(read("skills/corereplica-release/SKILL.md")))
    errors.extend(check_reference_qualification_text(
        read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md")
    ))
    errors.extend(check_reverse_engineering_text(
        read("skills/corereplica-reference/SKILL.md"),
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-product/SKILL.md"),
        read("skills/corereplica-orchestration/SKILL.md"),
    ))
    errors.extend(check_runtime_corroboration_text(
        read("skills/corereplica-reference/SKILL.md"),
        read("skills/corereplica-reference/references/RUNTIME_CORROBORATION.md"),
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-orchestration/SKILL.md"),
    ))
    errors.extend(check_adversarial_limit_text(
        read("skills/corereplica-reference/references/ADVERSARIAL_LIMIT_PROBING.md")
    ))
    errors.extend(check_external_research_and_comparative_re(
        read("skills/corereplica-reference/SKILL.md"),
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md"),
        read("skills/corereplica-reference/references/EXTERNAL_RESEARCH_AND_CORROBORATION.md"),
    ))

    reference = read("skills/corereplica-reference/SKILL.md")
    for phrase in ("evidence_kind", "EVIDENCE_QUALIFICATION.md", "acquire", "identify", "qualify"):
        if phrase not in reference:
            error(errors, "Reference skill missing qualification contract: %s" % phrase)

    side = read("skills/corereplica-verify/references/SIDE_EFFECT_SAFE_VERIFICATION.md").lower()
    for phrase in ("baseline", "cleanup", "oracle", "inconclusive"):
        if phrase not in side:
            error(errors, "Side-effect verification contract missing: %s" % phrase)

    product = read("skills/corereplica-product/SKILL.md")
    for phrase in ("scope_status", "PROVISIONAL_INTERPRETATION"):
        if phrase not in product:
            error(errors, "Product contract missing: %s" % phrase)

    policy = read("skills/corereplica-orchestration/references/SOURCE_USE_AND_DISTRIBUTION_POLICY.md").lower()
    for phrase in (
        "access/analysis",
        "retain locally",
        "version control",
        "target product",
        "redistribut",
        "documented basis",
    ):
        if phrase not in policy:
            error(errors, "Source/use/distribution policy missing: %s" % phrase)

    workspace = read("skills/corereplica-orchestration/references/WORKSPACE_AND_STANDALONE.md").lower()
    for phrase in ("raw/reference evidence", "scratch/intermediate", "control-plane", "target/runnable/shippable"):
        if phrase not in workspace:
            error(errors, "Workspace-role contract missing: %s" % phrase)

    policy_surfaces = "\n".join([
        read("skills/corereplica-reference/SKILL.md"),
        read("skills/corereplica-design/SKILL.md"),
        read("skills/corereplica-build/SKILL.md"),
        read("skills/corereplica-release/SKILL.md"),
        read("docs/ARCHITECTURE_GUARDRAILS.yaml"),
        read("docs/USER_VISION.md"),
    ]).lower()
    for forbidden in (
        "obtain or copy proprietary source, bundles, binaries or decompiled implementation",
        "do not copy proprietary reference code/assets/copy/private apis",
        "do not copy proprietary assets/copy",
        "a source-code extractor, decompiler",
    ):
        if forbidden in policy_surfaces:
            error(errors, "Blanket source/material prohibition reintroduced: %s" % forbidden)

    prov = read("SOURCE_PROVENANCE.md")
    if "77c9436fb3d18c3d58169efb8caf4fe906b0dc51" not in prov:
        error(errors, "Replica upstream commit provenance missing")
    if "cab634bd855fc287f6e420c1f36fd1a6b9245960" not in prov:
        error(errors, "reverse-skill reviewed commit provenance missing")
    return errors


def self_test_mutants():
    failures = []
    if not check_requirement_fields(["id", "requirement", "priority", "clone"]):
        failures.append("requirements mutant with builder status was not rejected")

    verify = read("skills/corereplica-verify/SKILL.md") + "\n## Step 5: fix loop\nFix it yourself.\n"
    if not any("fix loop" in e.lower() for e in check_verifier_text(verify)):
        failures.append("verifier self-fix mutant was not rejected")

    release = read("skills/corereplica-release/SKILL.md").replace("explicit current approval", "approval")
    if not check_release_text(release):
        failures.append("release approval-boundary mutant was not rejected")

    orch = read("skills/corereplica-orchestration/SKILL.md").replace(
        "REFERENCE TRUTH != PRODUCT TRUTH != IMPLEMENTATION STATE != VERIFICATION TRUTH != RELEASE APPROVAL",
        "REFERENCE AND PRODUCT TRUTH ARE THE SAME",
    )
    if not check_orchestration_text(orch):
        failures.append("truth-layer collapse mutant was not rejected")

    orch_evidence = read("skills/corereplica-orchestration/SKILL.md").replace(
        "CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY",
        "CLAIMS MAY EXCEED AVAILABLE EVIDENCE",
    )
    if not check_orchestration_text(orch_evidence):
        failures.append("claim-strength mutant was not rejected")

    eq = read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md")
    eq_mutant = eq.replace("multiple plausible matches → UNRESOLVED", "multiple plausible matches → ACCEPT")
    if not check_reference_qualification_text(eq_mutant):
        failures.append("ambiguous-resolution evidence mutant was not rejected")

    reverse_reference = read("skills/corereplica-reference/SKILL.md")
    reverse_mutant = reverse_reference.replace("recover as much useful technical knowledge as practical", "minimum surface observation")
    if not check_reverse_engineering_text(
        reverse_mutant,
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-product/SKILL.md"),
        read("skills/corereplica-orchestration/SKILL.md"),
    ):
        failures.append("reference-recovery-depth mutant was not rejected")

    apc_orch = read("skills/corereplica-orchestration/SKILL.md").replace(
        "CoreReplica owns **reference recovery**, not durable project compilation",
        "CoreReplica owns reference recovery and durable project compilation",
    )
    if not check_reverse_engineering_text(
        read("skills/corereplica-reference/SKILL.md"),
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-product/SKILL.md"),
        apc_orch,
    ):
        failures.append("CoreReplica/APC ownership-collapse mutant was not rejected")

    runtime = read("skills/corereplica-reference/references/RUNTIME_CORROBORATION.md")
    runtime_mutant = runtime.replace(
        "not a blanket requirement to launch every target",
        "every target must always be launched regardless of claim boundary",
    )
    if not check_runtime_corroboration_text(
        read("skills/corereplica-reference/SKILL.md"),
        runtime_mutant,
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-orchestration/SKILL.md"),
    ):
        failures.append("runtime-claim-sensitivity mutant was not rejected")

    ext = read("skills/corereplica-reference/references/EXTERNAL_RESEARCH_AND_CORROBORATION.md")
    ext_mutant = ext.replace("TARGET_CORROBORATED", "TARGET_ASSUMED_FROM_WEB")
    if not check_external_research_and_comparative_re(
        read("skills/corereplica-reference/SKILL.md"),
        read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md"),
        read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md"),
        ext_mutant,
    ):
        failures.append("external-target-corroboration mutant was not rejected")

    if not check_package_hygiene(["skills/x/__pycache__/a.pyc"]):
        failures.append("package-hygiene mutant with generated bytecode was not rejected")
    return failures


def run_tests():
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        text=True,
        env=env,
    ).returncode


def main():
    errors = structural_checks()
    mutants = self_test_mutants()
    if errors:
        print("CoreReplica structural gate: FAIL")
        for e in errors:
            print("- %s" % e)
        return 1
    if mutants:
        print("CoreReplica validator self-test: FAIL")
        for e in mutants:
            print("- %s" % e)
        return 1
    print("CoreReplica structural gate: PASS")
    print("CoreReplica validator self-test: PASS")
    code = run_tests()
    if code:
        print("CoreReplica regression gate: FAIL")
        return code
    print("CoreReplica regression gate: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
