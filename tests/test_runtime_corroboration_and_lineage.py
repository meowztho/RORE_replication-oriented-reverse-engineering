import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class RuntimeCorroborationAndLineage(unittest.TestCase):
    def test_runtime_is_claim_sensitive_not_mandatory_launch(self):
        runtime = read("skills/corereplica-reference/references/RUNTIME_CORROBORATION.md")
        self.assertIn("claim-sensitive", runtime)
        self.assertIn("not a blanket requirement to launch every target", runtime)
        self.assertIn("STATIC_SUFFICIENT", runtime)
        self.assertIn("RUNTIME_SENSITIVE", runtime)
        self.assertIn("RUNTIME_UNAVAILABLE", runtime)

    def test_runtime_sensitive_claims_fail_closed_without_real_boundary(self):
        runtime = read("skills/corereplica-reference/references/RUNTIME_CORROBORATION.md")
        self.assertIn("not started + runtime-sensitive claim presented as verified/complete", runtime)
        self.assertIn("RUNTIME_UNCHECKED", runtime)
        self.assertIn("RUNTIME_PARTIAL", runtime)
        self.assertIn("RUNTIME_BLOCKED", runtime)
        self.assertIn("representative authorized real run", runtime)

    def test_presence_and_effective_runtime_use_are_distinct(self):
        runtime = read("skills/corereplica-reference/references/RUNTIME_CORROBORATION.md")
        for phrase in ("PRESENT", "REFERENCED", "REACHABLE", "EXERCISED", "EFFECTIVE"):
            self.assertIn(phrase, runtime)
        self.assertIn("dead/legacy", runtime)

    def test_runtime_identity_must_match_static_target(self):
        runtime = read("skills/corereplica-reference/references/RUNTIME_CORROBORATION.md")
        self.assertIn("matches the analyzed artifact/version/build/environment", runtime)
        self.assertIn("cross-version/cross-environment evidence", runtime)

    def test_reference_owner_routes_runtime_jit(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        orch = read("skills/corereplica-orchestration/SKILL.md")
        index = read("docs/PROJECT_INDEX.yaml")
        self.assertIn("RUNTIME_CORROBORATION.md", ref)
        self.assertIn("RUNTIME_CORROBORATION.md", orch)
        self.assertIn("runtime_corroboration", index)
        self.assertIn("runtime-sensitive", ref.lower())

    def test_broad_reconstruction_coverage_is_explicit(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        model = read("skills/corereplica-reference/assets/reference-model.md")
        self.assertIn("Reconstruction coverage challenge", ref)
        self.assertIn("installation/update/relocation/portability/environment", ref)
        self.assertIn("timing/concurrency/performance/resource semantics", ref)
        self.assertIn("covered | partial | unresolved | not_applicable | out_of_scope", model)

    def test_v02_reference_trait_handoff_is_restored(self):
        ref = read("skills/corereplica-reference/SKILL.md")
        model = read("skills/corereplica-reference/assets/reference-model.md")
        self.assertIn("Replica trait handoff", ref)
        for phrase in (
            "trait id",
            "observed behavior/pattern/mechanism",
            "source Evidence / Findings / Paths",
            "runtime status when material",
            "adopt | adapt | reject | inspiration-only",
        ):
            self.assertIn(phrase, ref)
        self.assertIn("## Replica trait candidates", model)

    def test_system_flow_has_runtime_and_trait_boundaries(self):
        integration = read("docs/SYSTEM_INTEGRATION.yaml")
        self.assertIn("targeted runtime corroboration", integration)
        self.assertIn("compact replica trait candidates", integration)
        self.assertIn("runtime-sensitive static inference", integration)

    def test_decisions_and_guardrail_materialize_runtime_boundary(self):
        decisions = read("docs/DECISION_COMPENDIUM.md")
        guardrails = read("docs/ARCHITECTURE_GUARDRAILS.yaml")
        self.assertIn("D-021 — Claim-sensitive runtime corroboration", decisions)
        self.assertIn("D-022 — Reconstruction coverage and replica-trait continuity", decisions)
        self.assertIn("G019", guardrails)
        self.assertIn("Runtime-sensitive reference claims", guardrails)

    def test_behavioral_evals_cover_runtime_and_lineage_failures(self):
        evals = json.loads(read("skills/corereplica-orchestration/evals/evals.json"))
        ids = {e["id"] for e in evals}
        expected = {
            "runtime-sensitive-claim-needs-representative-run",
            "static-only-claim-does-not-force-launch",
            "dead-content-presence-is-not-effective-use",
            "runtime-build-mismatch-stays-explicit",
            "broad-reconstruction-runs-coverage-challenge",
            "reference-trait-handoff-remains-explicit",
        }
        self.assertTrue(expected.issubset(ids))


if __name__ == "__main__":
    unittest.main()
