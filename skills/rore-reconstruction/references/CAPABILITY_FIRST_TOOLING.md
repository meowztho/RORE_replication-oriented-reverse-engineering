# Capability-First Tooling

Route from the analysis question, not from a preferred product name.

```text
question
→ required evidence boundary
→ required capability
→ available provider
```

Examples of capabilities: archive extraction, decompilation, xref/callgraph lookup, runtime hook, memory read/write/watch, DOM/runtime evaluation, packet capture, protocol decode, image measurement, engine asset parsing, database inspection.

Provider ladder:
1. existing host/project/MCP capability;
2. narrow auditable helper script;
3. alternate installed provider;
4. temporary authorized external helper when justified.

Record provider/version when it materially affects interpretation. Temporary helpers are implementation aids, not Reference Truth. Avoid building a universal tool manager.

A missing named application is not a blocker until the capability itself is unavailable.
