---
name: corereplica-reference
description: Study a reference product clean-room style and produce sourced observations about screens, flows, components, states, data clues, and constraints. Use when the user asks how a reference app works, wants to map/rebuild a slice, supplies screenshots or a product URL, or when target decisions depend on reference evidence. Do not turn observations into target requirements or implementation status.
---

# CoreReplica Reference Analysis

Own **Reference Truth only**. This skill describes what can be supported about the reference product from allowed evidence. It does not decide what the user's product should include.

Read the CoreReplica clean-room policy JIT from `corereplica-orchestration` when source boundaries are material.

## Inputs

Use the smallest sufficient set of:

- public help/docs/pricing/changelog/store pages;
- public walkthroughs/reviews;
- user-supplied screenshots/recordings;
- the user's own authorized account used normally;
- public API documentation where it reveals public semantic contracts.

Research current facts when the claim can drift. Preserve the URL/source and observation date when material.

## Outputs

Prefer existing project authorities if they already own reference research. Otherwise create:

```text
corereplica/reference/REFERENCE_MODEL.md
corereplica/reference/FEATURE_OBSERVATIONS.csv
corereplica/reference/SOURCE_LOG.md
corereplica/reference/screens/        # reference-only, never shipped
```

`FEATURE_OBSERVATIONS.csv` schema:

```text
id,area,observation,evidence_ids,confidence,notes
```

It deliberately contains no target priority and no implementation/completion field.

## Procedure

1. Establish the requested reference product, platform/surface, and product slice. If the user asks for an impossibly broad whole product, propose a bounded slice based on their stated goal rather than silently studying everything.
2. Build the source log before making broad claims. Distinguish first-party, public third-party walkthrough/review, and user-provided evidence.
3. Inventory materially relevant screens/surfaces with stable IDs, entry path, purpose, states observed and evidence IDs.
4. Trace user goals as flows with stable IDs and observed/unknown edges. Preserve error/empty/loading/permission/mobile states when visible or materially documented.
5. Record repeated component/interaction patterns as reference observations, not target design requirements.
6. Infer entities/relationships only when useful. Attach evidence and confidence (`high | medium | low`). Do not present an inference as an observed schema.
7. Record capabilities/features as observations with evidence IDs. Mark unavailable/licensed/network/content constraints explicitly.
8. Record unknowns instead of filling them from genre expectations.

## Reference trait extraction

At the end, provide a compact trait list suitable for `corereplica-product`:

```text
trait id
observed behavior/pattern
source/evidence
confidence
copy/content/licensing constraint if any
```

Do not label a trait `must/should/could` here. The target product owner decides whether to adopt, adapt, reject or use it only as inspiration.

## Evidence discipline

- A screenshot proves visible state, not hidden interaction or persistence.
- A help article proves documented behavior, not necessarily the current runtime implementation.
- A public price page proves the displayed price at the observed date, not a timeless price.
- A user's own account interaction proves only the exercised path/state.
- Missing evidence remains unknown.

## Handoff

Return the reference observations plus unresolved unknowns. If the user is deciding what to build, route next to `corereplica-product`. If they asked only for reference research, stop there.
