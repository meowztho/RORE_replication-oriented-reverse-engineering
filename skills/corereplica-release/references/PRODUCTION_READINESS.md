# Production Readiness

Use only for the parts relevant to the target project's deployment/runtime.

## Environment and data

- Preserve a clear development/staging/production boundary where material.
- Production migrations are reproducible and have an appropriate backup/rollback or recovery plan for their risk class.
- Production secrets/config use the approved environment/secret mechanism and match the declared configuration contract.
- Confirm privacy/export/deletion/data-retention behavior that is actually required before release.

## External services

- Payments: live-mode enablement is its own consequential transition; production webhook/signing configuration and a bounded live verification are required only after approval.
- OAuth/integrations: production redirect/origin configuration, required provider review and least-privilege scopes are current.
- Email: sending-domain/provider verification and deliverability basics are ready when email is product-critical.
- DNS/domain changes use the provider's current authoritative values, not hard-coded historical defaults.

## Operational checks

- Production build/package succeeds.
- Required current Verification Truth covers the release's required outcomes.
- Applicable security/data checks pass.
- Error/health/logging/uptime observability is sufficient for the product's risk level.
- Rollback/disable path is known for consequential releases.

## After the transition

Verify the real production/external outcome: canonical URL, core user flow, auth/session, persistence and any consequential provider side effect required by the release. Tool/deploy status alone is not completion evidence.
