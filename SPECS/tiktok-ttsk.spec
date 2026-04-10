%global __strip /bin/true
%global __brp_strip /bin/true
%global __brp_strip_static_archive /bin/true
%global __brp_strip_comment_note /bin/true
%global __brp_mangle_shebangs /bin/true
%global __brp_check_rpaths /bin/true
%global __brp_python_bytecompile /bin/true

%global __brp_add_determinism /bin/true
%global _add_determinism_brp 0

%global _enable_debug_package 0
%global debug_package %{nil}

Name:           tiktok-ttsk
Version:        1.0.0
Release:        3%{?dist}

Summary:        Set the TikTok chat streak ON using Python
License:        GPL-3.0-or-later
URL:            https://github.com/Kameil/tiktok-ttsk
Source0:        https://github.com/Kameil/tiktok-ttsk/releases/download/1.0.0/tiktok-ttsk.bin

BuildArch:      x86_64
ExclusiveArch:  x86_64

%description
TTSK (TikTok Streak Keeper) is a Python tool that automatically maintains your TikTok conversation streaks by sending a message to your active chats once per day. Compiled with Nuitka as a standalone binary.

%prep
# already compiled

%build
# already compiled

%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/tiktok-ttsk

%files
%{_bindir}/tiktok-ttsk

%changelog
* Fri Apr 03 2026 luqenov <luqenov@tutamail.com> - 1.0.0-3
- Disabled add-determinism which was corrupting the Nuitka onefile payload
- Disabled more BRP macros