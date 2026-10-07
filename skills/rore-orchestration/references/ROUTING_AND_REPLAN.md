# Routing and Replan

## Method routing

Route from the unresolved fact and needed evidence boundary. Target/product domain only narrows applicable surfaces; it does not select a privileged workflow. Domain-specific rows below are conditional profiles, not owners.

| Knowledge gap / evidence need | JIT method under `rore-reconstruction` |
| --- | --- |
| screens/views, navigation, states, UI component relationships | `SURFACE_FLOW_STATE_RECONSTRUCTION.md` |
| layout, visual hierarchy, interaction/motion/media semantics | `VISUAL_INTERACTION_RECONSTRUCTION.md` |
| archive/package/container/resources/embedded artifacts | `ARTIFACT_EXTRACTION.md` |
| functions/classes/control/data flow/binary structure | `STATIC_CODE_BINARY_RECONSTRUCTION.md` |
| effective running behavior, process/files/network/persistence/timing | `RUNTIME_DYNAMIC_RECONSTRUCTION.md` |
| live values/objects, readers/writers, authoritative state | `MEMORY_STATE_CAUSALITY.md` |
| browser/client/HTTP surfaces when present | `WEB_JS_API_RECONSTRUCTION.md` (conditional profile) |
| unknown messages/framing/state machine/serialization | `PROTOCOL_RECONSTRUCTION.md` |
| schemas/records/formats/defaults/relationships | `DATA_SCHEMA_FORMAT_RECONSTRUCTION.md` |
| mobile/platform packaging/runtime semantics when present | `MOBILE_PLATFORM_RECONSTRUCTION.md` (conditional profile) |
| engine/asset-heavy runtime semantics when present (games are one example) | `GAME_ENGINE_ASSET_RECONSTRUCTION.md` (conditional profile) |
| changed builds/patches/version migration | `CROSS_VERSION_DIFFERENTIAL_RECONSTRUCTION.md` |
| formulas/state rules/cooldowns/economy/balancing | `MECHANICS_RULES_BALANCING_RECONSTRUCTION.md` |
| docs/source/history/reviews/community clues | `EXTERNAL_VERSION_RESEARCH.md` |
| hidden contract only exposed by deliberate variation | `PERTURBATION_AND_CAUSAL_PROBING.md` |

Several methods may cooperate, but use the smallest active set that can discriminate the current hypotheses.

## Stage-exit contract

At the end of a meaningful analysis unit record:

```text
current hypothesis
supporting Evidence IDs
contradicting / negative Evidence IDs
confidence / boundary
next decision: continue | switch | stop
reason
```

`stop` means the current requested mechanism/coverage is sufficiently understood or further progress is genuinely blocked/low-value. It does not mean every possible analysis technique was exhausted.

## Deadlock and bias

Trigger a replan when, as a practical default, roughly three analysis actions yield no new evidence or two method switches merely bounce between the same unresolved assumptions. These numbers are heuristics, not a rigid counter.

On replan:
1. restate the unresolved claim;
2. enumerate the competing explanations;
3. name what observation would discriminate them;
4. challenge whether the current tool/method can actually observe it;
5. change anchor, evidence boundary or capability — not just command syntax.

Bias warnings: one decompiler treated as truth, runtime symptoms without stable anchors, screenshot-only claims about temporal behavior, repeated parsing without identity proof, or repeated web research replacing target-local checks.
