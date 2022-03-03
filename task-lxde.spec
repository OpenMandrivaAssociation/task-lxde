# List of actively developed components:
#	https://wiki.lxde.org/en/Status_of_LXDE_Components

Summary:	Metapackage for LXDE Desktop Environment
Name:		task-lxde
Version:	%distro_release
Release:	1
Group:		Graphical desktop/Other
License:	GPL
URL:		https://lxde.org/
BuildArch:	noarch

Requires:	%{name}-minimal >= %{version}
Requires:	lxterminal
Requires:	lxappearance-obconf

Recommends:	lightdm #lxdm
#Recommends:	lxhotkey (new)
Recommends:	lxinput
#Recommends:	lxmed (new)
Recommends:	lxmenu-data
Recommends:	lxmusic
Recommends:	lxpolkit
Recommends:	lxrandr
Recommends:	lxsession-edit
Recommends:	lxtask
Recommends:	pcmanfm

Suggests:	lxcontrol
Suggests:	lxlauncher

# Apps not developed by the LXDE project
# but well integrated with it
Recommends:	gpicview
Recommends:	leafpad
Recommends:	preload
Recommends:	xarchiver
Recommends:	xmessage
# Suggests:	halevt-user
Recommends:	scrot # lxscreenshot
Recommends:	menu-cache
Recommends:	networkmanager-applet
Recommends:	parcellite
Recommends:	volumeicon
Recommends:	catfish
# Recommends:	mdvinput
# Recommends:	fskbsetting
Recommends:	xreader #new

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LXDE, the Lightweight X11 Desktop Environment.

%files

#---------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for LXDE Desktop Environment
Group:		Graphical desktop/Other

Requires:	adwaita-gtk2-theme
Requires:	dbus-x11
Requires:	drakconf
Requires:	desktop-common-data
Requires:	gnome-themes-standard
Requires:	lxappearance
Requires:	lxde-common
Requires:	lxde-icon-theme
#Requires:	lx-control-center# FIXME: missing
Requires:	lxpanel
Requires:	lxsession
Requires:	obconf
Requires:	preload
Requires:	task-pulseaudio
Requires:	task-x11

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal LXDE, the Lightweight X11
Desktop Environment.

%files minimal

#---------------------------------------------------------------------------

%build
# Nothing to do here

%install
# Nothing to do here

