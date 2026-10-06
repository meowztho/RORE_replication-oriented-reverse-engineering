# CoreReplica

CoreReplica is a skills-only Agent Plugin for building **independent products informed by reference products** without turning reference observations into product truth or letting implementation agents certify their own completion.

It is derived from the MIT-licensed `Jakeschincariol/replica-skill` ideas and deterministic helpers, but replaces the original mandatory 11-step pipeline with Core-First ownership, material-triggered JIT routing, separate truth layers, read-only verification, and an exact release gate.

## Core model

```text
Reference evidence
  != Product requirements
  != Implementation progress
  != Verification evidence
  != Release approval
```

The primary agent remains the integrator. When architecture, ownership, reuse, producer convergence, authoritative state, capability boundaries, or extension semantics are material, CoreReplica routes to the installed `core-first-extension-architecture` procedure when available. Real user/external runtime claims route to `observable-product-verification` when available. CoreReplica remains usable without those plugins through its project-native fallback rules.

## Skills

| Skill | Responsibility |
| --- | --- |
| `corereplica-orchestration` | Small JIT router, truth/freshness/gate discipline |
| `corereplica-reference` | Clean-room reference observation and evidence |
| `corereplica-product` | Independent target product scope and adopt/adapt/reject decisions |
| `corereplica-design` | Design-system semantics and visual reference translation |
| `corereplica-build` | Implementation through existing canonical owners; progress only |
| `corereplica-verify` | Read-only runtime/flow/parity verification and evidence |
| `corereplica-market` | Review research, differentiation, brand profile, launch material |
| `corereplica-release` | Release preparation and exact publish/go-live gate |

There is **no mandatory linear sequence**. The router loads only the skill or reference whose trigger is material.

## Target-project artifact model

CoreReplica skills normally write beneath `corereplica/` in the user's project:

```text
corereplica/
  reference/       reference observations and source evidence only
  product/         user/compiler-authoritative target product scope
  design/          design-system contracts and reference interpretation
  implementation/  non-authoritative progress/build notes
  verification/    test plans, findings, evidence records, parity reports
  market/          review research, positioning and brand profile
  release/         release preparation and gate evidence
```

A project that already has stronger canonical authorities should route into those instead of creating duplicate truth.

## Deterministic helpers

CoreReplica retains/adapts six standard-library helpers from the upstream MIT project:

- `contrast.py` — token contrast checks;
- `imgdiff.py` — heuristic structural screenshot comparison;
- `parity.py` — **rewritten** to score target requirements from verification evidence rather than builder self-report;
- `reviews.py` — sourced review-theme analysis;
- `sweep.py` — original-name/domain/color residue scan;
- `listing.py` — listing-field linting.

These helpers produce evidence. They are never architecture or completion owners.

## Validate

```bash
python3 scripts/validate_project.py
```

The gate validates plugin structure/governance invariants and runs the tool regression suite.

## Provenance and license

See `SOURCE_PROVENANCE.md` and `THIRD_PARTY_NOTICES.md`. Upstream portions remain under the MIT License.
