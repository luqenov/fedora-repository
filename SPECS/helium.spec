Name:           helium
Version:        0.11.3.2
Release:        1%{?dist}
Summary:        Private, fast, and honest web browser

%global debug_package %{nil}
%global __strip /bin/true

License:        GPL-3.0-or-later
URL:            https://helium.computer
Source0:        https://github.com/imputnet/helium-linux/releases/download/%{version}/helium-%{version}-x86_64.AppImage

BuildRequires:  fuse-libs

Requires:       gtk3
Requires:       nss
Requires:       alsa-lib
Requires:       libXScrnSaver
Requires:       libnotify
Requires:       xdg-utils
Requires:       hicolor-icon-theme
Requires:       desktop-file-utils

%description
Helium is a private, fast, and honest web browser based on Chromium,
with built-in privacy features and a clean interface.

%prep
cp %{SOURCE0} helium.AppImage
chmod +x helium.AppImage
./helium.AppImage --appimage-extract
mv squashfs-root helium-extracted

%build
# binary pre compiled

%install
install -dm755 %{buildroot}/opt/helium
cp -r helium-extracted/opt/helium/* %{buildroot}/opt/helium/

install -dm755 %{buildroot}/usr/bin
cat > %{buildroot}/usr/bin/helium << 'EOF'
#!/bin/sh
exec /opt/helium/helium "$@"
EOF
chmod 755 %{buildroot}/usr/bin/helium

install -Dm644 helium-extracted/helium.desktop \
    %{buildroot}/usr/share/applications/helium.desktop

install -Dm644 helium-extracted/usr/share/icons/hicolor/256x256/apps/helium.png \
    %{buildroot}/usr/share/icons/hicolor/256x256/apps/helium.png

%check
# no tests available

%files
/opt/helium/
/usr/bin/helium
/usr/share/applications/helium.desktop
/usr/share/icons/hicolor/256x256/apps/helium.png

%changelog
* Tue Apr 14 2026 luqenov <luqenov@tutamail.com> - 0.11.2.1
- Update to 0.11.2.1

* Sun Apr 12 2026 luqenov <luqenov@tutamail.com> - 0.11.1.1-1
- Update to 0.11.1.1

* Sat Apr 11 2026 luqenov <luqenov@tutamail.com> - 0.10.9.1-1
- Initial RPM package of Helium browser
