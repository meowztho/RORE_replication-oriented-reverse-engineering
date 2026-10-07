# Evidence Review Checklist

Use proportionally; a narrow claim does not require a whole-product audit.

## Reviewer independence
- fresh reviewer context used where feasible?
- evidence graph/reference authorities available without reconstruction-agent confidence or persuasive rationale?
- prior review conclusion withheld before independent derivation where feasible?

## Identity / fixity
- target/build/revision/environment identified?
- raw artifact hash recorded where material?
- hash/fixity still valid?
- derived view tied to the same target identity?

## Evidence graph
- every material Finding has Evidence?
- every Path edge has Evidence/Finding support?
- unlinked Evidence intentionally retained or accidentally ignored?
- raw vs normalized vs derived views distinct?

## Claim boundary
- static claim presented as static?
- runtime-sensitive claim has appropriate runtime evidence or explicit limitation?
- memory-local values not promoted into cross-version truth?
- model-assisted annotation still marked derived until grounded?

## Qualification
- correct object/layer/version identity?
- parser/transformation semantics validated?
- completeness denominator known or limitation stated?
- corroborating sources materially independent?

## Analysis quality
- negative evidence preserved?
- contradictory evidence visible?
- rejected hypotheses resurrected?
- deadlock/tool bias hidden behind repeated similar evidence?
- cross-version semantic anchors re-established?

## Fidelity
- reference's own awkward/legacy/duplicated structure preserved when evidenced?
- any unexplained normalization, design translation or target-product language introduced?

## Coverage
For broad claims, inspect material classes for `covered | partial | unresolved | not_applicable | out_of_scope` and challenge any silent gap.
