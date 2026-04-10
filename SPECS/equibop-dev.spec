Name:           equibop-dev
Version:        0.0.0.20260407
Release:        1%{?dist}
Summary:        Custom Discord App (dev branch)

%global _gitcommit b8d7a11614648dd752fe0289c5fba247f2d8c235
%global _electronver 35
%global __strip /bin/true
%global _builddir_name Equibop-%{_gitcommit}
%global debug_package %{nil}
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-strip[[:space:]].*$!!g')

License:        GPL-3.0-or-later
URL:            https://github.com/Equicord/Equibop
Source0:        https://github.com/Equicord/Equibop/archive/%{_gitcommit}.tar.gz
Source1:        equibop.sh
Source2:        equibop.desktop

# hostmakedepends
BuildRequires:  gcc
BuildRequires:  nodejs
BuildRequires:  python3
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  bun
BuildRequires:  nodejs-devel
BuildRequires:  gcc-c++

# depends
Requires:       electron%{_electronver}
Requires:       hicolor-icon-theme
Requires:       desktop-file-utils

Provides:       equibop = %{version}-%{release}
Conflicts:      equibop >= 0

%description
Equibop is a custom Discord desktop app based on Vesktop,
built from the dev branch of Equicord.

%prep
%autosetup -n %{_builddir_name}
cp %{SOURCE1} equibop.sh
cp %{SOURCE2} equibop.desktop

%build
sed -i "s|execSync(\"git rev-parse HEAD\", { encoding: \"utf-8\" }).trim()|\"${_gitcommit}\"|" \
    scripts/build/build.mts

export SKIP_BUN_DOWNLOAD=true
export npm_config_nodedir=/usr
CI=true bun install
bun run buildLibVesktop
bun run package:dir

%install
install -dm755 %{buildroot}/usr/lib/equibop

install -Dm644 dist/linux-unpacked/resources/app.asar \
    %{buildroot}/usr/lib/equibop/app.asar

install -Dm644 dist/linux-unpacked/resources/app-update.yml \
    %{buildroot}/usr/lib/equibop/app-update.yml

cp -r dist/linux-unpacked/resources/arrpc \
    %{buildroot}/usr/lib/equibop/

install -Dm755 equibop.sh %{buildroot}/usr/bin/equibop

install -Dm644 equibop.desktop \
    %{buildroot}/usr/share/applications/equibop.desktop

install -Dm644 static/icon.png \
    %{buildroot}/usr/share/pixmaps/equibop.png

install -Dm644 build/icon.svg \
    %{buildroot}/usr/share/icons/hicolor/scalable/apps/equibop.svg

%check
# no tests available

%files
%license LICENSE
/usr/lib/equibop/
/usr/bin/equibop
/usr/share/applications/equibop.desktop
/usr/share/pixmaps/equibop.png
/usr/share/icons/hicolor/scalable/apps/equibop.svg

%changelog
* Tue Apr 07 2026 luqenov <luqenov@tutamail.com> - 0.0.0.20260407-1
- Initial RPM package (ported from Void Linux template)
