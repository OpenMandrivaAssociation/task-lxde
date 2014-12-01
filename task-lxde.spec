Name:		task-lxde
Version:	2014.0
Release:	2.1
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
Requires:	lxpolkit
Suggests:	fskbsetting
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Lightweight X11 Desktop Environment.

%files

