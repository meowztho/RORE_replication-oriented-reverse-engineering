---
name: corereplica-build
description: Implement CoreReplica target requirements in the current project/workspace through its canonical owners, contracts, data paths, and design system. Use for source changes, screens, flows, backend/auth/data/payments/jobs/integrations, or replacing temporary/fake paths. Do not redefine product scope, create clone-specific parallel owners, or mark requirements verified from implementation progress.
---

# CoreReplica Build

Own implementation execution and non-authoritative progress only.

## Preconditions

Before a material reference-derived feature is implemented:

- the target requirement exists in Product Truth;
- relevant reference observations are sourced if the behavior depends on them;
- architecture/ownership/reuse is resolved through current project authorities and Core-First when material;
- design/system contracts are known when the change affects shared UI semantics.

If any of those are unresolved, route back rather than inventing a local answer.

## Core rules

1. Implement from target requirements and authorized reference evidence. Source access/analysis does not by itself authorize target inclusion or redistribution; any third-party code/assets/copy/binaries/data/API dependency included in the product must have a documented basis covering its intended use.
2. Reuse/correct/configure/compose existing project owners before extending architecture.
3. Equivalent producers converge before domain behavior. A builder/importer/agent/reference path does not get a private business-rule path.
4. Keep fake/synthetic data behind the same declared consumer contract when used for a walking skeleton. Mark resulting evidence synthetic; it cannot prove representative production behavior.
5. Use project-native data/auth/integration boundaries. Do not hard-code a universal SaaS stack.
6. Current external API/provider facts are checked against current official documentation when material.
7. Record progress, not acceptance.

## Implementation status

Fallback schema `corereplica/implementation/IMPLEMENTATION_STATUS.csv`:

```text
requirement_id,status,revision,notes
REQ-001,implemented,<revision>,...
```

Allowed status values may include `not_started | in_progress | implemented | blocked`. They are execution hints only. `corereplica-verify` does not treat them as proof.

## Vertical proof without architecture distortion

Prefer an early production-shaped walking skeleton when useful, but only enough core to prove a real owner/contract path. Do not build throwaway local architecture merely to show a screen quickly.

## Backend and integrations

Read `references/BACKEND_AND_INTEGRATIONS.md` JIT when auth, persistence, payments, email/jobs, external providers, webhooks, multi-tenancy, security, privacy/deletion or production data concerns are material.

## Completion of a build lane

A build lane may report implementation complete for its scope when code/config/migrations and focused checks are complete. It must not claim the target outcome `VERIFIED` unless the verification owner has current sufficient evidence.
