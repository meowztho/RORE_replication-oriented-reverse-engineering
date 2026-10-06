# Side-Effect-Safe Verification

Read before exercising a real boundary that can mutate the host, user data, filesystem, registry/config, database, accounts, external services, payments, messages, devices, or another persistent environment.

## Preflight

1. Name the claim and the exact boundary that must be exercised.
2. Inventory plausible side effects and residue, including failure/crash paths.
3. Prefer the least invasive representative environment: disposable copy/profile, temp directory, test account/tenant, staging database, sandbox provider mode, VM/container, or another project-native isolation seam.
4. Capture a baseline/snapshot of the state that must be restored or proven unchanged.
5. Define cleanup/recovery before the run, including what happens after forced termination or partial failure.
6. If isolation is impossible and the consequence is material, obtain the required user approval or leave the claim INCONCLUSIVE rather than silently risking real state.

## During and after

- Observe the intended boundary plus residue indicators, not merely process exit/tool success.
- Distinguish graceful shutdown from forced termination when cleanup semantics differ.
- After the run, verify restoration/cleanup explicitly. A cleanup command returning success is not proof that residue is gone.
- If a failure leaves state behind, record the finding before repair/cleanup; then restore safely and re-run on the corrected revision.
- When crash recovery is itself a requirement, inject a controlled interrupted state and verify the next-run recovery path separately.

## Oracle freshness/liveness

If an evidence source can replay stale data (screenshots, caches, logs, mirrors, telemetry), prove it is live when that matters. Use a controlled stimulus or an independent activity signal; identical observations alone do not prove staleness because the real scene may legitimately be static.

Record what the oracle cannot see. Synthetic/disposable evidence proves only the boundary exercised; a final representative real-environment check may still be required.
