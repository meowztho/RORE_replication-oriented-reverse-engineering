import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class ReferenceReverseEngineering(unittest.TestCase):
    def test_reference_owner_is_reverse_engineering_not_surface_only(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        for phrase in (
            "recover as much useful technical knowledge as practical",
            "extract / unpack / decode / decompile",
            "static structural analysis",
            "dynamic/runtime observation",
            "Evidence → Finding → Path",
            "Reference Model",
        ):
            self.assertIn(phrase, ref)

    def test_reverse_engineering_depth_is_jit_not_fixed_pipeline(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        workflow = read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md")
        self.assertIn("REVERSE_ENGINEERING_WORKFLOW.md", ref)
        self.assertIn("not a mandatory linear pipeline", ref.lower())
        self.assertIn("Broad triage before narrow depth", workflow)
        self.assertIn("Static analysis", workflow)
        self.assertIn("Dynamic/runtime analysis", workflow)
        self.assertIn("Hypothesis-driven replanning", workflow)
        self.assertIn("Coverage and gap loop", workflow)

    def test_tool_discovery_is_provider_neutral_and_not_guessed(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        workflow = read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md")
        self.assertIn("actually available capabilities, paths and versions", ref)
        self.assertIn("do not guess executable paths", ref)
        self.assertIn("CoreReplica does not require or bundle a universal toolchain", workflow)

    def test_reference_corpus_has_evidence_findings_paths_model(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        for path in (
            "corereplica/reference/EVIDENCE/",
            "corereplica/reference/FINDINGS.md",
            "corereplica/reference/PATHS.md",
            "corereplica/reference/REFERENCE_MODEL.md",
            "corereplica/reference/DERIVED/",
        ):
            self.assertIn(path, ref)

    def test_apc_is_downstream_compiler_not_reference_owner(self):
        orch = read("skills/corereplica-orchestration/SKILL.md")
        product = read("skills/corereplica-product/SKILL.md")
        decisions = read("docs/DECISION_COMPENDIUM.md")
        self.assertIn("CoreReplica owns **reference recovery**, not durable project compilation", orch)
        self.assertIn("APC owns compilation", orch)
        self.assertIn("Do not generate APC-style System Map/Plan/Acceptance/Blueprint artifacts here", product)
        self.assertIn("D-004 — APC boundary", decisions)

    def test_system_integration_routes_corpus_before_compilation(self):
        integration = read("docs/SYSTEM_INTEGRATION.yaml")
        self.assertIn("qualified Evidence", integration)
        self.assertIn("Findings + Paths + Reference Model", integration)
        self.assertIn("APC durable project compilation", integration)
        self.assertIn("APC inventing unresolved reference behavior", integration)

    def test_reverse_skill_provenance_and_license_are_retained(self):
        prov = read("SOURCE_PROVENANCE.md")
        notices = read("THIRD_PARTY_NOTICES.md")
        self.assertIn("cab634bd855fc287f6e420c1f36fd1a6b9245960", prov)
        self.assertIn("zhaoxuya520/reverse-skill", prov)
        self.assertIn("zhaoxuya520/reverse-skill", notices)
        self.assertTrue(os.path.isfile(os.path.join(ROOT, "LICENSE-REVERSE-SKILL")))

    def test_behavioral_evals_cover_recovery_and_apc_boundary(self):
        evals = json.loads(read("skills/corereplica-orchestration/evals/evals.json"))
        ids = {e["id"] for e in evals}
        expected = {
            "broad-reference-recovery-does-not-stop-at-surface",
            "tool-discovery-before-specialized-analysis",
            "static-dynamic-disagreement-stays-evidence-driven",
            "reference-corpus-handoff-to-apc",
            "apc-does-not-own-reverse-engineering",
        }
        self.assertTrue(expected.issubset(ids))


if __name__ == "__main__":
    unittest.main()
