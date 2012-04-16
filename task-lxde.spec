Name:		task-lxde
Version:	201100
Release:	%mkrel 11
Summary:	Metapackage for lxde
Group:		Graphical desktop/Other
License:	GPL
URL:		http://lxde.org
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

Requires: desktop-common-data
Requires: lxde-common
Requires: lxappearance
Requires: lxterminal

Suggests: gpicview
Suggests: leafpad
Suggests: xarchiver
Suggests: lxtask
Suggests: lxrandr
Suggests: scrot
Suggests: xmessage
Suggests: networkmanager-applet
Suggests: parcellite
Suggests: volumeicon
Suggests: catfish
Suggests: mdvinput
Suggests: fskbsetting

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Lightweight X11 Desktop Environment.

%files
%defattr(-,root,root)
