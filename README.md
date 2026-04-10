# Fedora Repository

A third-party RPM binary package repository.

## Setup

> [!NOTE]
> You can find all packages [here](https://copr.fedorainfracloud.org/coprs/luqenov/)

Add the repo:

```sh
sudo dnf copr enable luqenov/<package>
```

Install a package:

```sh
sudo dnf install <package>
```

Updates come through normally with:

```sh
sudo dnf upgrade -y
```