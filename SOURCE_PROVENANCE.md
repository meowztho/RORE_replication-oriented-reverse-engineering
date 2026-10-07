# Source provenance

CoreReplica v0.3.3 is derived from and informed by reviewed sources:

- Repository: `https://github.com/Jakeschincariol/replica-skill`
- Upstream commit: `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`
- Upstream release description: Replica skill pack v1.0, eleven Claude skills
- Upstream license: MIT

## Reused/adapted code

The following deterministic helper families originate from the upstream project and retain MIT provenance:

- `replica-design/contrast.py` → `skills/corereplica-design/scripts/contrast.py`
- `replica-diff/imgdiff.py` → `skills/corereplica-verify/scripts/imgdiff.py`
- `replica-diff/parity.py` → concept retained but implementation contract rewritten for evidence-separated parity
- `replica-entrepreneur/reviews.py` → `skills/corereplica-market/scripts/reviews.py`
- `replica-brand/sweep.py` → `skills/corereplica-market/scripts/sweep.py` with CoreReplica planning-folder handling
- `replica-launch/listing.py` → `skills/corereplica-market/scripts/listing.py`

Templates/themes derived from upstream examples retain the same provenance.

## Architectural rewrite

CoreReplica does not preserve the upstream mandatory chain `recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy` as governance.

The rewrite adds material-triggered JIT routing, explicit Reference/Product/Implementation/Verification/Release boundaries, Core-First owner routing instead of a parallel architecture skill, read-only verification, and exact consequential release gates.

## v0.1.1 pre-test hardening

No new upstream source was incorporated. v0.1.1 restores useful procedural depth from the already-attributed Replica v1.0 source as JIT references while preserving CoreReplica ownership boundaries.

## v0.2.0 field-evaluation hardening

v0.2.0 is driven by the staged ANotePortable evaluation supplied by the project user. No third-party source code was incorporated for these corrections.

## v0.2.1 source/use-policy normalization

v0.2.1 replaces blanket source/asset/binary-copy prohibitions with one provider-neutral rule: authorization to access/analyze/transform material is distinct from authorization to retain/share, include or redistribute it.

## v0.2.2 reference-evidence qualification

v0.2.2 is driven by a user-supplied domain-neutral review of a game-reference extraction/replication workflow. No game code, assets, parser code or Universal Modder implementation is copied into CoreReplica. The release generalizes the empirical failure classes into procedural rules for claim strength, object identity, coverage, lineage, parser safety, independent failure modes, source-layer precedence, gate competence, retention/VCS boundaries and current-view reconciliation.

## v0.3.0 reverse-engineering/reference-recovery expansion

Reviewed source:

- Repository: `https://github.com/zhaoxuya520/reverse-skill`
- Reviewed main commit: `cab634bd855fc287f6e420c1f36fd1a6b9245960`
- License: MIT

CoreReplica adapts provider-neutral method concepts rather than the upstream security product topology: target triage, actual tool discovery, staged-but-iterative static/dynamic analysis, hypothesis-driven replanning, Evidence→Finding→Path synthesis, plus controlled adversarial reasoning around broken assumptions, control gaps, state drift, parser/layer differentials and failure/recovery behavior. CoreReplica does **not** import reverse-skill's pentest/exploit/CTF routing stack, payload catalog, offensive-operation modules, tool bootstrap stack, or routing database as product ownership.

The new `REVERSE_ENGINEERING_WORKFLOW.md` is a CoreReplica-specific rewrite aligned to reference reconstruction and APC handoff boundaries; no reverse-skill executable code is copied.

## v0.3.1 adversarial-limit reasoning

The uploaded `reverse-skill-main.zip` was additionally reviewed for domain-neutral reasoning embedded in pentest/CTF/pwn methodology. CoreReplica admits only the analysis patterns needed to understand a reference system: assumption/control-gap mapping, one-variable differential probing, state-machine sequence/replay tests, bounded concurrency for state-drift semantics, parser/normalization differential reasoning, failure/recovery probing, and primitive decomposition. Payload/exploit-chain instructions are not copied.

## v0.3.2 external-research and comparative-RE review

Additional public sources were reviewed for domain-neutral method ideas; no executable code or proprietary content from these sources is copied into CoreReplica:

- J.W. McKiddy, `Using AI Skills for Reverse Engineering` and `Codex vs. Claude: Which One Handles RE Skills Better?` — artifact-first playbooks, preflight/tool reality, raw-vs-normalized evidence separation, controlled execution boundaries and cross-provider workflow observations.
- J. Scott Christianson, `Using AI for Reverse Engineering` — public web research as a pre-compilation discovery input, reinforcing the CoreReplica→APC boundary.
- `mahaloz/DAILA` (BSD-3-Clause) and the NDSS 2026 `Decompiling the Synergy` study — decompiler-neutral AI interaction, function summarization/renaming/source-identification as analyst aids, and empirical evidence that LLM assistance also produces hallucinations/unhelpful suggestions; CoreReplica therefore treats model annotations as derived hypotheses. No DAILA code is copied.
- `Bioruebe/UniExtract2` (GPLv2) — conceptual inspiration for format-first detection, multiple extractor backends and broad/nested extraction coverage. No UniExtract2 code is copied, avoiding GPL code incorporation.
- `louisgthier/decompai` (custom MIT-style license with attribution requirement) — conceptual inspiration for hash-keyed persistent analysis workspaces and isolated short-lived tool runners. No DecompAI code is copied or modified.
- Public `InfinityUnlocked` / Reddit reverse-engineering case — empirical example that one product rule may be enforced at many call sites/layers and that cross-version ports should re-discover semantic patterns rather than reuse offsets blindly. No game/mod code is copied.
- MCPMarket and CoddyKit summaries were reviewed as secondary sources but did not add unique methodology beyond the primary repositories/material already reviewed.

The admitted changes remain under existing `CR_REFERENCE` ownership: external research/corroboration, format-first bounded fallback extraction, artifact-bound analysis identity, tool-neutral decompiler semantics, enforcement-site coverage and cross-version comparative anchors.

## v0.3.3 runtime corroboration and lineage-retention audit

v0.3.3 is driven by an empirical comparison between two user-observed field cases: ANotePortable exercised the real application and exposed process/filesystem/registry/recovery contracts, while the OMD3 extraction/reconstruction run had not visibly launched the game. The correction is domain-neutral: runtime is not mandatory for every claim, but material effective-runtime claims require representative corroboration when practical or an explicit runtime-unchecked/partial/blocked boundary.

A direct archive comparison of CoreReplica v0.2.0, v0.2.1, v0.2.2, v0.3.0, v0.3.1 and v0.3.2 was also performed to detect accidental semantic compression. No unintended file removal was found after v0.2.1. The only v0.2.0-only file was the intentionally superseded `CLEAN_ROOM_POLICY.md`. One semantic contract had become too implicit during the v0.3 reference expansion: v0.2.x's explicit `Reference trait extraction` handoff. v0.3.3 restores that handoff and adds a proportional broad-reconstruction coverage challenge without adding a new owner or mandatory pipeline.

No new third-party source code is incorporated in v0.3.3.
