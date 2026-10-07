import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class ExternalResearchAndComparativeRE(unittest.TestCase):
    def test_external_research_is_jit_under_reference_owner(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        orch = read("skills/corereplica-orchestration/SKILL.md")
        ext = read("skills/corereplica-reference/references/EXTERNAL_RESEARCH_AND_CORROBORATION.md")
        self.assertIn("EXTERNAL_RESEARCH_AND_CORROBORATION.md", ref)
        self.assertIn("EXTERNAL_RESEARCH_AND_CORROBORATION.md", orch)
        self.assertIn("discovery and corroboration lane", ext)
        self.assertIn("TARGET_CORROBORATED", ext)
        self.assertIn("research packet", ext)

    def test_format_first_fallback_recursive_extraction(self):
        flow = read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md")
        for phrase in ("format-first dispatch", "alternate compatible extractor/parser", "nested packages/archives/bundles", "depth/size/resource bounds", "exit code alone"):
            self.assertIn(phrase, flow)

    def test_analysis_state_is_bound_to_target_identity(self):
        flow = read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md")
        self.assertIn("Bind the working analysis state", flow)
        self.assertIn("changed artifact", flow)
        self.assertIn("cross-version correlation", flow)

    def test_model_annotations_are_derived_hypotheses(self):
        flow = read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md")
        eq = read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md")
        self.assertIn("derived semantic hypotheses", flow)
        self.assertIn("MODEL_ASSISTED_HYPOTHESIS", eq)
        self.assertIn("reversible", flow)

    def test_mechanism_fanout_and_cross_version_semantic_anchors(self):
        flow = read("skills/corereplica-reference/references/REVERSE_ENGINEERING_WORKFLOW.md")
        self.assertIn("Mechanism fan-out and enforcement-site coverage", flow)
        self.assertIn("one decisive-looking check does not prove the complete mechanism", flow)
        self.assertIn("Comparative and cross-version analysis", flow)
        self.assertIn("semantic anchors", flow)
        self.assertIn("Absolute offsets/addresses are version-local evidence", flow)

    def test_raw_and_normalized_views_are_separate(self):
        eq = read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md")
        self.assertIn("Raw evidence vs normalized candidate views", eq)
        self.assertIn("derived", eq)
        self.assertIn("Do not silently replace", eq)

    def test_behavioral_evals_cover_new_failure_modes(self):
        evals = json.loads(read("skills/corereplica-orchestration/evals/evals.json"))
        ids = {e["id"] for e in evals}
        expected = {
            "external-docs-do-not-become-target-truth",
            "offline-agent-emits-research-packet",
            "nested-container-fallback-extraction",
            "changed-hash-invalidates-session-assumptions",
            "distributed-enforcement-sites-require-coverage",
            "cross-version-port-uses-semantic-anchors",
            "llm-decompiler-summary-is-derived-hypothesis",
            "raw-evidence-and-normalized-view-stay-separate",
        }
        self.assertTrue(expected.issubset(ids))


if __name__ == "__main__":
    unittest.main()
