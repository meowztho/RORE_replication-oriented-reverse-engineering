# External Research and Corroboration

Load this JIT reference when local evidence leaves an important technology, format, identifier, version behavior, implementation pattern, public contract or source location unresolved, or when public knowledge could materially improve the next reverse-engineering step.

External research is a **discovery and corroboration lane** inside `CR_REFERENCE`. It is not a substitute for target-local evidence when the claim is specifically about the target under analysis, and it is not a second APC/research owner.

## Core loop

```text
local evidence / unresolved question
→ focused external research
→ source + claim + version/scope extraction
→ hypothesis / source-discovery update
→ target-local corroboration when the claim is target-specific
→ Evidence → Finding → Path → Reference Model
```

Public research may reveal what to inspect next, which tool/format/engine mechanism matters, what older version semantics were, or which hidden local artifact is likely to exist. It does not gain extra authority merely because it is published.

## Source classes

Prefer the strongest source that directly addresses the active question. Useful classes include:

- first-party product/engine/framework documentation and source;
- standards, protocol/file-format/API specifications;
- official SDKs, headers, symbols, release notes, changelogs and issue trackers;
- developer talks, technical blogs and archived version-matched documentation;
- public source repositories and commit history;
- credible independent reverse-engineering/modding research;
- community forums, wikis, Reddit/social discussions as discovery/hypothesis sources.

Do not collapse these into a universal ranking. Source authority is relative to the claim: a version-matched implementation source may beat current generic documentation, while a community report may be valuable for discovering an edge case that still requires corroboration.

## Claim scope and target corroboration

For material external claims, preserve enough to answer:

```text
source_id
source_type
title / publisher / author
URL or stable reference
published/revision date
version/build applicability
claim supported
claim scope: general mechanism | version behavior | target-specific | tool/format guidance | discovery hint
target corroboration: CONFIRMED | PARTIAL | UNCHECKED | CONTRADICTED | NOT_APPLICABLE
accessed_at
notes / limitations
```

A useful semantic ladder is:

```text
DISCOVERY_HINT
→ EXTERNAL_DOCUMENTED
→ TARGET_CORROBORATED
```

The first two may guide analysis. Only the last supports a target-specific claim at the corroborated boundary unless the user explicitly asked only what the external source says.

## Research questions, not broad browsing

Search from a concrete unknown whenever possible:

```text
unknown identifier / format / engine behavior / API / field / call pattern
+ observed target version/platform/context
+ exact discriminator needed
```

Prefer focused queries that can change the next local action. Avoid broad browsing that does not improve the hypothesis set, source inventory or target model.

## Internet research as source discovery

External research may reveal new local evidence classes. Examples:

- documentation says the engine uses a specific registry/index file → inspect that file locally;
- a file-format reference identifies nested container types → extend inventory/extraction;
- a public symbol/header reveals semantic names → re-anchor local call/data analysis;
- a modding report identifies a likely layer/override path → test the precedence locally;
- release notes identify a version boundary → compare the target build against both sides.

Treat the public source as the reason to inspect; record the resulting local observation separately.

## Version and time discipline

Current documentation does not automatically describe an older target. Preserve version/build applicability and observation/publication dates when material.

When sources disagree, test likely causes before choosing one:

- version/build drift;
- platform differences;
- base vs patch/override layer;
- documentation describing intended rather than effective behavior;
- community report being incomplete or wrong;
- target-local customization.

If the disagreement cannot be resolved, keep it explicit.

## Research without web capability

A local/offline agent must not invent missing public knowledge. Instead produce a compact research packet such as:

```text
question
why it matters
known local evidence
target version/platform/build
useful search terms / candidate source classes
what result would discriminate the hypotheses
```

A web-capable agent/user can return sources to the same `CR_REFERENCE` lane. This preserves provider neutrality: Internet access is a capability, not a requirement for CoreReplica to function.

## Raw vs normalized external evidence

Preserve exact source-backed facts separately from normalized interpretation. Do not silently clean malformed identifiers, values or excerpts into a stronger claim. A normalized candidate view may be useful, but it must remain derived and linked to the raw/source record.

## Stop condition

Stop external research when it no longer changes the source inventory, hypothesis set, local analysis route or confidence boundary. Return to target-local analysis rather than browsing for reassurance.
