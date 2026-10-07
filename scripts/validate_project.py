#!/usr/bin/env python3
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"rore-orchestration", "rore-reconstruction", "rore-evidence-review"}
REQUIRED = [
    "plugin.json", ".codex-plugin/plugin.json", "README.md", "SOURCE_PROVENANCE.md",
    "THIRD_PARTY_NOTICES.md", "LICENSE-UPSTREAM", "LICENSE-REVERSE-SKILL",
    "docs/USER_VISION.md", "docs/SYSTEM_MAP.yaml", "docs/CAPABILITY_GRAPH.yaml",
    "docs/ARCHITECTURE_GUARDRAILS.yaml", "docs/DECISION_COMPENDIUM.md",
    "docs/ACCEPTANCE.yaml", "docs/PROJECT_INDEX.yaml", "docs/SYSTEM_INTEGRATION.yaml",
    "skills/rore-orchestration/SKILL.md", "skills/rore-reconstruction/SKILL.md",
    "skills/rore-evidence-review/SKILL.md",
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def fail(msgs, msg):
    msgs.append(msg)


def structural_checks():
    e=[]
    for path in ROOT.rglob("*"):
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            fail(e, f"generated Python artifact must not ship: {path.relative_to(ROOT)}")
    for rel in REQUIRED:
        if not (ROOT/rel).is_file(): fail(e, f"missing {rel}")
    try:
        p=json.loads(read("plugin.json"))
        c=json.loads(read(".codex-plugin/plugin.json"))
    except Exception as exc:
        return [f"manifest parse: {exc}"]
    if p.get("name") != "corereplica": fail(e, "backend plugin identity changed")
    if p.get("version") != "0.4.2": fail(e, "version must be 0.4.2")
    iface=p.get("extensions",{}).get("com.openai",{}).get("interface",{})
    if iface.get("displayName") != "RORE": fail(e, "displayName must be RORE")
    if c.get("interface",{}).get("displayName") != "RORE": fail(e, "codex displayName must be RORE")

    found={d.name for d in (ROOT/"skills").iterdir() if (d/"SKILL.md").is_file()}
    if found != SKILLS: fail(e, f"skill set mismatch: {sorted(found)}")

    active="\n".join(read(x) for x in [
        "skills/rore-orchestration/SKILL.md",
        "skills/rore-reconstruction/SKILL.md",
        "skills/rore-evidence-review/SKILL.md",
        "docs/SYSTEM_MAP.yaml", "docs/CAPABILITY_GRAPH.yaml", "docs/SYSTEM_INTEGRATION.yaml"
    ])
    for forbidden in ("corereplica-product", "corereplica-build", "corereplica-release", "CR_PRODUCT", "CR_BUILD", "CR_RELEASE"):
        if forbidden in active: fail(e, f"active downstream owner residue: {forbidden}")
    if "Agent Project Compiler" in active or re.search(r"\bAPC\b", active):
        fail(e, "active RORE architecture must not depend on APC")

    recon=read("skills/rore-reconstruction/SKILL.md")
    for phrase in (
        "reference's own structure", "Negative Evidence", "continue | switch | stop",
        "sufficient mechanism understanding", "Evidence", "Finding", "Path", "Model"
    ):
        if phrase not in recon: fail(e, f"reconstruction contract missing: {phrase}")

    perturb=read("skills/rore-reconstruction/references/PERTURBATION_AND_CAUSAL_PROBING.md")
    for phrase in ("baseline", "one material dimension", "trace", "restore", "sufficient mechanism understanding", "not exploit"):
        if phrase.lower() not in perturb.lower(): fail(e, f"perturbation contract missing: {phrase}")

    review=read("skills/rore-evidence-review/SKILL.md")
    for phrase in ("read-only", "do not mutate", "do not silently", "Path integrity", "Reference-native fidelity"):
        if phrase.lower() not in review.lower(): fail(e, f"review contract missing: {phrase}")

    model=read("skills/rore-reconstruction/assets/reference-model.md")
    for ident in ("SUR-###", "FLOW-###", "STATE-###", "COMP-###", "ENT-###", "PROTO-###"):
        if ident not in model and ident == "STATE-###":
            # STATE identity is documented in the reconstruction skill; template may represent it through models.
            if ident not in recon: fail(e, f"stable identity missing: {ident}")
        elif ident not in model: fail(e, f"stable identity missing: {ident}")

    return e


def run_tests():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable,"-m","unittest","discover","-s","tests","-v"],cwd=ROOT,env=env).returncode


def main():
    errors=structural_checks()
    if errors:
        print("RORE structural gate: FAIL")
        for x in errors: print("-",x)
        return 1
    print("RORE structural gate: PASS")
    code=run_tests()
    if code:
        print("RORE regression gate: FAIL")
        return code
    print("RORE regression gate: PASS")
    return 0

if __name__=="__main__": raise SystemExit(main())
