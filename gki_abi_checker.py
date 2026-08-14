#!/usr/bin/env python3
"""
Android GKI ABI Compatibility Checker Utility v1.1.0
"""

import sys
import os
import argparse
import json

REQUIRED_CONFIGS = {
    "CONFIG_SLUB_DEBUG": "y",
    "CONFIG_UNMAP_KERNEL_AT_EL0": "y",
    "CONFIG_NET_SCH_FQ": "y",
    "CONFIG_TCP_CONG_BBR": "y"
}

RECOMMENDED_CONFIGS = {
    "CONFIG_LTO_CLANG_THIN": "y",
    "CONFIG_UCLAMP_TASK": "y"
}

def check_defconfig(config_path, json_export=False):
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

    report = {"mandatory": {}, "recommended": {}, "passed": True}
    passed = True

    print("\n--- Mandatory GKI ABI Configs ---")
    for key, val in REQUIRED_CONFIGS.items():
        is_ok = key in configs and configs[key] == val
        report["mandatory"][key] = is_ok
        if is_ok:
            print(f"  [✓] {key}={val} (GKI ABI Preserved)")
        else:
            print(f"  [✗] {key} is missing or not set to {val}! (ABI Breakage / Bootloop Risk)")
            passed = False

    print("\n--- Recommended Performance Configs ---")
    for key, val in RECOMMENDED_CONFIGS.items():
        is_ok = key in configs and configs[key] == val
        report["recommended"][key] = is_ok
        if is_ok:
            print(f"  [✓] {key}={val} (Performance Tuned)")
        else:
            print(f"  [!] {key} not set to {val} (Optional Performance Boost)")

    report["passed"] = passed

    if json_export:
        with open("abi_report.json", "w") as jf:
            json.dump(report, jf, indent=2)
        print("\n[+] Audit report exported to -> abi_report.json")

    if passed:
        print("\n[+] Result: Kernel defconfig passes GKI ABI verification.")
    else:
        print("\n[-] Result: Defconfig contains ABI incompatibilities that may cause bootloops.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Android GKI ABI Compatibility Checker Utility v1.1.0")
    parser.add_argument("defconfig", help="Path to kernel defconfig file")
    parser.add_argument("--json", action="store_true", help="Export audit report as JSON")
    args = parser.parse_args()

    check_defconfig(args.defconfig, args.json)
