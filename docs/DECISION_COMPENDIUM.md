# Decision Compendium

## Confirmed project decisions

### D-001 — Name
The project/plugin is named **CoreReplica**.

### D-002 — Source strategy
Use useful material from `Jakeschincariol/replica-skill` under its MIT license, but redesign governance instead of preserving the upstream mandatory pipeline.

### D-003 — Core-First integration
CoreReplica uses Core-First Governance as the preferred procedural owner when available. It does not copy the full Core-First method into a new architecture skill. Architecture/ownership/reuse materiality routes to `core-first-extension-architecture`; user/external runtime claims route to `observable-product-verification`; fresh architecture verification and Independent Review remain separate triggered layers.

### D-004 — APC use
Agent Project Compiler principles define CoreReplica's durable authority model: Product Truth, Realization Truth and Verification Truth are separate, project authorities outrank chat/skill memory, and JIT routing is preferred over context hydration.

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
CoreReplica never creates `architecture.md` as a competing project authority merely because a reference reconstruction is underway. In an existing repository it consumes current architecture/project authorities first. In Greenfield work, Core-First/APC owner decomposition establishes the architecture before implementation.

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
