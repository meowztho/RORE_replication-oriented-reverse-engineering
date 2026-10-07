# CoreReplica

CoreReplica is a skills-only Agent Plugin for **reverse-engineering and reconstructing authorized reference targets** and, when requested, using that knowledge to build an independent replica without collapsing Reference Truth into Product Truth.

Its primary job is to discover **how a piece of software, website, game, data format, service, package, workflow or system actually works**: inventory the target, extract/decompress/decode/decompile useful material, observe runtime behavior, connect static and dynamic evidence, recover structures/algorithms/dataflows, and turn the result into a usable reference corpus.

CoreReplica treats runtime as a claim-sensitive evidence boundary: static/package evidence may fully prove static claims, but effective loading, live state, exercised content, persistence, generated values and other runtime-sensitive claims require representative runtime corroboration when practical before they are called runtime-verified or complete.

CoreReplica may also use version-aware public research as a discovery/corroboration lane when it can resolve unknown formats, mechanisms, versions or source locations. External sources guide and challenge the local model; they do not silently replace target-local evidence for target-specific claims.

CoreReplica is not the project compiler. When Agent Project Compiler (APC) is selected, CoreReplica supplies the qualified reference corpus and APC compiles that material plus user intent into durable Product/Realization/Acceptance/Plan authorities. CoreReplica remains usable without APC through minimal fallback target-scope artifacts.

It incorporates useful ideas from the MIT-licensed `Jakeschincariol/replica-skill` and, from v0.3.0+, selected analysis-method ideas from the MIT-licensed `zhaoxuya520/reverse-skill`, while retaining Core-First owner/routing boundaries.

## Core model

```text
authorized target
→ survey / inventory
→ extract / unpack / decode / decompile when useful
→ static analysis + targeted runtime corroboration when material
→ qualified Evidence
→ Findings
→ causal/call/data/runtime Paths
→ Reference Model / usable corpus

Reference Truth
!= Product Truth
!= Implementation State
!= Verification Truth
!= Release Approval
```

Within Reference Truth:

```text
source acquired
!= correct object identified
!= correctly interpreted
!= complete population
!= independently corroborated claim
```

## CoreReplica ↔ APC boundary

```text
CoreReplica
  recover / qualify / connect reference knowledge
  ↓
Evidence + Findings + Paths + Reference Model
  ↓
APC (when selected)
  compile durable project authorities from user intent + reference corpus
  ↓
Product / Realization / System / Plan / Acceptance package
```

APC does not own reverse engineering or source extraction. CoreReplica does not create an APC-style project package merely because the reference analysis becomes rich.

## Skills

| Skill | Responsibility |
| --- | --- |
| `corereplica-orchestration` | JIT routing, truth/freshness/evidence/gate discipline, CoreReplica↔APC boundary |
| `corereplica-reference` | Reverse engineering, extraction, static/dynamic analysis, evidence qualification, Findings/Paths/Reference Model |
| `corereplica-product` | Minimal replica-target decisions when no stronger project Product Truth owner already exists |
| `corereplica-design` | Design-system semantics and visual reference translation |
| `corereplica-build` | Direct replica implementation through existing canonical project/workspace owners; progress only |
| `corereplica-verify` | Read-only target runtime/flow/parity verification and evidence |
| `corereplica-market` | Review research, differentiation, brand profile, launch material |
| `corereplica-release` | Release preparation and exact publish/go-live gate |

There is **no mandatory linear sequence**. Reverse-engineering depth is progressive and target-dependent; the router loads only material procedures.

## Reference corpus

For a substantial reference investigation, the fallback control-plane corpus may contain:

```text
corereplica/reference/
  SOURCE_LOG.md
  INVENTORY.md
  HYPOTHESES.md
  FEATURE_OBSERVATIONS.csv
  EVIDENCE/            raw/qualified observation records or precise refs
  FINDINGS.md          supported interpretations / recovered behavior
  PATHS.md             call/data/runtime/user-flow relationships
  REFERENCE_MODEL.md   synthesized usable model
  DERIVED/             reproducible parsed/converted views
  scratch/             local-only intermediates when needed
```

Do not create every artifact for a small visual study. Use them only when the investigation benefits from them.

## Reverse-engineering depth

`corereplica-reference` JIT-loads `REVERSE_ENGINEERING_WORKFLOW.md` when the target requires extraction, decompilation, static/dynamic analysis, browser/runtime observation, protocol/data-format recovery, or system reconstruction. It loads `RUNTIME_CORROBORATION.md` when a material claim depends on effective running behavior or broad reconstruction would otherwise overstate runtime coverage. It loads `ADVERSARIAL_LIMIT_PROBING.md` when hidden contracts are best exposed through boundary, sequence, replay, timing/concurrency, parser/layer or failure/recovery perturbations. It loads `EXTERNAL_RESEARCH_AND_CORROBORATION.md` when public documentation/source/history/research can resolve an unknown or reveal a new local evidence path. It JIT-loads `EVIDENCE_QUALIFICATION.md` when identity, parser correctness, coverage, source layering or corroboration are material.

The aim is **maximum useful recoverable knowledge within the authorized scope**, not the minimum observation needed to close one claim. For broad reconstruction, CoreReplica also challenges coverage across user flows, functional rules, architecture/ownership, data/content, algorithms, packages/assets, runtime/persistence, integrations/protocols, visual/media semantics, version/layering, install/update/portability, timing/resource behavior and failure/trust boundaries where material.

Before direct replica product decisions, CoreReplica preserves a compact reference-trait handoff (`trait → evidence/findings/paths → confidence/runtime status → limitations/constraints`) so earlier Reference→Product semantics are not lost as the RE corpus becomes richer. Start with cheap breadth, then deepen high-value unresolved areas until the requested coverage is reached, the next step is blocked, or additional work has sharply diminishing information value.

## Deterministic helpers

CoreReplica retains/adapts six standard-library helpers from the original Replica project: `contrast.py`, `imgdiff.py`, evidence-based `parity.py`, `reviews.py`, `sweep.py`, and `listing.py`. These produce narrow evidence only; they are not architecture or completion owners.

## Validate

```bash
python3 scripts/validate_project.py
```

The gate validates package/governance invariants, representative known-bad mutants, and the regression suite.

## Provenance and license

See `SOURCE_PROVENANCE.md`, `THIRD_PARTY_NOTICES.md`, `LICENSE-UPSTREAM`, and `LICENSE-REVERSE-SKILL`. CoreReplica itself is MIT licensed.
