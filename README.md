# RORE — Replication-Oriented Reverse Engineering

RORE is a provider-neutral Agent Plugin for **deep reconstruction of authorized reference systems**. Its purpose is to recover how a reference actually behaves and is structured — not to decide what a new product should be, not to redesign the reference for a builder, and not to implement or release a replica.

The word *replication-oriented* describes the required depth: RORE should recover enough reference truth that a later human, agent, compiler or project process could make informed decisions without RORE prematurely translating the original into a different architecture.

The current package keeps that boundary unchanged. It covers evidence freshness, reviewer independence, justified descent to lower-level binary/memory facts, source trust and API projection across distinct system layers.

## Boundary

```text
REFERENCE TARGET
→ observe / acquire / inventory
→ extract / decode / decompile / inspect
→ dynamic + runtime + memory analysis when useful
→ controlled perturbation to expose hidden causality
→ qualify Evidence
→ Findings
→ Paths
→ reference-native Models
→ coverage / contradictions / unknowns
= REFERENCE TRUTH
STOP RORE
```

RORE does **not** own target requirements, target architecture, product planning, implementation, replica acceptance, branding, launch or release. It has no APC dependency and does not compile a downstream project package.

## Active skills

| Skill | Responsibility |
| --- | --- |
| `rore-orchestration` | Choose the next analysis method from target/surface, current knowledge gap, required evidence boundary and available capabilities. |
| `rore-reconstruction` | Acquire, interpret and connect evidence into Findings, Paths and reference-native models while preserving the original system's structure and uncertainty. |
| `rore-evidence-review` | Read-only audit of evidence sufficiency, fixity, traceability, contradictions, coverage and claim overreach. |

These are canonical responsibilities, not a mandatory three-stage pipeline. Narrow work may use only reconstruction; evidence review is triggered when a claim, handoff, broad completeness statement or high-consequence interpretation needs an independent check.

## Core evidence model

```text
Evidence = directly observed/acquired fact or bounded derived artifact
Finding  = evidence-backed interpretation
Path     = grounded relationship/flow/cause connecting evidence/findings
Model    = a reference-native synthesis: surface, state, component, data,
           protocol, causal, asset, mechanics, architecture, etc.
```

RORE preserves several distinctions:

```text
parseable output != correct object identity
correct subset != population completeness
two tools agree != independent corroboration
present != referenced != reachable != exercised != effective
model-generated annotation != grounded Reference Truth
```

For broad investigations, material coverage is explicit: `covered | partial | unresolved | not_applicable | out_of_scope`.

## Reconstruction methods

`rore-reconstruction` JIT-loads only the methods that fit the current gap:

- surface / flow / state reconstruction;
- visual / interaction measurement;
- artifact extraction and nested container recovery;
- static code / binary reconstruction;
- runtime / dynamic observation;
- memory / state / reader-writer causality;
- web / JavaScript / API reconstruction;
- protocol reconstruction;
- data / schema / format reconstruction;
- mobile/platform reconstruction;
- conditional engine / asset / runtime profiling when those semantics exist;
- cross-version / differential reconstruction;
- mechanics / rules / balancing reconstruction;
- external/version/review research;
- controlled perturbation and causal probing.

A named tool is a **provider**, not an owner. RORE first identifies the required analysis capability, then discovers an available provider or uses the smallest auditable helper that can supply it.

## Perturbation as an epistemic instrument

RORE may deliberately vary inputs, state, memory, DOM/client state, files/configuration, timing, sequence or other authorized boundaries when normal observation cannot reveal the mechanism. The purpose is causal understanding, not exploit maximization.

```text
baseline
→ hypothesis
→ vary one material dimension
→ observe differential
→ trace cause
→ corroborate against stable anchors
→ restore / record residue
→ Evidence + Finding + Path
```

Stop when the mechanism is sufficiently understood for the requested reconstruction scope.

## Reference identities

Use stable IDs where the target contains the corresponding class, for example:

```text
SUR-###    surface/screen/view
FLOW-###   user/system flow
STATE-###  material state
COMP-###   component/subsystem
ENT-###    data/domain entity
PROTO-###  protocol/message identity
E-###      evidence
FIND-###   finding
PATH-###   user/call/data/runtime/causal path
PROBE-###  reproducible probe
```

Do not force unused classes onto a target. Stable IDs exist to preserve relationships across evidence and versions, not to impose a foreign architecture.

## Provenance

RORE evolves from CoreReplica and retains methodology provenance from the MIT-licensed `Jakeschincariol/replica-skill` and `zhaoxuya520/reverse-skill`. v0.4.0 re-reviewed the user-supplied source snapshots and deliberately admitted reverse-engineering methods while removing downstream clone/product ownership. See `SOURCE_PROVENANCE.md`.
