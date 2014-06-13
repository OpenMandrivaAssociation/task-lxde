Name:		task-lxde
Version:	%distro_release
Release:	2
Summary:	Metapackage for lxde
Group:		Graphical desktop/Other
License:	GPL
URL:		http://lxde.org
Requires:	desktop-common-data
Requires:	lxde-common
Requires:	lxappearance
Requires:	lxterminal
Suggests:	gpicview
Suggests:	leafpad
Suggests:	xarchiver
Suggests:	lxtask
Suggests:	lxrandr
#Suggests:	gdm
#Suggests:	halevt-user
Suggests:	scrot
Suggests:	xmessage
%if %mdvver >= 201100
Suggests:	networkmanager-applet
%endif
Suggests:	parcellite
Suggests:	volumeicon
Suggests:	catfish
#Suggests:	lxsession-edit
#Suggests:	lxinput
Suggests:	mdvinput
Suggests:	fskbsetting
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Lightweight X11 Desktop Environment.

%files

