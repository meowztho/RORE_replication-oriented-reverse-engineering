# Flow and Parity Verification

Use when target requirements contain multi-step user flows, stateful behavior, cross-user isolation, or intentional reference parity.

## Build the plan from target requirements

For each material flow, derive stable cases from the target Acceptance authority, not merely from what the reference app exposes:

- happy path and expected settled outcome;
- empty/missing input;
- long input, Unicode/emoji and boundary values where relevant;
- duplicate submit/double click and concurrency races;
- back/refresh/interruption/resume when stateful;
- slow network/offline/provider failure when material;
- expired/invalid session and permission denied;
- second-user/tenant isolation;
- time-zone/DST/date-boundary behavior when relevant;
- responsive/mobile behavior for supported surfaces;
- keyboard/focus/screen-reader semantics for accessible UI;
- destructive or consequential actions with exact confirmation/gate semantics.

Do not turn this checklist into mandatory tests for irrelevant concerns. Select the cheapest cases likely to falsify the next claim.

## Automation

Use the project's existing test framework when possible. For browser E2E, stable role/label/test-id selectors are preferable to presentation-only selectors. Failures in console/network can be useful supporting evidence, but no log substitutes for the expected user-visible state when that is the claim.

For flows that cannot be automated economically, use a bounded manual/agent-driven pass and record evidence explicitly instead of pretending coverage.

## Visual/layout comparison

When reference comparison is intentionally required:

- capture the same target state and comparable viewport/data shape;
- use layout/image-diff tooling only as structural evidence;
- record reference and target evidence identities/revisions;
- compare behavior separately: completion steps, errors, remembered state, resulting external effects and messages.

Do not chase pixel identity with a third-party product. The target Design/Product authority decides acceptable similarity and intentional divergence.

## Finding discipline

A finding records exact reproduction, expected/actual outcome, severity/impact when useful, evidence and revision. Verification remains read-only with respect to product implementation: route correction to the canonical owner, then re-run the affected cases on the changed revision.
