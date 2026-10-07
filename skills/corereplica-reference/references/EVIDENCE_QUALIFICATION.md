# Evidence Qualification

Load this reference only when Reference Truth depends materially on transformed/extracted inputs, parsing, heuristic identity resolution, large structured populations, layered sources, completeness claims, or claims of independent corroboration.

The goal is not more paperwork. The goal is to prevent a correct-looking derived artifact from silently becoming a stronger claim than its evidence supports.

## Core boundary

```text
source acquired
→ source/object identity established
→ structure/value interpreted
→ coverage established
→ claim qualified
```

Never skip a boundary by wording. `CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY`.

## Evidence kind and confidence

Use a compact evidence kind when it helps scope a claim:

- `DIRECT_RUNTIME`
- `DIRECT_STRUCTURED`
- `TARGETED_PARSE`
- `METADATA_OR_INDEX`
- `NAME_OR_LABEL_DERIVED`
- `THIRD_PARTY_DOCUMENTED`
- `MODEL_ASSISTED_HYPOTHESIS`
- `HEURISTIC`
- `HYPOTHESIS`

The names are descriptive, not a universal type system.

`evidence_kind` answers **what was actually observed**.  
`confidence` answers **how trustworthy that observation is inside that scope**.

High confidence never promotes a weaker evidence kind into a stronger boundary.


## Raw evidence vs normalized candidate views

Preserve raw/source-backed evidence unchanged enough to audit the original observation. Cleaning, normalization, symbol renaming, deduplication, type inference or LLM-assisted annotation belongs in a **derived** view with a source reference and transformation note.

Do not silently replace:

```text
raw observation
→ plausible cleaned value
```

and then cite the cleaned value as if it was directly observed. When normalization is useful, keep both lanes explicit.

## Model-assisted semantic annotations

Decompiler/LLM summaries, proposed names/types, source identification and algorithm labels are often high-value orientation aids. They are not raw program evidence. Treat them as `MODEL_ASSISTED_HYPOTHESIS` or another appropriately weak evidence kind until supported by cross-references, constants, callers/callees, runtime behavior, known signatures/source, or another independent boundary.

A model agreement with itself across two prompts is not independent corroboration.

## Object identity

When acquisition, extraction, conversion, importing or resolution can yield more than one plausible object, establish identity separately from parseability.

Material records should be able to answer, as applicable:

```text
requested identity
source identity
acquisition/transformation path
produced/output identity
identity evidence
source/output revision or hash
```

Rules:

- Parseable output is not identity proof.
- Identifier/name/reference occurrence is not ownership or identity proof.
- If multiple objects can legitimately reference the requested identifier, occurrence alone cannot resolve identity.
- `unique proven match → ACCEPT`
- `multiple plausible matches → UNRESOLVED`
- `no proven match → NOT_FOUND`

Do not promote a "best-looking candidate" merely to keep the pipeline moving.

## Coverage and completeness

Keep **value correctness** separate from **population completeness**.

When the population is material and knowable, record enough to make incompleteness visible:

```text
population_known
population_count
covered_count
missing_ids
unresolved_ids
duplicate_ids
coverage
explicit_exclusions
```

Do not use `complete`, `full`, `all` or equivalent language unless coverage plus explicit exclusions actually support it.

A correct 38/50 dataset is useful evidence; it is not a complete 50-record dataset.

## Derived-artifact lineage

For material derived datasets/artifacts, keep a reproducible chain:

```text
raw/reference source
→ acquisition/transformation
→ parser/interpreter/resolver
→ derived artifact
```

For consequential derived views, capture source revision/hash, tool/parser revision, coverage and known limitations when practical.

Derived views are disposable and reproducible. Raw/reference evidence remains the authority for what was observed.

## Parser safety

A parser encountering unknown or unexpected structure may:

- parse within established bounds;
- skip only when the next boundary is proven;
- stop and report unresolved.

It must not lose synchronization, continue through plausible-looking bytes, and emit them as valid evidence.

Material parser invariants include, as applicable:

- monotonic cursor/progress;
- bounded reads;
- established record/object boundary;
- range/count validation;
- identity validation;
- explicit unknown-type handling;
- explicit parse end;
- expected vs actual coverage.

A partially successful parser may support the records it actually proved. It must not be described as full-table verification if the remaining structure is unproven.

## Independent corroboration

Independent corroboration requires **materially independent failure modes**.

Two agents, scripts, files or tools are not independent merely because they are different implementations. Treat them as one evidence family when they share the same unresolved identity, guessed offsets/boundaries, source mapping, fixture, parser primitive, generated dataset or other material failure assumption.

Stronger patterns combine evidence that can fail differently, for example:

- targeted parse + independently established structured boundary;
- parsed configuration + matching runtime behavior;
- one source-layer interpretation + independently observed effective result.

Independence is methodological, not personal.

## Gate/verifier competence

A gate or parser claiming strong evidence should demonstrate that at least one representative relevant failure mode can make it fail.

Examples:

- local-only/VCS rule → a tracked forbidden fixture must fail;
- ambiguous resolver → multiple plausible matches must become `UNRESOLVED`;
- parser → malformed/unknown structure must stop or safely skip;
- completeness gate → missing members must prevent a `complete` claim.

A PASS cannot prove an invariant the gate does not test.

## Layered source precedence

When the same logical identity exists in multiple layers, establish effective precedence before merging evidence.

Examples include base+patch, local+remote config, CSS/inheritance, versioned APIs, feature flags, environment overrides, filesystem/package overlays, inherited definitions.

Do not assume `base wins`, `latest timestamp wins`, or `first found wins` without evidence. If effective precedence is unresolved, record `UNRESOLVED_SOURCE_PRECEDENCE`.

## Current-view reconciliation

When material evidence supersedes a current claim, update or explicitly supersede all current derived views that present that claim within the same work unit.

Historical logs may remain unchanged when clearly historical.

Do not leave one current authority saying `pending` while another current authority says `delivered` and expect file recency to resolve the contradiction.

## Keep it proportional

Do not turn this procedure into a provenance database, generic parser framework, mandatory manifest for every screenshot, license system, or second verification owner.

Ordinary visual/reference research keeps the lightweight path. Load and apply this qualification depth only when identity, transformation, parsing, completeness, layering or corroboration is materially at risk.
