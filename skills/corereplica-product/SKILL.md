---
name: corereplica-product
description: Define the independent target product from user intent plus reference observations. Use when deciding which reference traits to adopt, adapt, reject, or treat as inspiration; when setting scope/priorities; or before implementing a reference-derived feature whose target intent is not explicit. Do not infer product scope from the reference alone and do not store implementation or verification status in requirements.
---

# CoreReplica Product Definition

Own **target Product Truth** for the CoreReplica-specific fallback artifacts. In a compiled/mature project, update the project's existing product authorities instead of creating duplicates.

## Inputs

- user's goal, audience, constraints and differentiators;
- `corereplica-reference` observations when relevant;
- existing project product authorities;
- current market/review evidence when the user wants it to influence scope.

## Output

Fallback artifacts:

```text
corereplica/product/PRODUCT_SCOPE.md
corereplica/product/REQUIREMENTS.csv
```

`REQUIREMENTS.csv` schema:

```text
id,area,requirement,priority,source_decision,reference_ids,acceptance,notes
```

No `done`, `clone`, `verified`, or builder-owned completion field is allowed.

## Procedure

1. Preserve the user's master outcome and intended audience before decomposing features.
2. For each material reference trait, resolve one of:
   - `adopt` — same user outcome/behavior is intentionally required;
   - `adapt` — keep the useful idea but change semantics/flow/constraints;
   - `reject` — explicitly not part of the target product;
   - `inspiration-only` — useful context, not a requirement.
3. Add target requirements that do not exist in the reference when they are part of the user's distinct value proposition.
4. Preserve explicit exclusions/deferred scope. Do not let a reference application's breadth silently expand the project.
5. Classify priorities only after target intent exists. `must | should | could` are product priorities, not evidence states.
6. Give each requirement a stable ID and outcome-oriented acceptance statement. Do not prescribe a class/file/provider unless that is itself a confirmed constraint.
7. If a decision changes user-visible behavior, scope, cost, trust, business model, or a consequential product tradeoff and the user has not settled it, ask. Reversible implementation details remain technical decisions.
8. When requirements imply architecture/ownership/reuse decisions, route to Core-First before implementation; do not create a parallel `architecture.md` here.

## Distinct-product challenge

Before freezing scope, ask whether the target product is merely reproducing a reference or has a coherent independent reason to exist. This is a challenge, not a requirement to invent novelty. Preserve the user's chosen answer.

Useful dimensions:

- target audience/niche;
- workflow simplification;
- pricing/business-model difference;
- privacy/local/offline posture;
- integrations;
- accessibility;
- missing reference capability;
- intentionally smaller scope.

## Handoff

Return explicit adopted/adapted/rejected traits, target-only requirements, deferred/out-of-scope items and unresolved user decisions. Implementation uses these authorities; it may not rewrite them to match what was easiest to build.
