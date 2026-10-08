# oocpuinfo: Sovereign CPU Architecture & Topology Engine

<div align="center">

```
================================================================================
                                oocpuinfo
          Sovereign CPU Topology, Flags & Security Mitigation Engine
================================================================================
```

**Sovereign CPU Architecture & Topology Engine**  
*Decodes CPU microarchitecture, topology hierarchy, instruction set extensions, cache geometries, and hardware vulnerability mitigations.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Streaming MCP stdio for AI agents  
Written in 100% pure native [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocpuinfo/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocpuinfo-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocpuinfo/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocpuinfo/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocpuinfo-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocpuinfo/uninstall.sh | bash
```

---

## 2. CLI Usage

```
Usage: oocpuinfo [OPTIONS]

Hardware CPU topology & instruction set inspection engine in pure native openOODA.

Options:
  -t, --topology         Display socket, core, and thread topology hierarchy
  -f, --flags            Display processor instruction set flags
  -c, --cache            Display processor cache geometry
  -u, --vulns            Display hardware vulnerability mitigations
  -a, --all              Display all sections (summary, topology, flags, vulns)
      --filter <QUERY>   Filter instruction set flags by query substring
  -d, --demo             Run in deterministic synthetic demo mode
  -j, --json             Output structured JSON
      --theme <THEME>    Select terminal color theme (ember, ocean, matrix, cyber, monochrome)
      --mcp              Run streaming MCP JSON-RPC 2.0 server on stdio
  -h, --help             Show this help message and exit
  -v, --version          Show version information and exit
```

---

## 3. Theming Integration (`oote`)

`oocpuinfo` provides rich terminal themes (`default`, `ember`, `ocean`, `matrix`, `cyber`, `monochrome`) and honors the standard `NO_COLOR` override.

```bash
oocpuinfo --theme matrix
oocpuinfo --theme ember -t
```

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocpuinfo` runs a JSON-RPC 2.0 stdio server exposing six sovereign CPU inspection tools:

* `cpuinfo_summary`: Complete CPU model, vendor, clock speed, cache, and topology overview.
* `cpuinfo_topology`: Physical sockets, cores per socket, threads per core, and logical CPU totals.
* `cpuinfo_flags`: Categorized instruction set flags (AVX-512, AMX, AES, VMX) with substring filtering.
* `cpuinfo_vulnerabilities`: Hardware vulnerability audit and mitigation statuses (Spectre, Meltdown, Retbleed, etc.).
* `cpuinfo_cache`: L1/L2/L3 cache sizing and memory hierarchy.
* `cpuinfo_demo`: Deterministic synthetic 192-core dual-socket AMD EPYC server telemetry.

```bash
oocpuinfo --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`).
* **Negative-Trust Architecture:** Sandboxed execution with zero ambient network or arbitrary write authority.
* **Hermetic Binary:** Standalone, zero-dependency compiled openOODA executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
