---
name: corereplica-orchestration
description: Route reference-driven product work with Core-First discipline and minimal context. Use when the user wants to study/rebuild/replace a reference app, continue a CoreReplica project, or when it is unclear which CoreReplica capability owns the next step. Do not force a fixed pipeline; route only material reference, product, design, implementation, verification, market, or release procedures.
---

# CoreReplica Orchestration

The primary agent is the integrator. CoreReplica is a routing and procedure family, not a second project architecture or acceptance engine.

## Kernel

Always preserve:

1. `REFERENCE TRUTH != PRODUCT TRUTH != IMPLEMENTATION STATE != VERIFICATION TRUTH != RELEASE APPROVAL`.
2. Current workspace/project authorities and runtime evidence outrank remembered chat, skill memory, old plans, and stale status. A Git repository is only one possible workspace shape.
3. If architecture, ownership, authoritative state, reuse, capability/module/provider boundaries, producer convergence, extension semantics, or architecture repair are material, load/apply `core-first-extension-architecture` in the primary context when available before freezing the change boundary. Core-First is a preferred companion, not a hard runtime dependency: when unavailable, use current project authorities plus the compact standalone owner-safety fallback in `references/WORKSPACE_AND_STANDALONE.md`; unresolved ownership stays explicit.
4. Real user/external runtime claims require real outcome evidence; use `observable-product-verification` when available. Tool/log/build success does not substitute for an observable outcome.
5. Reference observations never become requirements without an explicit target-product decision.
6. Builder progress never proves acceptance or parity.
7. Verification records evidence/findings before correction; a verifier does not silently fix what it is judging.
8. Approval/admission gates block the exact consequential transition, not authorized reversible preparation. Broad implementation intent does not imply approval.

## JIT routing capsule

| Material trigger | Owner |
| --- | --- |
| what the reference product does; screens/flows/components/data clues/sources | `corereplica-reference` |
| what the new product should adopt/adapt/reject/add; scope/priorities | `corereplica-product` |
| visual hierarchy, design tokens, component semantics, reference visual translation | `corereplica-design` |
| source implementation, integration, backend/auth/data/payments/jobs/providers | `corereplica-build` + Core-First when architecture is material |
| QA, runtime evidence, bugs, parity, screenshot comparison, acceptance evidence | `corereplica-verify` + Observable Product Verification when applicable |
| review research, complaints, positioning, branding, pricing, landing/store content | `corereplica-market` |
| release preflight, production preparation, publish/deploy/store-submit | `corereplica-release` |

Do not preload all siblings. Sequence the minimum owner set when a request crosses boundaries.

## Operating sequence

1. Classify the active workspace shape before assuming repository semantics: source repository, binary/distribution package, installed application, artifact bundle, or mixed workspace. Establish the control-plane/project root separately from the runnable/shippable target root when material. If the target already has canonical product/system/acceptance artifacts, use them instead of creating duplicate CoreReplica truth.
2. Classify the request by responsibility, not by the upstream Replica step number.
3. Before reference-derived implementation, ensure the relevant observation has an explicit target-product decision. If not, route to `corereplica-product`.
4. Before architecture-relevant implementation, resolve the canonical owner/change class through Core-First or project-native equivalent.
5. Keep implementation progress in `corereplica/implementation/` or the project's existing tracker. If writing metadata inside the runnable/shippable target would contaminate it, place CoreReplica control artifacts in an adjacent non-shipping control-plane directory instead. Never write `verified` from the build lane.
6. Route real outcome claims to verification. Route findings back to the canonical implementation owner, then re-run verification on the changed revision.
7. For release work, perform reversible preparation, report the exact remaining gate, and cross it only with explicit current authorization.

## Local short path

Direct local work is acceptable when the target owner/edit location and intended semantics are already clear; no material product-scope, architecture, producer/persistence, verification, authority, dependency, or gate decision remains; shared behavior/authoritative transitions stay unchanged; and a bounded check can prove the claim. File count or apparent difficulty does not decide materiality.

## Context recovery

After context loss/compaction/workspace switch/material state change:

- discover current workspace/project state first; do not invent Git revisions for non-Git targets;
- read the smallest current authority set needed for the next decision;
- do not reconstruct product truth from reference files or implementation code;
- do not hydrate every CoreReplica skill for reassurance;
- reconcile open outcomes, evidence, blockers and the next admissible action before continuing.

## JIT references

Read only when material:

- `references/ARTIFACT_AUTHORITY_MODEL.md` — truth layers, target-project artifact routing, existing-project coexistence;
- `references/CLEAN_ROOM_POLICY.md` — allowed reference sources and prohibited copying/bypass behavior;
- `references/ROUTING_AND_CONTEXT.md` — cross-skill sequencing, context loss and Core-First/OPV binding;
- `references/WORKSPACE_AND_STANDALONE.md` — non-repository targets, control-plane placement, companion/standalone modes and revision identity;
- `references/RELEASE_AND_CORRECTION.md` — finding handoff, re-verification and exact release gate semantics.
