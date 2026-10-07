import csv
import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class EvidenceQualificationContract(unittest.TestCase):
    def test_reference_schema_scopes_evidence_kind_separately_from_confidence(self):
        with open(
            os.path.join(ROOT, "skills", "corereplica-reference", "assets", "feature-observations.csv"),
            newline="",
            encoding="utf-8",
        ) as fh:
            fields = [f.lower() for f in next(csv.reader(fh))]
        self.assertIn("evidence_kind", fields)
        self.assertIn("confidence", fields)

    def test_reference_qualification_is_jit_not_a_new_owner(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        self.assertIn("EVIDENCE_QUALIFICATION.md", ref)
        self.assertIn("acquire", ref)
        self.assertIn("identify", ref)
        self.assertIn("interpret", ref)
        self.assertIn("qualify", ref)
        self.assertFalse(
            os.path.exists(os.path.join(ROOT, "skills", "corereplica-reference-verifier", "SKILL.md"))
        )

    def test_identity_coverage_independence_and_precedence_fail_closed(self):
        eq = read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md")
        for phrase in (
            "Parseable output is not identity proof",
            "multiple plausible matches → UNRESOLVED",
            "value correctness",
            "population completeness",
            "materially independent failure modes",
            "UNRESOLVED_SOURCE_PRECEDENCE",
            "Current-view reconciliation",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, eq)

    def test_parser_safety_and_gate_competence_are_explicit(self):
        eq = read("skills/corereplica-reference/references/EVIDENCE_QUALIFICATION.md")
        self.assertIn("Parser safety", eq)
        self.assertIn("must not lose synchronization", eq)
        self.assertIn("representative relevant failure mode", eq)
        self.assertIn("A PASS cannot prove an invariant the gate does not test", eq)

    def test_source_policy_separates_retention_vcs_inclusion_and_redistribution(self):
        policy = read("skills/corereplica-orchestration/references/SOURCE_USE_AND_DISTRIBUTION_POLICY.md")
        for phrase in (
            "may retain locally after the active work",
            "may share/commit through VCS or collaboration systems",
            "may include in the target product",
            "may redistribute / publish / sublicense in the release",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, policy)

    def test_workspace_roles_prevent_scratch_from_becoming_truth(self):
        workspace = read("skills/corereplica-orchestration/references/WORKSPACE_AND_STANDALONE.md")
        for phrase in (
            "raw/reference evidence",
            "scratch/intermediate output",
            "control-plane/project metadata",
            "target/runnable/shippable payload",
            "must not silently become durable project truth",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, workspace)

    def test_new_evals_cover_empirical_failure_classes(self):
        evals = json.loads(read("skills/corereplica-orchestration/evals/evals.json"))
        ids = {e["id"] for e in evals}
        expected = {
            "identity-not-name-occurrence",
            "partial-coverage-not-complete",
            "shared-assumption-not-independent",
            "parser-desynchronization-fails-closed",
            "local-only-not-vcs",
            "layered-source-precedence",
            "gate-competence-negative-control",
            "stale-current-views",
        }
        self.assertTrue(expected.issubset(ids))

    def test_validator_self_tests_claim_strength_and_ambiguity(self):
        validator = read("scripts/validate_project.py")
        self.assertIn("claim-strength mutant was not rejected", validator)
        self.assertIn("ambiguous-resolution evidence mutant was not rejected", validator)


if __name__ == "__main__":
    unittest.main()
