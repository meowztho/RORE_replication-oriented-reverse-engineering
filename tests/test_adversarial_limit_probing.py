import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class AdversarialLimitProbing(unittest.TestCase):
    def test_reference_routes_limit_probing_jit(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        orch = read("skills/corereplica-orchestration/SKILL.md")
        self.assertIn("ADVERSARIAL_LIMIT_PROBING.md", ref)
        self.assertIn("ADVERSARIAL_LIMIT_PROBING.md", orch)
        self.assertIn("Challenge assumptions", ref)

    def test_probing_is_for_mechanism_not_maximum_impact(self):
        probe = read("skills/corereplica-reference/references/ADVERSARIAL_LIMIT_PROBING.md")
        self.assertIn("proof of mechanism", probe)
        self.assertIn("not exploit maximization", probe)
        self.assertIn("one primary variable", probe)
        self.assertIn("State-machine and logic probing", probe)
        self.assertIn("Timing, concurrency and drift", probe)
        self.assertIn("Parser, loader and normalization differentials", probe)
        self.assertIn("Failure and recovery probing", probe)

    def test_bug_remains_reference_truth_until_product_decision(self):
        probe = read("skills/corereplica-reference/references/ADVERSARIAL_LIMIT_PROBING.md")
        integration = read("docs/SYSTEM_INTEGRATION.yaml")
        self.assertIn("does **not** automatically become target Product Truth", probe)
        self.assertIn("adversarial probing findings being promoted directly into target requirements", integration)

    def test_no_new_security_owner_or_capability(self):
        cap = read("docs/CAPABILITY_GRAPH.yaml")
        decisions = read("docs/DECISION_COMPENDIUM.md")
        self.assertIn("controlled adversarial limit probes", cap)
        self.assertNotIn("CAP_PENTEST", cap)
        self.assertNotIn("CAP_EXPLOIT", cap)
        self.assertIn("not a new security owner", decisions)

    def test_behavioral_evals_cover_adversarial_reasoning(self):
        evals = json.loads(read("skills/corereplica-orchestration/evals/evals.json"))
        ids = {e["id"] for e in evals}
        expected = {
            "limit-probe-hidden-state-machine",
            "race-probe-for-understanding-not-impact",
            "parser-layer-differential",
            "reference-bug-does-not-become-product-requirement",
            "failure-path-reveals-owner",
        }
        self.assertTrue(expected.issubset(ids))


if __name__ == "__main__":
    unittest.main()
