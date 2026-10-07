# CoreReplica Context Handoff — v0.3.3

## Current identity

CoreReplica is a skills-only plugin whose primary responsibility is **authorized reference reverse engineering and reconstruction**, with optional direct independent replication. It is not a second Agent Project Compiler.

## Canonical boundary

```text
CoreReplica
  target survey/inventory
  extraction/unpacking/decoding/decompilation
  static analysis + targeted runtime corroboration for runtime-sensitive claims
  controlled adversarial/limit probing
  external research / source discovery / target corroboration
  evidence qualification
  Evidence → Findings → Paths → Reference Model

APC (only when selected)
  user intent + CoreReplica corpus
  → durable Product/Realization/System/Plan/Acceptance project authorities
```

## v0.2 empirical baseline

ANote and OMD3-oriented field work exposed non-repo workspaces, side effects, non-visual outcomes, source-use/retention distinctions, object-identity failures, parser desynchronization, incomplete coverage, false independence, layered-source precedence, stale derived views and gate-competence gaps. v0.2.0–v0.2.2 hardened these boundaries.

## v0.3.0–v0.3.1

`CR_REFERENCE` became an active reverse-engineering/reference-recovery owner rather than a surface documentation lane. It may inventory, extract/unpack/decode/decompile, statically analyse, dynamically observe and correlate evidence. v0.3.1 added adversarial limit probing to learn hidden contracts from controlled boundary, state, timing, parser/layer and recovery differentials without creating a pentest/exploit owner.

## v0.3.2

A broader source review added six bounded improvements:

1. **External research/corroboration JIT** — public docs/source/history/research may discover mechanisms, formats and new local evidence sources; target-specific claims remain distinct until target corroboration is sufficient. Offline agents emit research packets.
2. **Format-first bounded extraction** — identify before dispatch where practical, try alternate compatible extractors/parsers after meaningful failures, recurse nested containers with lineage/resource bounds, and validate output semantics rather than exit code alone.
3. **Artifact-bound analysis state** — bind sessions/derived views to hash/build/revision/environment; changed artifacts require explicit cross-version correlation.
4. **Decompiler-neutral semantic layer** — callers/callees/xrefs/types/strings/annotations are semantic queries across tool providers; LLM names/summaries/source guesses remain reversible hypotheses until grounded.
5. **Enforcement-site fan-out coverage** — a broad mechanism/restriction may exist across several call sites/layers; one found check is not full coverage.
6. **Cross-version semantic anchors** — compare builds with behavior/pattern/schema/call-flow anchors and re-resolve identities instead of blindly carrying absolute offsets.

Raw evidence remains separate from normalized/cleaned candidate views.

## v0.3.3

A version-lineage audit across v0.2.0–v0.3.2 plus the ANote-vs-OMD3 runtime contrast added two bounded corrections:

1. **Claim-sensitive runtime corroboration** — starting every target is not mandatory, but material claims about effective runtime behavior must be exercised on a representative authorized real path when practical or remain explicitly runtime-unchecked/partial/blocked. Static/package presence is separated from `PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE`.
2. **Coverage/trait continuity** — the explicit v0.2 `Reference trait extraction` handoff is restored as a first-class contract, and broad reconstruction challenges material knowledge classes so richer RE procedures do not compress away UI/flow, install/update, runtime, failure, timing or trust-boundary knowledge.

The lineage comparison found no other unintended file loss: v0.2.1→v0.3.2 is additive, while v0.2.0's `CLEAN_ROOM_POLICY.md` was intentionally replaced by the canonical source/use/distribution policy.

## Next empirical work

Use the OMD3 reference project or another rich target to test whether a fresh agent:

1. uses external research only when it can change the next analysis action and returns to the local target for corroboration;
2. discovers nested/exotic containers through format-first fallback extraction instead of treating one failed extractor as absence;
3. invalidates stale derived state when the target hash/build changes;
4. maps distributed enforcement sites before claiming a mechanism is complete;
5. ports findings across versions through semantic anchors rather than offsets;
6. keeps LLM/decompiler annotations and normalized candidates distinct from raw evidence;
7. identifies runtime-sensitive claims, performs targeted real runs when practical, and labels static-only runtime gaps honestly;
8. distinguishes present/referenced content from reachable/exercised/effective runtime content;
9. preserves the compact reference-trait handoff into Product Truth;
10. hands the qualified corpus to APC without creating duplicate System/Plan/Acceptance authorities.

Behavioral success is not implied merely by static package tests.
