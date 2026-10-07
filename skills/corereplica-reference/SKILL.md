---
name: corereplica-reference
description: Reverse-engineer and reconstruct an authorized reference target into qualified, usable Reference Truth. Use for software, websites, games, binaries, packages, APIs, formats, datasets, services or systems when the user wants to know how they work, recover data/assets/structures/algorithms/flows, extract/decompress/decode/decompile material, research public sources to resolve unknowns, or build a reference corpus. Do not turn recovered knowledge into target Product Truth or silently broaden authorization.
---

# CoreReplica Reference Reconstruction

Own the **Reference Truth procedure**. The goal is not merely to describe visible features; it is to recover as much useful technical knowledge as practical inside the authorized scope and turn it into evidence-grounded models that another agent can use.

This skill does **not** compile a durable target project package. When APC is selected, hand APC the qualified reference corpus; APC owns project compilation.

Read `corereplica-orchestration/references/SOURCE_USE_AND_DISTRIBUTION_POLICY.md` JIT when source, retention, VCS/share, licensing, inclusion or redistribution boundaries are material.

## Mission

Use progressive analysis rather than a surface-only checklist:

```text
target / question
→ survey + inventory
→ acquire / extract / unpack / decode / decompile when useful
→ static structural analysis
→ dynamic/runtime observation when useful
→ correlate evidence
→ Findings + Paths
→ Reference Model
→ unresolved-gap loop
```

This is **not a mandatory linear pipeline**. Enter at the strongest available boundary and revisit earlier/later analysis modes when new evidence changes the best path.

When the user's mission is broad reconstruction, do not stop merely because one claim has enough evidence. Prefer cheap breadth first, then deepen high-value unresolved areas until requested coverage is reached, work is genuinely blocked, authorization/tooling prevents further progress, or the marginal information value becomes low.

## Inputs

Eligible inputs include, within actual authorization and applicable terms:

- public docs/help/changelog/store pages, public APIs and public walkthroughs;
- user-supplied screenshots, recordings, files, dumps and exports;
- the user's own authorized account/runtime;
- user-controlled installations, archives, packages, binaries, assets, source, databases, logs and data;
- live browser/desktop/service/runtime observations through available authorized tools.

Current facts that can drift require current evidence.

## Analysis modes

Classify the target before choosing depth/tools. Common modes include:

- **surface/black-box** — UI, flows, visible states, inputs/outputs;
- **artifact/package** — archives, installers, bundles, resources, manifests, assets;
- **compiled/static** — binaries, libraries, bytecode, metadata, symbols, strings, imports/exports, decompilation/disassembly;
- **structured-data** — schemas, records, tables, formats, indexes, cross-references;
- **dynamic/runtime** — process behavior, memory/state, files, registry/config, IPC, network/API, timing and persistence;
- **web/runtime** — DOM/accessibility surface, network requests, scripts, source maps, storage, runtime functions and backend contracts observable from the authorized client path;
- **game/engine** — packages/assets/data tables/maps/entities/components/materials/animations/engine metadata plus live gameplay/runtime behavior;
- **protocol/system** — messages, state transitions, producers/consumers, storage and cross-service paths.

Use several modes when the target crosses boundaries. Tool/provider choice is implementation detail, not a new Reference Truth owner.

## Tool discovery

Before relying on a specialized tool/provider:

1. inspect the host/project for actually available capabilities, paths and versions;
2. prefer an existing suitable tool/MCP/script instead of recreating it;
3. do not guess executable paths, installed versions or MCP availability;
4. if a preferred tool is absent, choose a valid alternate method or report the missing capability; install/configure tools only when authorized and material;
5. record the tool/method version when it materially affects reproducibility or interpretation.

Read `references/REVERSE_ENGINEERING_WORKFLOW.md` when extraction/decompilation/static/dynamic analysis or multi-surface reconstruction is material. Read `references/RUNTIME_CORROBORATION.md` when a material claim depends on effective running behavior or broad reconstruction would otherwise overstate runtime coverage. Read `references/ADVERSARIAL_LIMIT_PROBING.md` when hidden contracts are best exposed by boundary, sequence, replay, timing, concurrency, parser/layer, recovery or failure-path perturbation. Read `references/EXTERNAL_RESEARCH_AND_CORROBORATION.md` when public docs/source/history/research can resolve an unknown, reveal a new local evidence source, explain versioned semantics or independently challenge a local hypothesis.

## Reference corpus

Use existing project reference authorities when present. Otherwise create only the useful subset of:

```text
corereplica/reference/SOURCE_LOG.md
corereplica/reference/INVENTORY.md
corereplica/reference/HYPOTHESES.md
corereplica/reference/FEATURE_OBSERVATIONS.csv
corereplica/reference/EVIDENCE/
corereplica/reference/FINDINGS.md
corereplica/reference/PATHS.md
corereplica/reference/REFERENCE_MODEL.md
corereplica/reference/DERIVED/
corereplica/reference/scratch/       # local-only intermediates when needed
```

Raw/local-only material does not become VCS/shareable project content merely because it is useful evidence.

### Evidence → Finding → Path

Keep these meanings distinct:

- **Evidence** — what was directly observed/acquired, with a source/ref and reproducible method when practical;
- **Finding** — an evidence-backed interpretation such as recovered behavior, algorithm, schema, component role or constraint;
- **Path** — a connected user-flow/call-flow/data-flow/runtime-flow/producer-consumer path grounded in Evidence/Findings;
- **Reference Model** — the synthesized current understanding built from those paths/findings, with coverage and unknowns explicit.

A Finding must not outrun its Evidence. A Path must not use an unqualified guess as if it were a proven edge.

## Evidence qualification

`FEATURE_OBSERVATIONS.csv` fallback schema:

```text
id,area,observation,evidence_ids,evidence_kind,confidence,notes
```

When transformation/extraction/conversion, parser output, heuristic matching, large populations, layered sources, completeness or independent-corroboration claims are material, read `references/EVIDENCE_QUALIFICATION.md` and apply:

```text
acquire
→ identify
→ interpret
→ qualify
→ record coverage/unknowns
```

Ambiguous identity or source precedence fails closed rather than selecting the most plausible candidate simply to keep moving.

## Analysis loop

1. **Survey** — establish target identity, scope, versions, surfaces, containers/artifacts and obvious runtime boundaries.
2. **Inventory** — enumerate relevant files/resources/endpoints/scripts/components/records/surfaces before deepening one branch too early.
3. **Recover** — extract/unpack/decode/decompress/decompile/convert material that exposes additional structure or data.
4. **Static interpret** — recover structures, constants, schemas, references, algorithms, dependencies and likely paths.
5. **Dynamic observe** — classify material claims as static-sufficient or runtime-sensitive. When a runtime-sensitive claim matters and a representative authorized real run is practical, exercise the real path rather than promoting static inference into runtime truth. If runtime is unavailable, keep the claim explicitly runtime-unchecked/partial instead of calling the slice complete.
6. **Correlate** — connect Evidence into Findings and Paths; back-annotate runtime discoveries into the static model where useful. Distinguish artifact presence/reference from runtime reachability, exercised use and effective behavior.
7. **Challenge assumptions** — when normal-path evidence leaves hidden contracts unclear, use controlled adversarial/limit probes to vary one material dimension and observe the differential. Seek mechanism understanding, not maximum impact.
8. **Research externally when useful** — use version-aware public documentation/source/history/research to discover mechanisms, source locations, formats and discriminating hypotheses; corroborate target-specific claims against the target when material.
9. **Gap loop** — maintain explicit hypotheses/unknowns and choose the next analysis action by expected information gain. Repeated actions that produce no new evidence should cause a tool/anchor/method change rather than an endless loop.
10. **Synthesize** — reconcile current views into the Reference Model, preserving coverage limits, unresolved identities and contradictory evidence.

## Evidence discipline

- `CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY`.
- Tool success is not semantic correctness.
- A static decompile is an interpretation, not runtime truth.
- Runtime observation may refute a static hypothesis; explain the discrepancy instead of forcing agreement.
- A screenshot proves the visible state it contains, not hidden temporal behavior.
- Parseable output does not prove requested object identity.
- A correct subset does not prove completeness.
- Two tools are not independent if they share the same material failure assumption.
- Negative/failed analysis attempts are useful evidence when they narrow hypotheses.
- Public/Internet research can discover or explain a mechanism, but a target-specific claim remains externally documented until the actual target corroborates it or the user explicitly asks only what the external source states.
- LLM/decompiler-generated summaries, names and source guesses are derived annotations/hypotheses unless independently grounded in program evidence.
- Preserve raw/source evidence separately from normalized or cleaned candidate views.
- Controlled edge/failure behavior can reveal hidden contracts, but a defect/quirk remains Reference Truth until Product Truth explicitly decides what to do with it.
- Unknown remains unknown; do not fill gaps from genre/domain expectations.

## Reconstruction coverage challenge

For broad replication/reconstruction, challenge whether a competent analyst could name a material ordinary knowledge class that is neither covered nor explicitly unresolved/excluded. Do **not** turn this into a mandatory checklist for narrow tasks; use it to prevent premature "we understand the product" claims. Relevant classes may include:

- user-visible surfaces, flows, states and input/control behavior;
- functional rules, state machines and validation;
- architecture/components, ownership and producer/consumer paths;
- data/schema/content populations and relationships;
- algorithms, transforms, calculations and generated/defaulted values;
- packages/containers/assets/resources and their load/override relationships;
- runtime state, persistence, caches, processes/services/workers and recovery;
- network/API/protocol/external-service behavior;
- visual/layout/component semantics plus media/audio/animation where material;
- configuration, feature flags, build/version/layer precedence;
- installation/update/relocation/portability/environment dependencies;
- timing/concurrency/performance/resource semantics when they affect behavior;
- failure/edge states, trust/authority boundaries and other hidden invariants.

A class may be `covered`, `partial`, `unresolved`, `not applicable`, or explicitly `out of scope`. The goal is visible coverage, not artificial breadth.

## Replica trait handoff

Preserve the explicit reference-to-product handoff from earlier CoreReplica versions. Before direct replica product decisions, provide a compact set of candidate traits derived from the Reference Model:

```text
trait id
observed behavior/pattern/mechanism
source Evidence / Findings / Paths
evidence kind + confidence
runtime status when material
coverage/identity/version limitation
source/use/retention/VCS/inclusion/redistribution constraint if any
```

Do not label a reference trait `must | should | could`, `done`, or `verified` as a product requirement. `corereplica-product` or the project's canonical Product Truth owner decides `adopt | adapt | reject | inspiration-only`.

## Handoff

For a reference-only request, return the best current Reference Model plus Evidence/Findings/Paths, coverage, unresolved gaps and reproducible next analysis opportunities.

If the user wants a direct replica and no stronger target project authority already exists, route to `corereplica-product` for explicit adopt/adapt/reject decisions.

If the user selects Agent Project Compiler or asks to compile the recovered knowledge into a durable project package, hand APC the corpus **without first recreating APC authorities inside CoreReplica**.
