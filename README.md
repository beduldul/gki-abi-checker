# Android GKI ABI Compatibility Verification Utility

A command-line verification utility designed for Android GKI (Google Kernel Image) kernel developers to inspect kernel `.config` files and source definitions for GKI ABI compatibility and symbol safety.

---

## 🛠 Features

- **GKI Memory Structure Validation**: Checks mandatory flags like `CONFIG_SLUB_DEBUG=y` to prevent `struct page` layout shifts.
- **Symbol Export Verification**: Audits required symbol exports such as `__stack_chk_guard`.
- **CFI & Version Check Audit**: Inspects Control Flow Integrity (CFI) trap handler configurations and module version CRC checks.

---

## 💻 Usage

```bash
python3 gki_abi_checker.py path/to/kernel/.config
```

---

## 📄 License
MIT License
