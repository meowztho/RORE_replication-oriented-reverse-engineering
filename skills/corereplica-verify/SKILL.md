---
name: corereplica-verify
description: Independently verify CoreReplica target requirements and parity from current evidence. Use for QA, runtime/user-flow checks, process/filesystem/registry/database/network/external-service outcomes, accessibility/visual checks, screenshot comparison, bug reproduction, acceptance evidence, or "how close/does it work/is it ready" questions. Read-only with respect to product implementation by default; record findings before routing corrections and never trust builder progress as proof.
---

# CoreReplica Verification

Own **Verification Truth** for CoreReplica fallback artifacts. Do not own Product Truth, implementation fixes, architecture, or release approval.

## Core invariants

```text
implementation exists != connected != exercised != verified
implementation status != verification evidence
successful tool action != intended outcome
heuristic parity score != release readiness
```

When `observable-product-verification` is available and a real user/external outcome is material, load/use it as the real-boundary procedure and feed its evidence into this requirement/parity record rather than duplicating acceptance ownership.

## Inputs

- current target Product/Acceptance authorities;
- current implementation revision/state;
- applicable target Design/System authorities;
- reference evidence only when the requirement intentionally calls for parity/reference comparison;
- current runtime/test tools.

Do not derive target scope from the reference during verification.

## Outputs

Fallback artifacts:

```text
corereplica/verification/TEST_PLAN.md
corereplica/verification/FINDINGS.md
corereplica/verification/EVIDENCE.json
corereplica/verification/PARITY.md
corereplica/verification/diffs/
```

Evidence records use requirement IDs and describe what boundary was actually exercised. Visual evidence is only one boundary class; process state, filesystem, registry/config, database/persistence, network/API, external service, device/OS integration and user-visible UI are first-class when they are the actual acceptance boundary.

## Evidence schema

`EVIDENCE.json` is an object with `revision` and `requirements` entries:

```json
{
  "revision": "<git sha or other revision>",
  "requirements": {
    "REQ-001": {
      "status": "VERIFIED",
      "evidence": [
        {"kind": "runtime", "boundary": "filesystem|registry|process|browser|database|network|external-service|...", "ref": "...", "notes": "...", "side_effects": "contained/cleaned/none", "liveness": "checked/not-applicable"}
      ]
    }
  }
}
```

Allowed top-level requirement status: `VERIFIED | PARTIAL | FAILED | INCONCLUSIVE | SKIP`.

- `VERIFIED`: sufficient current evidence proves the full stated acceptance for this requirement.
- `PARTIAL`: evidence proves a strict subset; list what remains.
- `FAILED`: exercised evidence contradicts acceptance.
- `INCONCLUSIVE`: required evidence could not be acquired or does not prove the claim.
- `SKIP`: only when Product Truth explicitly excludes/deferred the requirement from the current scored scope.

## JIT depth

Read `references/FLOW_AND_PARITY_VERIFICATION.md` when multi-step flows, edge-case matrices, cross-user isolation, browser E2E, or intentional reference parity are material. Do not load it for a narrow unit/static verification claim.

## Procedure

1. Derive the test plan from **target requirements/acceptance**, not from reference flows alone. Identify the real acceptance boundary before choosing tools; do not default to screenshots for non-visual products. Reference flows may challenge parity only for adopted/adapted traits.
2. Before a potentially stateful/destructive real-boundary run, read `references/SIDE_EFFECT_SAFE_VERIFICATION.md` and establish isolation/baseline/cleanup or recovery as applicable. Then exercise the closest practical real boundary. For async/animation/navigation/persistence/network/physics, observe a meaningful settled state.
3. Use already acquired evidence broadly enough to notice obvious adjacent contradictions, but keep write scope narrow.
4. Record each failure with exact symptom identity, reproducible steps, expected/actual state, evidence, revision, and affected requirement.
5. Do **not** fix source implementation during the independent verification pass. Route the finding to the relevant canonical owner/implementation lane. After correction, verify the changed revision again.
6. Automated tests are valuable evidence for the claim they exercise. They do not automatically prove user-visible runtime behavior.
7. Image/layout comparison is heuristic structural evidence only and is optional; do not privilege it over the actual boundary. It deliberately cannot prove interaction, data integrity, persistence, accessibility semantics or business correctness.
8. If required tools/surfaces are unavailable, report `INCONCLUSIVE`; do not downgrade silently to static evidence.

## Evidence-based parity

Use `scripts/parity.py` with target requirements plus verifier-owned evidence. The tool must never read `IMPLEMENTATION_STATUS.csv` as acceptance.

Example:

```bash
python3 scripts/parity.py \
  corereplica/product/REQUIREMENTS.csv \
  corereplica/verification/EVIDENCE.json \
  --markdown
```

Use `scripts/imgdiff.py` only for intentionally comparable screenshots in the same state/viewport. Read `references/FLOW_AND_PARITY_VERIFICATION.md` for edge-case flow design and `references/SIDE_EFFECT_SAFE_VERIFICATION.md` before real runs that can leave state behind.

## Correction handoff

Return a correction packet rather than editing the product:

```text
requirement ID
exact observable symptom
reproduction/evidence
likely runtime path / owner if grounded
what remains unproven
required re-verification boundary
```

If architecture/ownership is implicated, route the reverse trace through Core-First before the implementation lane changes code.
