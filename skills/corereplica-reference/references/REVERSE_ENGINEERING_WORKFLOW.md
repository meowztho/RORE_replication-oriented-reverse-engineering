# Reverse Engineering and Reference Recovery Workflow

Load only when the reference mission requires more than ordinary surface/document research: extraction/unpacking, decompilation/disassembly, static/dynamic analysis, browser/runtime capture, protocol/data-format recovery, game/engine inspection, or system reconstruction.

This procedure adapts selected workflow ideas from `zhaoxuya520/reverse-skill` under MIT provenance. CoreReplica does not import its pentest/exploit/CTF routing stack as product ownership, but it does reuse the domain-neutral adversarial reasoning behind those disciplines when that reasoning reveals limits, hidden contracts, state transitions or failure semantics.

## 1. Establish target identity and analysis surface

Before deep analysis, establish the strongest practical identity of the target: product/version/build, URL/environment, package/binary hash, artifact revision, dataset revision, or equivalent. Preserve the original/raw source when practical and work from derived copies for transformations that could alter it.

Record the authorized scope and any retention/VCS/share constraints separately from analysis permission. Bind the working analysis state to the strongest practical target identity (hash/build/revision/environment). Reusing a prior workspace for a changed artifact requires explicit cross-version correlation; do not silently carry old Findings into a new hash/revision.

## 2. Broad triage before narrow depth

Perform low-cost breadth sufficient to reveal the useful branches:

- target/container/file/runtime types;
- platform/runtime/framework/engine/language clues;
- package/archive/bundle/resource structure;
- manifests, metadata, strings, imports/exports/symbols when applicable;
- visible/runtime surfaces and entry points;
- network/API/storage/IPC boundaries when applicable;
- known version/layer relationships such as base + patch/override.

The purpose is to choose the next high-information analysis path, not to complete a fixed checklist.

## 3. Extraction / recovery

Use **format-first dispatch**: identify the container/file/package type and useful metadata before choosing an extractor when practical. A failed preferred extractor is evidence about that method, not proof that the target contains nothing. When the expected information value is material, try an alternate compatible extractor/parser or lower-level scan before concluding the content is inaccessible.

For nested packages/archives/bundles, recurse intentionally while preserving the lineage from parent container to child artifact. Use depth/size/resource bounds so recursive extraction cannot become an uncontrolled expansion. Validate that an extractor actually produced plausible expected artifacts rather than treating exit code alone as semantic success.

Use authorized transformations when they materially expose information, including as applicable:

- unpacking/decompression/container extraction;
- decompilation/disassembly/bytecode recovery;
- resource/asset extraction and format conversion;
- symbol/metadata/schema/table extraction;
- source-map or bundled-source recovery;
- structured decoding of serialized/custom formats;
- database/export parsing;
- map/entity/component/asset relationship extraction in game/engine targets.

Prefer reproducible transformations. Keep raw/reference sources authoritative and derived outputs disposable/recreatable when feasible.

Broad extraction is valid when it is authorized, practical and increases coverage. Avoid indiscriminate bulk work whose cost is high and expected information value is low; inventory first so breadth is intentional rather than accidental. Preserve failed extractor/parser attempts when they meaningfully narrow the format/tool hypothesis.

## 4. Static analysis

Use static evidence to recover likely structure and causal relationships. When working through a decompiler/disassembler, prefer a **tool-neutral semantic query surface** where possible: function identity, callers/callees, cross-references, strings/constants, types, imports/exports, control/data-flow anchors and annotations. IDA/Ghidra/Binary Ninja/angr or another backend is a provider, not a new Reference Truth owner.

LLM-generated function summaries, variable/function renames, source-identification guesses and vulnerability/behavior annotations can accelerate triage, but they remain **derived semantic hypotheses** until grounded in the underlying program evidence. Keep raw decompiler/disassembly facts recoverable and make annotations reversible.

Use static evidence to recover likely structure and causal relationships:

- components/modules/classes/functions/resources;
- references/dependencies and producer/consumer relationships;
- schemas/entities/records and cross-references;
- algorithms, constants, state machines and validation/transformation logic;
- user/runtime flow entry points and likely call/data paths;
- assets/materials/layout definitions where relevant.

Assign confidence/evidence kind. Do not describe low-quality decompilation, strings or name occurrence as stronger structural/runtime proof.

## 5. Dynamic/runtime analysis

Use the closest authorized runtime boundary when behavior, state or generated values cannot be established reliably from static artifacts alone.

Examples:

- browser: DOM/accessibility state, network requests, storage, loaded scripts, runtime function inputs/outputs, navigation and settled states;
- desktop/mobile: process tree, files, registry/config, database, IPC, network, child services, user-visible behavior;
- game/simulation: live entities, transforms, navigation, state changes, timing/physics/animation, runtime-loaded assets/data;
- service/system: requests/responses, event/state transitions, persistence, queues/jobs and cross-service effects.

Static analysis supplies hypotheses; runtime observation tests or enriches them. When they disagree, preserve both raw evidence and investigate the cause (version/layer mismatch, dead code, conditional path, stale artifact, parser error, generated/defaulted state, another authoritative layer, etc.).

Before broad reconstruction is described as complete, classify material conclusions as static-sufficient or runtime-sensitive. If a runtime-sensitive claim matters and a representative authorized run is practical, use `RUNTIME_CORROBORATION.md` to exercise a targeted real path. Do not require a launch for a claim that static evidence already proves, but do not present `RUNTIME_UNCHECKED` static inference as runtime-verified behavior. Distinguish `PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE` when packaged content may include dead/legacy/mode-specific material.

When executing or instrumenting an unknown/untrusted binary or stateful target could have consequential side effects, record the analysis environment that makes the run interpretable and reversible (for example VM/container/snapshot, working copy, network posture and reset/cleanup path as applicable). Dynamic analysis on an uncontrolled host is not required merely because static analysis is incomplete; in that case keep the runtime boundary explicit rather than fabricating completion.

## 6. Mechanism fan-out and enforcement-site coverage

A behavior may be enforced by several call sites, layers, validators or data gates. Finding one decisive-looking check does not prove the complete mechanism.

When the question is broad parity, removal/reproduction of a restriction, or complete mechanism understanding, map materially relevant enforcement sites and layers:

```text
semantic rule / decision
→ callers / validators / data gates / runtime layers
→ per-site role
→ covered / unresolved / dead / version-specific
```

Use call/data-flow, references, runtime observations and source-layer evidence to distinguish duplicated enforcement from one shared owner. Report coverage such as `13 known sites / 13 mapped` only when the population is actually supported. One successful local modification or one call-site trace cannot certify complete fan-out coverage.

## 7. Comparative and cross-version analysis

Different builds/versions can be a high-value differential source. When comparing them, prefer stable **semantic anchors** over raw offsets:

- call relationships and function behavior;
- symbols/signatures/patterns and nearby constants;
- schemas/field relationships and asset identities;
- protocol/state semantics;
- reproducible source/data paths.

Absolute offsets/addresses are version-local evidence unless re-established. A port to another build should re-resolve the semantic identity and re-verify the relevant path rather than transplanting offsets blindly.

Version diffs can reveal when behavior was introduced/removed, isolate changed validators, recover symbols/names or explain documentation conflicts. Preserve both versions' identities and the comparison method.

## 8. External research and public-source corroboration

When an unknown technology/format/identifier/version rule or unresolved hypothesis can benefit from public knowledge, read `EXTERNAL_RESEARCH_AND_CORROBORATION.md`. Use external sources to discover mechanisms and new local evidence classes, then corroborate target-specific claims at the target boundary when material. If Internet capability is unavailable, emit a focused research packet instead of guessing.

## 9. Adversarial / limit probing

When the normal path does not expose an important contract, challenge one assumption at a time. Useful dimensions include value/shape boundaries, sequence/replay, timing/concurrency, identity/authority context, layer/source precedence, parser/normalization differences, restart/recovery and representative resource limits.

Use an explicit baseline and a minimal perturbation, observe the settled differential, and reduce the result to the smallest mechanism that explains it. The goal is to discover semantics such as hidden validation, state-machine gates, idempotency, ownership, recovery, parser precedence or async ordering.

Read `ADVERSARIAL_LIMIT_PROBING.md` for the detailed JIT procedure. Prefer proof of mechanism over escalation of impact. A discovered defect or quirk remains Reference Truth and does not become a replica requirement without a Product Truth decision.

## 10. Hypothesis-driven replanning

Maintain a small set of live questions/hypotheses only when they affect next actions. For each meaningful branch record:

```text
question / hypothesis
supporting evidence
contradicting evidence
next discriminator
status: open | supported | rejected | unresolved
```

If repeated actions produce no new evidence, change anchor/tool/method or lower the claim. Do not keep repeating the same failed technique merely because it is the familiar tool.

## 11. Evidence → Finding → Path synthesis

Promote raw observations carefully:

```text
Evidence
→ supported Finding
→ connected Path (call/data/runtime/user/system)
→ Reference Model
```

Useful Paths include:

- user action → UI/controller → service/API → persistence → resulting state;
- package/resource → loader/parser → runtime object → visible behavior;
- input → transform/algorithm → output;
- event → producer → queue/message → consumer → state mutation;
- game spawn → actor/entity definition → navigation/path → combat/result;
- web request → initiator script/function → parameter transform → API response → rendered state.

A Path is a compact causal model, not a replacement for raw evidence.

## 12. Coverage and gap loop

For broad reconstruction, periodically ask what material classes of knowledge remain weak:

- user-visible surfaces/flows/states and input/control behavior;
- functional rules/state machines/validation;
- architecture/components/ownership/producer-consumer paths;
- data/schema/content populations and relationships;
- algorithms/transforms/calculations/generated/defaulted values;
- packages/containers/assets/resources and load/override relationships;
- runtime/state/persistence/caches/processes/services/workers/recovery;
- external integrations/network/API/protocol behavior;
- visual/layout/media/audio/animation semantics when material;
- configuration/feature flags/build/version/layer precedence;
- installation/update/relocation/portability/environment dependencies;
- timing/concurrency/performance/resource semantics when they affect behavior;
- failure/edge states and trust/authority boundaries.

Continue high-value analysis until requested coverage is met, the next step is genuinely blocked, or information gain becomes low relative to cost. Report residual gaps explicitly instead of silently declaring the target understood.

## 13. Tool/provider discipline

Tool choice follows the target and question, not habit. Discover actual host capabilities and versions before relying on them. Examples of tool families may include decompilers/disassemblers, archive/resource extractors, browser/CDP tools, packet/network observers, debugger/instrumentation tools, database parsers and engine-specific viewers, but CoreReplica does not require or bundle a universal toolchain.

When a specialized companion skill/plugin already owns detailed engine/tool usage, use it as a procedure provider while keeping Reference Truth in CoreReplica.

## 14. Output

The desired result is a **usable reference corpus**, not just a narrative report:

- source/inventory with stable identities;
- reproducible raw/derived Evidence refs;
- evidence-backed Findings;
- causal/call/data/runtime Paths;
- reconstructed Reference Model;
- explicit coverage and unresolved gaps;
- optional machine-readable tables/exports useful to the target project or APC.
