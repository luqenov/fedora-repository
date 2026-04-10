Name:           bun
Version:        1.3.11
Release:        1%{?dist}
Summary:        JavaScript runtime, bundler, test runner and package manager

%global debug_package %{nil}
%global __strip /bin/true

License:        MIT
URL:            https://bun.sh
Source0:        https://github.com/oven-sh/bun/releases/download/bun-v%{version}/bun-linux-x64.zip

BuildRequires:  unzip

%description
Bun is an all-in-one JavaScript runtime built for speed, with a bundler,
test runner, and Node.js-compatible package manager.

%prep
unzip -o %{SOURCE0} -d bun-bin

%build
# pass

%install
install -dm755 %{buildroot}/usr/bin
install -Dm755 bun-bin/bun-linux-x64/bun %{buildroot}/usr/bin/bun

%check
# no tests available

%files
/usr/bin/bun

%changelog
* Fri Apr 10 2026 luqenov <luqenov@tutamail.com> - 1.3.11-1
- Initial RPM package of Bun
