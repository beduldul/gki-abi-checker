# Android GKI ABI Compatibility Verification Utility v1.1.0

A command-line verification utility designed for Android GKI (Google Kernel Image) kernel developers to inspect kernel `.config` files and source definitions for GKI ABI compatibility and symbol safety.

---

## 🛠 Features in v1.1.0

- **GKI Memory Structure Validation**: Checks mandatory flags like `CONFIG_SLUB_DEBUG=y` to prevent `struct page` layout shifts and instant bootloops.
- **Networking & Scheduler Audit**: Verifies `CONFIG_NET_SCH_FQ` and `CONFIG_TCP_CONG_BBR` configuration.
- **Performance Recommendations**: Audits `CONFIG_LTO_CLANG_THIN` and `CONFIG_UCLAMP_TASK`.
- **JSON Audit Reports**: Generates `--json` reports (`abi_report.json`) for CI/CD integration.

---

## 💻 Usage

```bash
python3 gki_abi_checker.py path/to/kernel/.config --json
```

---

## 📄 License
MIT License
