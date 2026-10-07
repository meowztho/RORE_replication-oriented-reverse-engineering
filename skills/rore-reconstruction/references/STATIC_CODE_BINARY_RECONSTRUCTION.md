# Static Code / Binary Reconstruction

Recover likely structure from source, bytecode, native code, metadata and related artifacts.

Useful semantic capabilities include:
- function/class/module identity;
- callers/callees and xrefs;
- control/data flow;
- imports/exports/symbols/types;
- strings/constants/resources;
- state machines/validation/transforms;
- vtables/RTTI/object layouts where evidenced;
- producer/consumer and enforcement-site mapping.

A decompiler is an interpretation surface. Preserve access to lower-level facts when an important conclusion depends on it.

Use the highest useful semantic level first, but descend only as far as unresolved information requires:

```text
source / metadata
→ decompiler / IR
→ bytecode / assembly
→ raw bytes / hex
→ live memory / machine state
```

Do not descend for ceremony. Descend when the lower layer can discriminate a material hypothesis that the higher layer cannot, then reconnect the low-level fact to stable semantic anchors before promoting a Finding.

Language/runtime clues matter: Go, Rust, C++ RTTI/EH, ObjC/Swift, .NET/AOT, WASM or heavy obfuscation may require different semantics. Do not force a C-like interpretation when the runtime model contradicts it.

For a broad mechanism, search for material enforcement-site fan-out. One check found does not prove the mechanism is fully mapped.
