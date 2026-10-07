# Reference Reconstruction: <target / slice>

## Target identity
- target:
- version/build/revision/hash:
- platform/runtime/engine/environment:
- observation date/range:
- authorized analysis boundary:

## Sources / evidence fixity
| Evidence ID | boundary | source/artifact | identity/hash | method | limitations |
| --- | --- | --- | --- | --- | --- |

## Stable reference identities
Create only the tables that exist for this target.

### Surfaces (`SUR-###`)
| ID | identity/purpose | reachability | states | evidence | notes |
| --- | --- | --- | --- | --- | --- |

### Flows (`FLOW-###`)
| ID | goal/path | states/surfaces | edge conditions | evidence | unknown edges |
| --- | --- | --- | --- | --- | --- |

### Components / subsystems (`COMP-###`)
| ID | observed responsibility | relationships | evidence | confidence/limitations |
| --- | --- | --- | --- | --- |

### Entities / schemas (`ENT-###`)
| ID | fields/relationships | source/canonicality evidence | evidence | limitations |
| --- | --- | --- | --- | --- |

### Protocol messages (`PROTO-###`)
| ID | direction/type | fields/framing | state transition | evidence | unknowns |
| --- | --- | --- | --- | --- | --- |

## Findings
| Finding ID | conclusion | evidence IDs | status | boundary | contradictions/limitations |
| --- | --- | --- | --- | --- | --- |

## Paths
| Path ID | type | ordered steps/edges | evidence/findings | unknown edges |
| --- | --- | --- | --- | --- |

Suggested path types: `user`, `call`, `data`, `runtime`, `causal`, `protocol`, `load`, `persistence`.

## Reference-native models
Use one or more sections as the reference demands: State Model, Component/Architecture Model, Data Model, Protocol Model, Causal Model, Asset/Resource Model, Mechanics Model, Timing/Concurrency Model, Failure/Recovery Model.

Do not merge them merely for compactness when separate views preserve important structure.

## Hypotheses and negative evidence
| hypothesis | status | supporting evidence | contradicting/negative evidence | next discriminator |
| --- | --- | --- | --- | --- |

## Runtime status
For material runtime claims, distinguish `PRESENT | REFERENCED | REACHABLE | EXERCISED | EFFECTIVE` or record why the ladder is not applicable.

## Coverage
Use `covered | partial | unresolved | not_applicable | out_of_scope`.

| class | status | evidence / gap |
| --- | --- | --- |
| surface / flow / state | |
| architecture / components / paths | |
| data / schema / content population | |
| algorithms / transforms | |
| packages / assets / resources / layering | |
| runtime / persistence / recovery | |
| memory / state / causality | |
| web / API / protocol | |
| visual / interaction / media | |
| mechanics / rules / balancing | |
| config / flags / version / precedence | |
| install / update / environment | |
| timing / concurrency / resources | |
| failures / limits / trust boundaries | |

## Open questions / next high-information probes
