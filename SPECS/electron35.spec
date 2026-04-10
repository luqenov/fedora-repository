Name:           electron35
Version:        35.2.0
Release:        1%{?dist}
Summary:        Cross-platform desktop application framework (v35)

%global debug_package %{nil}
%global __strip /bin/true

License:        MIT and BSD and Apache-2.0
URL:            https://electronjs.org
Source0:        https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-linux-x64.zip

BuildRequires:  unzip

Requires:       gtk3
Requires:       nss
Requires:       alsa-lib
Requires:       libXScrnSaver
Requires:       libnotify
Requires:       libXtst
Requires:       xdg-utils

%description
Electron is a framework for building cross-platform desktop applications
using web technologies. This package provides version 35.

%prep
unzip -o %{SOURCE0} -d electron35-bin

%build

%install
install -dm755 %{buildroot}/usr/lib/electron35
cp -r electron35-bin/* %{buildroot}/usr/lib/electron35/

install -dm755 %{buildroot}/usr/bin
cat > %{buildroot}/usr/bin/electron35 << 'EOF'
#!/bin/sh
exec /usr/lib/electron35/electron "$@"
EOF
chmod 755 %{buildroot}/usr/bin/electron35

%check
# no tests available

%files
/usr/lib/electron35/
/usr/bin/electron35

%changelog
* Thu Apr 09 2026 luqenov <luqenov@tutamail.com> - 35.2.0-1
- Initial RPM package of Electron 35
