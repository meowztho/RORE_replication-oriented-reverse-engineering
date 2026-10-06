# Routing and Context

## Cross-boundary sequencing

A request may legitimately require several procedures, but correctness must not depend on all skills being loaded simultaneously.

Typical sequence:

```text
reference uncertainty
→ corereplica-reference
→ raw observation/evidence
→ corereplica-product
→ explicit target decision
→ Core-First owner/change resolution when material
→ corereplica-build
→ corereplica-verify / OPV
```

Market research may run before implementation when the user is deciding whether/what to build. Release may prepare independently once sufficient project truth/evidence exists.

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
