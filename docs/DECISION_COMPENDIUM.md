# Decision Compendium

## Confirmed project decisions

### D-001 — Name
The project/plugin is named **CoreReplica**.

### D-002 — Source strategy
Use useful material from `Jakeschincariol/replica-skill` under its MIT license, but redesign governance instead of preserving the upstream mandatory pipeline.

### D-003 — Core-First integration
CoreReplica uses Core-First Governance as the preferred procedural owner when available. It does not copy the full Core-First method into a new architecture skill. Architecture/ownership/reuse materiality routes to `core-first-extension-architecture`; user/external runtime claims route to `observable-product-verification`; fresh architecture verification and Independent Review remain separate triggered layers.

### D-004 — APC boundary
Agent Project Compiler is an optional **downstream compiler**, not the owner of CoreReplica reference analysis. CoreReplica recovers and qualifies reference knowledge as `Evidence → Findings → Paths → Reference Model`; when APC is selected it consumes that corpus plus user intent and owns durable compilation of Product/Realization/System/Plan/Acceptance authorities. CoreReplica does not recreate an APC project package in parallel.

### D-005 — Truth separation
CoreReplica preserves the stronger operational split:

```text
Reference Truth
!= Product Truth
!= Implementation State
!= Verification Truth
!= Release Approval
```

Reference observations cannot silently become target requirements. Builder progress cannot prove parity/completion. Verification evidence cannot grant release approval.

### D-006 — Skill topology
CoreReplica v0.1 has eight coherent skills: orchestration, reference, product, design, build, verify, market and release. Backend/integration detail is a JIT reference under build rather than a separate owner. Test and parity are combined under a read-only verification owner. Entrepreneur/brand/launch are combined under a market owner with JIT subprocedures.

### D-007 — Routing model
There is no mandatory linear sequence. `corereplica-orchestration` routes by material trigger. Skills may be used independently when their prerequisites/authorities exist.

### D-008 — Architecture ownership
CoreReplica never creates `architecture.md` as a competing project authority merely because a reference reconstruction is underway. In an existing project/workspace it consumes current architecture/project authorities first. In Greenfield work, Core-First/APC owner decomposition establishes the architecture before implementation.

### D-009 — Verification independence
`corereplica-verify` is read-only with respect to product implementation by default. It records reproducible findings/evidence and hands corrections back to the relevant canonical implementation owner. It does not fix the bug it just judged.

### D-010 — Parity contract
Parity is derived from target requirements plus verification evidence. It never trusts an implementation agent's `done/yes` field as acceptance. Layout/image diff remains heuristic evidence and cannot prove interaction, persistence or release readiness.

### D-011 — Brand/design boundary
Design owns semantic design-system roles/contracts. Market/brand owns brand identity/profile values and positioning. Brand may supply inputs consumed by the design/build path; it does not directly become a second design-system owner.

### D-012 — Release boundary
Release preparation may proceed as far as reversible preparation allows. Publish/deploy/charge/store-submit or another defined consequential state transition remains gated by explicit user/project approval. Broad implementation intent is not approval.

### D-013 — Portability
The canonical plugin uses Agent Plugins 1.0 with standard `skills/` layout. Provider-specific capabilities are optional adapters. CoreReplica remains functional with explicit project-native fallback rules when Core-First or advanced host features are unavailable.

### D-014 — Source/use stages
Authorization to access/analyze/transform reference material, retain it locally, place/share it through project/VCS channels, include it in a target product, and redistribute it are separate decisions. Material type alone does not decide the answer.

### D-015 — Reference Evidence Qualification
Reference claims may not exceed their proven evidence boundary. Object identity, parser correctness, coverage, source-layer precedence and methodological independence remain explicit; ambiguity fails closed where a stronger claim would otherwise be fabricated.

### D-016 — Reverse-engineering mission
`corereplica-reference` is not a surface-only recon step. For broad authorized reconstruction it actively inventories, extracts/unpacks/decodes/decompiles, performs static and dynamic/runtime analysis, connects Evidence into Findings and Paths, and synthesizes a usable Reference Model. Evidence sufficiency for one claim is not by itself a stop condition when broader recovery was requested.

### D-017 — Reverse-skill admission
CoreReplica admits selected provider-neutral method ideas from `zhaoxuya520/reverse-skill` (MIT): target triage, actual tool discovery, static↔dynamic iteration, hypothesis-driven replanning, Evidence→Finding→Path synthesis, and the adversarial reasoning used to reveal broken assumptions, control gaps, state drift and parser/layer differentials. It does not import the upstream pentest/exploit/CTF routing stack or make security tooling a CoreReplica owner.

### D-018 — Adversarial limit probing
Controlled adversarial/limit testing is an analysis method owned by `CR_REFERENCE`, not a new security owner. CoreReplica may challenge value/shape boundaries, sequence/replay, timing/concurrency, parser/normalization, layer/source, recovery and authority assumptions to learn hidden contracts and failure semantics. The stop condition is sufficient mechanism understanding, not maximum exploit impact. A discovered bug or quirk remains Reference Truth until Product Truth explicitly decides whether to adopt, adapt, reject or treat it as inspiration-only.

### D-019 — External research and target corroboration
Public Internet sources are a first-class discovery/corroboration input under `CR_REFERENCE`, not a new research owner. Version-aware first-party docs/source/specs/history, independent research and community reports may reveal mechanisms, source locations and hypotheses. Target-specific claims remain externally documented until corroborated against the target when material; offline agents emit research packets rather than inventing missing public knowledge.

### D-020 — Analysis identity, fan-out and comparative anchors
Reverse-engineering state is bound to the strongest practical target identity (hash/build/revision/environment). Cross-version work re-resolves semantic identities instead of transplanting raw offsets. Broad mechanism claims map materially relevant enforcement sites/layers, and decompiler/LLM annotations remain reversible derived hypotheses until grounded. Extraction uses format-first dispatch with bounded recursive/fallback recovery when useful.

### D-021 — Claim-sensitive runtime corroboration
Launching the reference target is not a ritual requirement. Static/package/structured claims may remain static when that boundary fully proves them. Material claims about effective loading/use, generated state, temporal behavior, persistence, live entities/processes, user interaction, recovery or other runtime-only semantics require a representative authorized runtime attempt when practical before they are described as runtime-verified or the relevant reconstruction slice is called complete. If runtime is unavailable, the boundary remains explicit (`RUNTIME_UNCHECKED | RUNTIME_PARTIAL | RUNTIME_BLOCKED`).

### D-022 — Reconstruction coverage and replica-trait continuity
The broader v0.3 reverse-engineering corpus does not replace the earlier explicit Reference→Product handoff. Broad reconstruction challenges material knowledge classes for covered/partial/unresolved/not-applicable/out-of-scope status, and direct replica work emits compact candidate traits grounded in Evidence/Findings/Paths, including runtime status and limitations when material. Product Truth still owns `adopt | adapt | reject | inspiration-only`.

