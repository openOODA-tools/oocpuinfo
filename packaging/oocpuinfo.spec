Name:           oocpuinfo
Version:        0.2.0
Release:        1%{?dist}
Summary:        Decodes CPU microarchitecture, flags (AVX512, AES, etc.), cache sizes, and bugs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocpuinfo
Source0:        oocpuinfo-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocpuinfo is a sovereign, capability-bounded CPU TOPOLOGY & INSTRUCTION SET INSPECTOR
written in pure openOODA, featuring zero ambient authority, oote color themes,
hardware vulnerability audits, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocpuinfo
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocpuinfo-uninstall

%files
/usr/bin/oocpuinfo
/usr/bin/oocpuinfo-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA implementation with CPU topology and MCP surface
