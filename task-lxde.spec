Name: task-lxde
Version: 2009.0
Release: %mkrel 3
Summary: Metapackage for lxde
Group: Graphical desktop/Other
License: GPL
Requires: desktop-common-data
Requires: lxde-common
Requires: lxappearance
Requires: lxtask
Requires: gpicview
Requires: leafpad
Requires: xarchiver
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Lightweight X11 Desktop Environment.

%files
%defattr(-,root,root-)
