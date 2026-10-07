# RORE Decision Compendium

## D-001 — Product identity
The user-facing plugin is **RORE — Replication-Oriented Reverse Engineering**. The backend manifest name remains `corereplica` in v0.4.x solely to preserve the existing private plugin identity and release lineage.

## D-002 — Scope boundary
RORE owns reference reverse engineering and reconstruction only. It stops at qualified Reference Truth and does not own downstream target-product decisions, project compilation, target architecture, implementation, replica acceptance, branding, launch or release.

## D-003 — Reference-native reconstruction
The reference is allowed to reveal its own architecture, logic, state model, data model, protocols, flows, timing and failure behavior. RORE preserves those structures and uncertainties rather than converting them into a cleaner or implementation-oriented target design.

## D-004 — Owner topology
RORE has three durable responsibilities: orchestration, reconstruction and read-only evidence review. Surface, static, runtime, memory, protocol, web, mobile, engine/asset and other analysis modes or conditional profiles are JIT methods beneath reconstruction unless future evidence proves a distinct canonical responsibility.

## D-005 — Evidence discipline
`CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY`. Object identity, parser correctness, source precedence, population coverage, methodological independence, target identity and runtime status remain explicit where material.

## D-006 — Analysis decision quality
RORE admits hypothesis-driven stage exits, negative evidence, deadlock→replan, stage/tool-bias detection, runtime back-annotation and context-pollution detection from the reviewed reverse-skill methodology. These improve epistemic quality and do not create a security-product owner.

## D-007 — Perturbation and causal probing
Controlled mutation, boundary tests, replay/sequence variation, timing/concurrency probes, failure/recovery injection, DOM/client-state changes, memory edits and similar authorized interventions are valid when they materially expose mechanism or causality. Their purpose is understanding, not exploit maximization.

## D-008 — Provider-neutral tooling
RORE routes `question → required evidence boundary → analysis capability → provider`. IDA, Ghidra, Binary Ninja, radare2, x64dbg, Frida, browser/CDP tools, packet analyzers and helper scripts are providers, not responsibility owners.

## D-009 — Stable reference identities
When useful, stable reference IDs such as `SUR`, `FLOW`, `STATE`, `COMP`, `ENT`, `PROTO`, `E`, `FIND`, `PATH` and `PROBE` preserve cross-artifact relationships. They are not a mandatory schema imposed on every target.

## D-010 — Cross-version semantics
Cross-version work re-resolves semantic anchors — call relationships, strings, constants, types, schemas, patterns, behavior and data references — rather than transplanting raw addresses or offsets.

## D-011 — LLM/decompiler annotations
Function names, summaries, source-identification guesses and other model-assisted annotations are reversible derived hypotheses until grounded by target evidence.

## D-012 — External research
Public docs, source/history, reviews, changelogs, community reports and research can discover mechanisms and new local evidence paths. Target-specific claims remain externally documented until target corroboration is sufficient for the claimed boundary.

## D-013 — Upstream replica-skill admission
RORE retains useful recon ideas from `Jakeschincariol/replica-skill`: stable screen/flow identities, state inventories, component mapping, inferred data models with evidence/confidence, measured visual semantics and systematic edge-state thinking. Clone priorities, sizing, target architecture/design/build and ship/parity semantics are not admitted.

## D-014 — Upstream reverse-skill admission
RORE retains provider-neutral reverse-engineering methods from `zhaoxuya520/reverse-skill`, including protocol/mobile/web/binary-diff patterns, Evidence→Finding→Path, analysis-decision quality and selected adversarial/pwn/patch-diff reasoning where it serves mechanism discovery. Offensive impact, persistence, lateral movement, credential theft and exploit stabilization are not RORE goals.

## D-015 — Evidence review boundary
Evidence Review audits an existing reconstruction package read-only. It may report unsupported claims, stale hashes, contradictions, unlinked evidence or overclaimed coverage, but the correction is performed later by Reconstruction so the reviewer does not silently repair its own judgment target.

## D-016 — Domain neutrality
RORE is domain-neutral. Product categories such as web, API, ERP, CRM, desktop, mobile, protocol, game or simulation do not become responsibility owners and none is a primary target. Domain/surface labels may select conditional JIT profiles, but routing remains `knowledge gap → evidence boundary → analysis method/capability → provider`. Games are retained as a useful high-complexity stress-test domain, not as a privileged architecture focus.
