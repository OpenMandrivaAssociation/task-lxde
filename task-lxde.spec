%define name    task-lxde
%define version 2009.0
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Metapackage for lxde
Group: Graphical desktop/Other
License: GPL
URL: http://lxde.org
Requires: desktop-common-data
Requires: lxde-common
Requires: lxappearance
Requires: lxterminal
Suggests: gpicview
Suggests: leafpad
Suggests: xarchiver
Suggests: lxtask
Suggests: lxrandr
Suggests: gdm
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Lightweight X11 Desktop Environment.

%files
%defattr(-,root,root)
