import csv
import json
import os
import re
import unittest

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


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class Governance(unittest.TestCase):
    def test_manifest_identity_and_skill_set(self):
        manifest = json.loads(read("plugin.json"))
        self.assertEqual(manifest["name"], "corereplica")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        short = manifest["extensions"]["com.openai"]["interface"]["shortDescription"]
        self.assertLessEqual(len(short), 30)
        found = sorted(
            d for d in os.listdir(os.path.join(ROOT, "skills"))
            if os.path.isfile(os.path.join(ROOT, "skills", d, "SKILL.md"))
        )
        self.assertEqual(found, sorted(SKILLS))

    def test_skill_frontmatter_names_and_trigger_descriptions(self):
        for name in SKILLS:
            text = read("skills/%s/SKILL.md" % name)
            m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            self.assertIsNotNone(m, name)
            fm = m.group(1)
            self.assertIn("name: %s" % name, fm)
            self.assertIn("description:", fm)
            self.assertRegex(fm.lower(), r"use (when|for)")
            # Negative/limiting trigger language prevents skill sprawl.
            self.assertRegex(fm.lower(), r"do not|without|only|read-only|route")

    def test_no_mandatory_upstream_pipeline(self):
        orchestration = read("skills/corereplica-orchestration/SKILL.md").lower()
        self.assertIn("do not preload all siblings", orchestration)
        self.assertIn("no mandatory linear sequence", read("README.md").lower())
        self.assertNotIn("recon -> architect -> design -> build -> backend -> test -> diff", orchestration)

    def test_truth_layers_are_explicit(self):
        orch = read("skills/corereplica-orchestration/SKILL.md")
        self.assertIn("REFERENCE TRUTH != PRODUCT TRUTH != IMPLEMENTATION STATE != VERIFICATION TRUTH != RELEASE APPROVAL", orch)
        product = read("skills/corereplica-product/SKILL.md")
        self.assertIn("No `done`, `clone`, `verified`", product)
        self.assertIn("scope_status", product)
        self.assertIn("PROVISIONAL_INTERPRETATION", product)

    def test_reference_template_has_no_priority_or_completion(self):
        path = os.path.join(ROOT, "skills", "corereplica-reference", "assets", "feature-observations.csv")
        with open(path, newline="", encoding="utf-8") as fh:
            fields = [f.lower() for f in next(csv.reader(fh))]
        for forbidden in ("priority", "clone", "done", "verified", "implementation_status"):
            self.assertNotIn(forbidden, fields)

    def test_requirements_template_has_no_completion(self):
        path = os.path.join(ROOT, "skills", "corereplica-product", "assets", "requirements.csv")
        with open(path, newline="", encoding="utf-8") as fh:
            fields = [f.lower() for f in next(csv.reader(fh))]
        for forbidden in ("clone", "done", "verified", "implementation_status"):
            self.assertNotIn(forbidden, fields)

    def test_verifier_is_read_only_and_routes_correction(self):
        verify = read("skills/corereplica-verify/SKILL.md").lower()
        self.assertIn("read-only", verify)
        self.assertIn("do **not** fix source implementation", verify)
        self.assertIn("route the finding", verify)
        self.assertNotIn("## step 5: fix loop", verify)

    def test_release_exact_gate(self):
        release = read("skills/corereplica-release/SKILL.md").lower()
        self.assertIn("reversible preparation", release)
        self.assertIn("exact gated transition", release)
        self.assertIn("explicit current approval", release)
        self.assertIn("do not treat the deploy command's success as proof", release)

    def test_core_first_is_external_owner_not_forked_skill(self):
        self.assertNotIn("corereplica-architect", SKILLS)
        build = read("skills/corereplica-build/SKILL.md")
        self.assertIn("Core-First", build)
        system_map = read("docs/SYSTEM_MAP.yaml")
        self.assertIn("core_first_extension_architecture", system_map)

    def test_provenance_present(self):
        prov = read("SOURCE_PROVENANCE.md")
        self.assertIn("77c9436fb3d18c3d58169efb8caf4fe906b0dc51", prov)
        self.assertTrue(os.path.isfile(os.path.join(ROOT, "LICENSE-UPSTREAM")))

    def test_jit_procedural_depth_is_preserved_without_owner_sprawl(self):
        expected = [
            "skills/corereplica-build/references/BACKEND_AND_INTEGRATIONS.md",
            "skills/corereplica-verify/references/FLOW_AND_PARITY_VERIFICATION.md",
            "skills/corereplica-verify/references/SIDE_EFFECT_SAFE_VERIFICATION.md",
            "skills/corereplica-orchestration/references/WORKSPACE_AND_STANDALONE.md",
            "skills/corereplica-market/references/REVIEW_RESEARCH.md",
            "skills/corereplica-market/references/BRAND_AND_POSITIONING.md",
            "skills/corereplica-market/references/LAUNCH_AND_LISTING.md",
            "skills/corereplica-release/references/PRODUCTION_READINESS.md",
        ]
        for rel in expected:
            self.assertTrue(os.path.isfile(os.path.join(ROOT, rel)), rel)
            self.assertGreater(len(read(rel).splitlines()), 12, rel)
        verify = read("skills/corereplica-verify/SKILL.md")
        release = read("skills/corereplica-release/SKILL.md")
        self.assertIn("FLOW_AND_PARITY_VERIFICATION.md", verify)
        self.assertIn("PRODUCTION_READINESS.md", release)
        self.assertNotIn("fix s1 and s2 first", read(expected[1]).lower())

    def test_field_eval_is_materialized_and_next_eval_ready(self):
        plan = read("docs/PROJECT_PLAN.yaml")
        self.assertRegex(plan, r"P6_FIELD_EVAL_ANOTE[\s\S]*?status: complete")
        self.assertRegex(plan, r"P7_FIELD_EVAL_HARDENING[\s\S]*?status: complete")
        self.assertRegex(plan, r"P12_NEXT_FIELD_EVAL[\s\S]*?status: ready")

    def test_workspace_shape_and_standalone_degradation(self):
        orch = read("skills/corereplica-orchestration/SKILL.md")
        ref = read("skills/corereplica-orchestration/references/WORKSPACE_AND_STANDALONE.md")
        self.assertIn("binary/distribution package", orch)
        self.assertIn("Core-First is a preferred companion, not a hard runtime dependency", orch)
        self.assertIn("Do not require Git", ref)
        self.assertIn("outside the payload", ref)
        self.assertIn("Standalone mode", ref)
        self.assertIn("unresolved", ref.lower())

    def test_side_effect_safe_nonvisual_verification(self):
        verify = read("skills/corereplica-verify/SKILL.md")
        side = read("skills/corereplica-verify/references/SIDE_EFFECT_SAFE_VERIFICATION.md")
        self.assertIn("filesystem", verify)
        self.assertIn("registry", verify)
        self.assertIn("SIDE_EFFECT_SAFE_VERIFICATION.md", verify)
        self.assertIn("baseline", side.lower())
        self.assertIn("cleanup", side.lower())
        self.assertIn("oracle", side.lower())
        self.assertIn("INCONCLUSIVE", side)

    def test_verification_role_matrix_is_explicit(self):
        routing = read("skills/corereplica-orchestration/references/ROUTING_AND_CONTEXT.md")
        self.assertIn("CoreReplica Verify", routing)
        self.assertIn("Observable Product Verification", routing)
        self.assertIn("Core-First Verifier", routing)
        self.assertIn("Independent Review", routing)

    def test_source_use_distribution_policy_is_consistent(self):
        policy = read("skills/corereplica-orchestration/references/SOURCE_USE_AND_DISTRIBUTION_POLICY.md")
        self.assertIn("access/analysis", policy)
        self.assertIn("target-product inclusion and distribution", policy)
        self.assertIn("may access / inspect / analyze / transform for this task", policy)
        self.assertIn("may redistribute / publish / sublicense in the release", policy)
        self.assertIn("documented basis", policy)

        combined = "\n".join([
            read("skills/corereplica-reference/SKILL.md"),
            read("skills/corereplica-design/SKILL.md"),
            read("skills/corereplica-build/SKILL.md"),
            read("skills/corereplica-release/SKILL.md"),
            read("skills/corereplica-release/references/PRODUCTION_READINESS.md"),
            read("docs/ARCHITECTURE_GUARDRAILS.yaml"),
            read("docs/USER_VISION.md"),
        ])
        for phrase in ("provenance", "intended use", "redistribution"):
            self.assertIn(phrase, combined.lower())
        for forbidden in (
            "obtain or copy proprietary source, bundles, binaries or decompiled implementation",
            "do not copy proprietary reference code/assets/copy/private apis",
            "do not copy proprietary assets/copy",
            "a source-code extractor, decompiler",
        ):
            self.assertNotIn(forbidden, combined.lower())

    def test_authority_yaml_parses_when_yaml_runtime_is_available(self):
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML not installed")
        for rel in (
            "docs/ACCEPTANCE.yaml",
            "docs/ARCHITECTURE_GUARDRAILS.yaml",
            "docs/CAPABILITY_GRAPH.yaml",
            "docs/PRODUCT_REALIZATION.yaml",
            "docs/PROJECT_INDEX.yaml",
            "docs/PROJECT_PLAN.yaml",
            "docs/SYSTEM_INTEGRATION.yaml",
            "docs/SYSTEM_MAP.yaml",
        ):
            with self.subTest(rel=rel):
                yaml.safe_load(read(rel))


if __name__ == "__main__":
    unittest.main()
