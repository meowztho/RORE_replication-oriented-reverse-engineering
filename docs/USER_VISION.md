# CoreReplica User Vision

## Product intent

CoreReplica is a provider-neutral **reference reverse-engineering and reconstruction plugin**. Its primary responsibility is to discover how an authorized software product, website, game, package, data format, service, workflow or system works and convert that discovery into a qualified, reproducible and usable reference corpus.

It should actively recover useful information rather than stop at surface observation: inventory artifacts and surfaces; extract/decompress/decode/decompile when useful and authorized; inspect structures and data; observe and, when material, actively corroborate runtime-sensitive claims against the effective running target; correlate static and dynamic evidence; recover algorithms, entities, formats, assets, dependencies and causal paths; and preserve unknowns instead of guessing.

When the user also wants an independent replica, CoreReplica may define minimal target decisions and implement/verify the replica through canonical project/workspace owners. If Agent Project Compiler is selected, APC owns durable project compilation from the reference corpus plus user intent; CoreReplica does not duplicate APC System Map/Plan/Acceptance/Blueprint authorities.

The plugin should feel like Core-First discipline applied to reverse engineering and reference-driven replication: small routing kernel, detailed procedures JIT, one responsibility owner, maximum useful evidence, claims bounded by evidence, no parallel truth, and explicit correction/release boundaries.

## Desired outcomes

A capable fresh agent using CoreReplica should be able to:

- classify the target and analysis surfaces before choosing tools;
- discover actual available tools/providers instead of guessing paths or capabilities;
- inventory the reference broadly enough to expose useful analysis branches;
- extract, unpack, decode, decompress or decompile authorized material when this increases recoverable knowledge;
- combine static artifact analysis with targeted dynamic/runtime corroboration where either alone is incomplete;
- avoid forcing a launch for static-only claims while refusing to present runtime-sensitive static inference as runtime-verified;
- distinguish packaged presence/reference from runtime reachability, exercised use and effective behavior;
- keep raw evidence, derived artifacts, Findings and causal/call/data/runtime Paths distinguishable;
- qualify object identity, parser correctness, coverage, source-layer precedence and corroboration;
- reconstruct a usable model of behavior, data, flows, algorithms, assets, interfaces and unresolved gaps;
- challenge broad reconstruction coverage across material knowledge classes instead of silently dropping UI/flow, runtime, install/update, failure, timing or trust-boundary knowledge;
- preserve a compact reference-trait handoff for direct replica Product Truth decisions;
- preserve source/evidence provenance plus retention/VCS/inclusion/redistribution constraints;
- hand a structured reference corpus to APC when durable project compilation is requested;
- separate reference knowledge from target product decisions;
- implement an independent replica through existing canonical project/workspace owners when requested;
- verify the actual replica outcome on the closest practical boundary;
- continue after context loss by rediscovering current workspace/reference truth and loading only the required procedures.

## Non-goals

CoreReplica is not:

- a second Agent Project Compiler or general project-authority compiler;
- a universal exploit/pentest/red-team framework;
- a requirement to perform every possible reverse-engineering technique on every target;
- a universal parser/decompiler implementation or tool installer;
- a bypass/credential-harvesting/unauthorized-acquisition or unauthorized-redistribution framework;
- a replacement for Core-First Governance;
- a second architecture owner;
- a general test runner, deployment platform or legal compliance engine;
- an acceptance system that trusts builder self-report;
- a mandatory fixed-stage pipeline.
