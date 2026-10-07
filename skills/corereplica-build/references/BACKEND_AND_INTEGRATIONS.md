# Backend and Integrations

Use project-native owners/providers first. These are conditional checks, not a mandated stack.

## Auth / authorization

- Authentication and authorization are separate responsibilities.
- Server-side authorization owns protected reads and writes; never trust client UI visibility as access control.
- When roles, teams or scopes exist, centralize the authorization decision behind the project's canonical owner rather than duplicating checks per route.
- Exercise at least one negative isolation case when multi-user data is material: another user/tenant must not see or mutate the first user's data.
- Sessions/cookies/tokens follow the project's security model; logout, expiry, reset/recovery and sign-out-everywhere are covered when required.
- Account deletion/export/privacy behavior must match Product Truth and current platform/legal obligations when material.

## Persistence

- Migrations are durable, reviewable and reproducible; avoid one-off manual production edits as the canonical path.
- Put invariants that must survive concurrency at the strongest appropriate owner/boundary, often including transactions, unique/exclusion constraints or idempotency records.
- Foreign keys, indexes, time, money and identifiers follow current project conventions and requirements rather than a universal schema template.
- Definitions/configuration remain distinct from mutable runtime state.
- Seed/test data is synthetic unless explicitly approved; do not use real people/customer data for fixtures.
- Backups/restore capability are verified when loss would be consequential; “backup enabled” without a usable restore path is weaker evidence.

## Payments

- Use official provider interfaces and the user's/project's own account.
- Use sandbox/test mode until the exact live-charging transition is approved.
- Verify webhook authenticity and idempotency when applicable; providers retry and may reorder events.
- Persist authoritative payment/subscription state behind the project's canonical payment/billing owner; client state does not become authority.
- Exercise material lifecycle states such as success, cancellation, failed payment/refund/reversal when they are part of Product Truth.
- Test/sandbox evidence does not silently prove live charging.

## Email, jobs and async work

- Transactional messages use the project's approved provider and fresh/original copy.
- Time-based jobs define schedule/time-zone semantics, retry behavior and observable failure handling when material.
- Repeated/retried jobs must not duplicate consequential side effects.
- Long-running/background work exposes enough state/logging to verify completion and diagnose failures without making logs the product outcome.

## External providers

For each material integration record or verify, from current official documentation when needed:

- public API/SDK and supported version;
- least-privilege scopes/permissions;
- authentication/refresh lifecycle;
- rate limits/quotas and retry/backoff semantics;
- webhook/event authenticity where applicable;
- provider review/verification requirements and likely lead time;
- failure/degraded-mode behavior.

Provider adapters stay behind target capability contracts. Do not treat observed/private credentials or endpoints as authorization; depend only on contracts/endpoints whose use is authorized for the target product, and never reuse another party's credentials.

## Uploads and untrusted input

When applicable, validate server-side type/size/content constraints, isolate storage/serving appropriately, avoid leaking user data through URLs/logs, and follow the project's existing malware/content-safety posture rather than inventing a second pipeline.

## Secrets

Do not put secrets in project truth, source control, logs or plugin artifacts. Use the host/project's approved secret mechanism and provide variable names/examples without live values. Never fabricate live credentials.

## Evidence

Prefer focused contract/integration tests plus the closest practical real boundary. Record what remains unverified: provider review, live payment, deliverability, production data scale, external rate-limit behavior, etc.
