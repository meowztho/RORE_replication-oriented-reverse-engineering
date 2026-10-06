# CoreReplica Context Handoff — v0.1.1

## Current state

CoreReplica is a new skills-only Agent Plugin derived from the MIT `replica-skill` source at commit `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`.

The rewrite was initiated after a Core-First review found five structural failure classes in the upstream pack:

1. reference observations could become product truth without an explicit target-product decision layer;
2. a single feature matrix mixed reference scope, priorities, implementation progress and parity/completion;
3. the architecture skill could create a parallel architecture authority instead of first resolving current project owners;
4. the test skill both verified and fixed its own findings;
5. parity and deploy each carried overlapping completion/release semantics inside a mandatory sequential pipeline.

## Canonical correction

CoreReplica v0.1 uses:

```text
Reference Truth
→ explicit product decision
→ Product Truth
→ Core-First owner/change resolution when material
→ implementation progress
→ independent Verification Truth
→ release readiness
→ exact approval gate
→ consequential transition
```

The skills are JIT-routed rather than mandatory-sequential.

## Protected decisions

- Keep Core-First Governance as an external procedural owner when available; do not fork its full architecture method into CoreReplica.
- Keep Agent Project Compiler truth/authority/verification separation in the project model.
- Preserve the upstream MIT license and provenance for adapted scripts/templates.
- Builder status is non-authoritative for acceptance.
- Verification is read-only by default and records a finding before any correction path begins.
- Market/brand provides brand profile inputs; Design remains the semantic design-system owner.
- Release preparation may continue until the exact gated transition; broad requests do not imply approval.
- Current external platform/legal/pricing facts are JIT research concerns, not timeless plugin truth.

## v0.1.1 pre-test hardening

A critical comparison against the original Replica v1.0 pack found that the architectural rewrite was sound but several useful domain procedures had been compressed too aggressively. v0.1.1 restores that detail only behind existing JIT owners: backend/integration checks, flow/edge-case verification, market/brand/launch procedures, and production-readiness checks. The eight-skill ownership model and non-linear routing remain unchanged.

The private-plugin packaging stage is complete. Field evaluation is now ready.

## Next work after v0.1.1 package

Run real field evaluations against reference-driven projects. Admit additional governance text only for observed failures where a minimal provider-neutral intervention measurably improves behavior.
