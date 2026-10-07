# Routing and Context

## Cross-boundary sequencing

A request may legitimately require several procedures, but correctness must not depend on all skills being loaded simultaneously.

Typical sequence:

```text
reference target / unknown
→ corereplica-reference
→ Evidence → Findings → Paths → Reference Model
→ APC when durable project compilation is requested/selected
   OR corereplica-product for standalone direct target decisions
→ explicit target decision
→ Core-First owner/change resolution when material
→ corereplica-build
→ corereplica-verify / OPV
```

Market research may run before implementation when the user is deciding whether/what to build. APC is an optional downstream compiler, not a CoreReplica prerequisite: it consumes the qualified reference corpus and user intent; unresolved reference questions route back to CoreReplica rather than being invented during compilation. Release may prepare independently once sufficient project truth/evidence exists.

## Core-First binding

When available:

- use `core-first-orchestration` for software-work routing/freshness/review semantics;
- use `core-first-extension-architecture` for architecture/ownership/reuse/change decisions;
- use `observable-product-verification` for real user/external outcomes;
- use `core-first-verifier` only as a fresh architecture conformance layer;
- use `independent-review` only when consequential/high-risk/difficult-to-verify/materially blocked.

CoreReplica skills remain domain procedures. They must not duplicate the full Core-First method or pretend a missing plugin was loaded.

## Context invalidation

Treat loaded skill bodies, reference observations, external facts, working plans and verification evidence as potentially stale. Re-check the relevant source/authority after:

- fresh session or major compaction;
- repository/project switch;
- skill/authority revision;
- target product scope change;
- material code/runtime change;
- reference product change when the claim depends on current behavior;
- platform/store/provider rule changes.

## Verification role coordination

When companion procedures are present, keep one purpose per lane:

- **CoreReplica Verify** — owns target-requirement/parity evidence records and finding handoff for the reconstruction effort;
- **Observable Product Verification (OPV)** — supplies the procedure/evidence for real user/external outcomes when that boundary is material; its evidence can feed CoreReplica Verify instead of creating a parallel acceptance truth;
- **Core-First Verifier** — independently checks architecture/ownership/reuse conformance only;
- **Independent Review** — reviews consequential implementation quality/risk when triggered, not target parity.

A project-native Acceptance/completion authority may sit above all of these. Do not require every lane on every change and do not count the same observation as several independent proofs.
