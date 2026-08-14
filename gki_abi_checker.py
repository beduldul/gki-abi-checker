#!/usr/bin/env python3
"""
Android GKI ABI Compatibility Checker Utility
"""

import sys
import os

REQUIRED_CONFIGS = {
    "CONFIG_SLUB_DEBUG": "y",
    "CONFIG_UNMAP_KERNEL_AT_EL0": "y",
}

def check_defconfig(config_path):
    print(f"[*] Auditing GKI ABI Configuration: {config_path}")
    if not os.path.exists(config_path):
        print(f"[!] Error: File {config_path} does not exist.")
        sys.exit(1)

    configs = {}
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split('=', 1)
                if len(parts) == 2:
                    configs[parts[0]] = parts[1]

    passed = True
    for key, val in REQUIRED_CONFIGS.items():
        if key in configs and configs[key] == val:
            print(f"  [✓] {key}={val} (GKI ABI Preserved)")
        else:
            print(f"  [✗] {key} is missing or not set to {val}! (ABI Breakage Risk)")
            passed = False

    if passed:
        print("\n[+] Result: Kernel defconfig passes GKI ABI verification.")
    else:
        print("\n[-] Result: Defconfig contains ABI incompatibilities that may cause bootloops.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 gki_abi_checker.py <defconfig_file>")
        sys.exit(1)
    check_defconfig(sys.argv[1])
