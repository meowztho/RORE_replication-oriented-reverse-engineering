# Correction and Release Flow

## Finding correction

Verification finding flow:

```text
observable failure
→ evidence + exact symptom identity
→ current project routing/runtime trace
→ canonical responsibility owner / implementation anchor
→ correction by implementation owner
→ changed revision
→ fresh verification of affected claim
```

The verifier may propose likely routing but does not silently modify product code before recording the finding.

## Release boundary

Prepare all reversible release work that is authorized: validate config, build artifacts, draft DNS/env changes, create checklists, stage migrations, prepare store metadata, or configure preview environments as appropriate.

Define the exact consequential transition, for example:

- publish production release;
- switch traffic/DNS;
- run irreversible production migration;
- enable real charging;
- submit to an external store/reviewer;
- send a campaign;
- delete/replace production data.

Without explicit current approval, stop immediately before that transition. Do not treat a broad instruction such as "build the app" or "prepare launch" as approval to cross it.
