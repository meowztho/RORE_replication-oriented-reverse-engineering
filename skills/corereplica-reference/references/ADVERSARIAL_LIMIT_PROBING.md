# Adversarial Limit Probing

Load this JIT reference when understanding the target depends on discovering **where its assumptions stop holding**: boundary values, unusual sequencing, replay, concurrency, timing, parser/normalization differences, stale state, recovery behavior, authority/trust boundaries, resource limits or failure paths.

The purpose is **reference understanding**, not exploit maximization. A broken assumption is useful because it reveals a hidden contract, state transition, owner, parser boundary or dependency.

This procedure adapts selected domain-neutral reasoning patterns from the MIT-licensed `zhaoxuya520/reverse-skill` security/CTF material while deliberately excluding its payload, exploit-chain and offensive-operations procedures.

## Core model

```text
expected invariant / assumption
→ controlled perturbation
→ differential observation
→ minimal decisive effect
→ inferred mechanism / hidden contract
→ Evidence → Finding → Path → Reference Model
```

Prefer **proof of mechanism** over proof of maximum impact.

## 1. Build an assumption map

For the active flow/component, state the assumptions that appear to keep it valid. Examples:

- input has a type/range/shape/order;
- step B follows step A;
- an action occurs once;
- one actor owns one resource/state transition;
- one parser/loader/layer interprets the same object consistently;
- a cache/config/derived view is current;
- read/check/write happens atomically enough for the intended result;
- a retry is idempotent;
- a file/resource is present, unique or correctly versioned;
- a service/process/worker remains available;
- restart/crash/recovery preserves or restores expected state.

Do not assume these are requirements of the target product. They are investigation hypotheses until evidenced.

## 2. Perturb one dimension at a time

Use the smallest safe change that can distinguish hypotheses. Useful dimensions include:

- **value boundary** — minimum/maximum/zero/empty/null/unexpected type/size;
- **structure** — missing/extra/duplicate/reordered field or record;
- **sequence** — skip/replay/reorder/repeat a normal step;
- **identity/authority** — same operation under another legitimate role/context/owner in an authorized test setup;
- **time** — delay, retry, expiry, stale cache, async completion order;
- **concurrency** — two legitimate operations competing for the same mutable state;
- **layer/source** — base vs patch/override, client vs server, proxy vs backend, config vs runtime;
- **environment** — restart, offline/online transition, missing dependency, moved package/path, changed locale/encoding;
- **resource boundary** — representative small/large populations or constrained resource conditions when safe and material.

Change one primary variable where practical so the resulting delta remains interpretable.

## 3. Differential evidence

A surprising result is not enough. Compare against an explicit baseline.

Useful pattern:

```text
baseline input/state
→ baseline settled result

one controlled perturbation
→ perturbed settled result

material delta
→ candidate hidden rule / boundary
```

Where nondeterminism is material, repeat enough to distinguish a real pattern from noise and report the observed rate rather than pretending determinism.

## 4. State-machine and logic probing

When behavior is flow-dependent, model states and transitions rather than only screens/functions.

Probe questions such as:

- Can a later transition occur without the expected prior state?
- Is replay treated as a new action or the same action?
- Does cancellation/rollback restore all coupled state?
- Do retries duplicate side effects?
- Does the client merely hide a transition that the authoritative runtime still accepts/rejects differently?
- Which state variable actually gates the next transition?

Record the smallest sequence that changes the outcome and the state that changed.

## 5. Timing, concurrency and drift

Use this only when mutable shared state or async ordering is material.

Map:

```text
read
→ check
→ mutate/write
→ commit/persist
→ cache/queue/event propagation
```

Compare a clean baseline with a controlled reordered/concurrent run. Preserve timestamps/sequence identifiers when needed. Reduce the result to the minimal ordering that explains the state drift.

Do not turn concurrency into a stress/DoS exercise. The goal is to reveal ordering semantics, lock/idempotency assumptions or stale-state behavior.

## 6. Parser, loader and normalization differentials

When several layers interpret the same logical input, compare their effective views:

```text
raw input/artifact
→ layer A interpretation
→ layer B interpretation
→ effective runtime object/result
```

Useful targets include path/case/encoding normalization, duplicate fields, archive/package precedence, config inheritance, proxy/backend parsing, serialization versions and engine asset overlays.

A differential is valuable when it identifies **which layer owns the decisive interpretation**. Do not automatically treat it as a security defect.

## 7. Failure and recovery probing

Failure paths often reveal hidden ownership and persistence more clearly than the happy path.

When safe and authorized, inspect:

- invalid/missing dependency;
- interrupted operation;
- restart after partial state;
- corrupt/unknown record or optional field;
- failed network/service dependency;
- stale/missing cache;
- relocated package/path/locale/encoding changes;
- retry after timeout/crash.

Record what survives, what rolls back, what self-heals and which component performs recovery.

## 8. Primitive decomposition

When a defect or unusual behavior is found, decompose it into the smallest reusable mechanism instead of immediately chasing a longer chain.

Examples of safe conceptual primitives:

- input influences authoritative field;
- one state transition can be repeated;
- two layers disagree about identity/path;
- stale read precedes authoritative write;
- retry duplicates side effect;
- client-visible restriction is not the deciding runtime boundary;
- malformed/unknown structure shifts parser synchronization;
- recovery path restores state from another source.

Then ask: **what does this teach us about the target architecture/contract?**

## 9. Stop conditions and safety

Prefer reversible/local/sandboxed/working-copy perturbations. Establish baseline/reset/cleanup before stateful probes when material.

Stop escalating an effect when the mechanism is already sufficiently established for the reference question. Do not broaden from understanding a defect into destructive impact, credential/data acquisition, persistence, service disruption or unrelated exploitation merely because a longer chain exists.

If stronger probing would create consequential side effects and is not already authorized/safely isolated, keep the mechanism `PARTIAL`/`INCONCLUSIVE` or request the exact needed boundary through the normal project/user gate.

## 10. Synthesis into Reference Truth

Adversarial observations remain Reference Truth:

```text
Evidence: controlled perturbation + observed delta
Finding: inferred hidden invariant / failure mode / decision boundary
Path: where the perturbation flows to the decisive state/result
Reference Model: documented behavior, including edge/failure semantics
```

A discovered bug/quirk does **not** automatically become target Product Truth. A direct replica still needs an explicit `adopt | adapt | reject | inspiration-only` decision for that behavior.

## High-value questions

When unsure what to challenge next, ask:

1. What assumption must be true for this path to work normally?
2. What is the smallest safe perturbation that would falsify it?
3. Which layer should reject/normalize/recover the perturbation?
4. What observable result distinguishes the competing explanations?
5. If it fails, what hidden owner/state/parser/dependency does that reveal?
6. Have we learned the mechanism already, or are we merely increasing impact?
