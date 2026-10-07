# Runtime Corroboration

Load this JIT reference when a material Reference Truth claim depends on the **effective running target**, not merely on what static artifacts contain or appear to imply.

Runtime corroboration is **claim-sensitive**, not a blanket requirement to launch every target. Static/package/structured claims may remain static when that boundary fully proves the claim. But when the claim concerns effective loading, live state, temporal behavior, persistence, generated values, exercised content, runtime ownership, user interaction, async ordering, recovery, or another runtime-only boundary, a representative authorized real run should be attempted when practical before the claim is described as runtime-verified or the corresponding reconstruction is called complete.

## Core rule

```text
static/package evidence
→ candidate mechanism / runtime-sensitive claim
→ representative real run when practical + authorized
→ corroborate | refute | refine | remain runtime-unchecked
→ Reference Model
```

`not started` is not itself a failure.

`not started + runtime-sensitive claim presented as verified/complete` **is** an evidence-boundary failure.

## 1. Classify the claim boundary

Before launching anything, classify the claim:

- **STATIC_SUFFICIENT** — the claim is about artifact presence/structure/content and is fully supported at that boundary;
- **RUNTIME_SENSITIVE** — effective behavior depends on execution, loading, dynamic state, timing, user flow, persistence, generated values, authoritative runtime decisions or exercised reachability;
- **RUNTIME_REQUIRED_FOR_COMPLETENESS** — broad reconstruction would materially overstate coverage without testing at least one representative real path;
- **RUNTIME_UNAVAILABLE** — a real run is blocked by authorization, missing environment/tooling, unsafe side effects or inaccessible prerequisites.

Do not upgrade `RUNTIME_SENSITIVE` to `STATIC_SUFFICIENT` merely because the static evidence looks plausible.

## 2. Claims that commonly need runtime corroboration

Examples include, when material:

- which packaged/data-defined object is actually loaded or used;
- base/patch/override precedence at the effective runtime boundary;
- whether content is live, dead, legacy, feature-gated, mode-specific or unreachable;
- generated/defaulted/overridden values after initialization;
- actor/entity/component relationships that only exist after spawn/load;
- navigation/pathfinding/physics/animation/timing behavior;
- user input, focus, keyboard/controller, interaction and visible state transitions;
- process/service/worker/child-process behavior;
- filesystem/registry/config/database persistence and cleanup;
- client-vs-server or UI-vs-authoritative-runtime decision boundaries;
- network/API/runtime request formation and response handling;
- queues/jobs/events/async propagation and settled state;
- crash/restart/recovery and idempotency semantics.

Artifact existence alone does not establish any of these effective-use claims.

## 3. Bind runtime to the same target identity

Before correlating static and runtime evidence, confirm that the running target matches the analyzed artifact/version/build/environment strongly enough for the claim.

Useful anchors include:

```text
binary/package hash
build/version/revision
install/package identity
environment/account/region when material
loaded module/package/resource identity
```

If runtime and static inputs differ, record the mismatch and treat the comparison as cross-version/cross-environment evidence rather than silently merging them.

## 4. Run with a question, not aimlessly

A runtime launch should discriminate hypotheses. Prefer a small list such as:

```text
claim / question
static evidence
expected runtime discriminator
observable boundary
capture method
reset/cleanup needs
result
```

Examples:

- `Enemy_A` references `StatsRow_17`; observe whether a spawned `Enemy_A` receives those effective values.
- Two map layers contain the same logical actor; observe which layer produces the live object.
- Base and patch packages define one asset identity; observe the effective loaded version.
- A desktop package mirrors settings into AppData; run, mutate one setting, close/restart, and inspect the settled state.

The purpose is not to "use the app for a while". It is to connect static/reference structure to effective behavior.

## 5. Observe the closest practical boundary

Prefer the boundary that can actually prove the claim:

- rendered/user-visible state for UI behavior;
- process/file/registry/database state for host integration;
- runtime objects/logs/debugger/instrumentation for live program structure;
- network/API traces for request/response semantics;
- gameplay/entity transforms/state for game behavior;
- persisted/reloaded state for durability;
- authoritative backend or service outcome when the client is not decisive.

Logs/tool exit codes may support a claim but do not replace the relevant observable boundary when they cannot prove it.

## 6. Distinguish presence, reachability and exercised behavior

For broad reconstruction, keep these separate:

```text
PRESENT
  artifact/object exists

REFERENCED
  another artifact/object points to it

REACHABLE
  a runtime path can load/reach it

EXERCISED
  the observed run actually used it

EFFECTIVE
  it materially determined the settled behavior/state being claimed
```

Do not call unused/dead/legacy content part of effective runtime behavior solely because it exists in the package.

## 7. Reconcile static and runtime evidence

When runtime agrees with static evidence, strengthen only the proven boundary.

When they disagree, preserve both and investigate likely causes:

- wrong object identity;
- version/build/environment mismatch;
- base/patch/override precedence;
- dead/unreachable code/content;
- generated/defaulted runtime state;
- conditional/feature-gated path;
- parser/decompiler interpretation error;
- stale cache or persistence;
- another authoritative owner/layer.

A disagreement is valuable evidence, not permission to discard whichever source is inconvenient.

## 8. Side effects and reset

Before a state-changing run, identify material side effects and how the baseline will be restored or distinguished. Prefer disposable profiles, test accounts, copied installs, snapshots, temporary data roots or other reversible setups when practical.

For crash/recovery, persistence or destructive-edge probes, use the same baseline/cleanup discipline as CoreReplica verification. If a stronger probe would create material consequences outside the authorized safe boundary, leave the claim `PARTIAL`/`INCONCLUSIVE` rather than manufacturing proof.

## 9. Runtime status language

Use explicit statuses when useful:

- `STATIC_SUPPORTED`
- `RUNTIME_CORROBORATED`
- `RUNTIME_REFUTED`
- `RUNTIME_PARTIAL`
- `RUNTIME_UNCHECKED`
- `RUNTIME_BLOCKED`

These are Reference Truth qualifiers, not Product/implementation completion states.

## 10. Completion and stopping

For a narrow static question, no runtime launch is required if the static boundary fully answers it.

For broad software/game/web/system reconstruction, before claiming the relevant slice is understood or complete, ask:

1. Which material claims are runtime-sensitive?
2. Has at least one representative real path been exercised for each important runtime class?
3. Are static-only conclusions clearly labeled where no runtime corroboration exists?
4. Did runtime evidence reveal dead content, generated state, alternate owners or layer precedence that changes the model?

Stop additional runtime work when the requested runtime-sensitive mechanisms are sufficiently established, remaining gaps are explicit, or further runs have low information value relative to cost/risk.
