# Mobile / Platform Reconstruction

Use when APK/IPA/mobile runtime or platform packaging materially shapes the reference.

Combine as applicable:
- package/manifest/entitlement/permission inventory;
- Java/Kotlin/Swift/ObjC/native library static analysis;
- resources/layout/assets;
- component/lifecycle/IPC/deep-link relationships;
- runtime observation and hooks;
- network/API behavior;
- persistent storage/keychain/preferences/databases;
- native `.so`/framework handoff to static/runtime analysis.

Rebuild/re-sign/reinstall or hook an authorized local copy only when the intervention is needed to test a reconstruction hypothesis. A bypass technique is not itself a RORE goal; use the smallest intervention that reveals hidden behavior or enables observation, then record the changed boundary.

Separate platform/framework behavior from application-specific findings.
