---
name: corereplica-release
description: Prepare and gate a CoreReplica product release using current verification evidence and project-native deployment rules. Use for production preflight, environment/DNS/provider preparation, deploy/publish/store-submit, live charging, or release readiness. Continue authorized reversible preparation, but do not cross the exact consequential transition without explicit current approval.
---

# CoreReplica Release

Own **release preparation and release-gate evaluation**, not Product Truth or Verification Truth.

## Release semantics

```text
Product/Acceptance scope
+ current sufficient Verification Truth
+ project-defined release prerequisites
= release-ready candidate

release-ready candidate
+ explicit approval for exact consequential transition
= transition may execute
```

A parity score, passing build, zero S1 bugs, clean brand sweep, or tool success alone is never release authority.

## JIT depth

Read `references/PRODUCTION_READINESS.md` when production environment/data, DNS, payments, OAuth, email, operational monitoring, rollback, mobile/store or other production-readiness concerns are material.

## Procedure

1. Read current project release/deployment authorities first. Do not impose a universal host, stack or store process.
2. Reconcile current required outcomes and current verifier-owned evidence. Stale/missing evidence stays missing.
3. Run project-native build/test/security/data/migration/privacy/operational checks that are actually applicable.
4. Verify current external provider/platform requirements from official sources when material.
5. Complete reversible preparation that is already authorized: draft env/DNS settings, validate migrations, prepare preview/staging, configure non-live resources, assemble store metadata, generate runbook/rollback steps.
6. Define the exact gated transition and the evidence that counts as approval.
7. If approval is absent, stop immediately before the transition while clearly reporting what is prepared, what remains, and what exact action is gated.
8. After an approved transition, verify the real production/external outcome on the relevant settled boundary. Do not treat the deploy command's success as proof that the user flow works.

## Examples of consequential transitions

- production traffic switch / live deploy;
- irreversible or high-risk production migration;
- enabling live payments/real charging;
- external store submission/publication;
- sending a real campaign/message;
- production deletion/replacement.

Use project-specific semantics; do not create an approval engine merely because a gate exists.

## Fallback output

`corereplica/release/RELEASE_GATE.md` with:

- target revision/environment;
- required current verification evidence;
- project release checks and results;
- reversible preparation completed;
- exact gated transition;
- approval authority/source and current status;
- rollback/monitoring plan where material;
- post-transition verification requirement.
