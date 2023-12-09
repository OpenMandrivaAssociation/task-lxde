# List of actively developed components:
#	https://wiki.lxde.org/en/Status_of_LXDE_Components

Summary:	Metapackage for LXDE Desktop Environment
Name:		task-lxde
Version:	%distro_release
Release:	2
Group:		Graphical desktop/Other
License:	GPL
URL:		https://lxde.org/
BuildArch:	noarch

Requires:	%{name}-minimal >= %{version}
Requires:	lxterminal
Requires:	lxappearance-obconf
Recommends:	lightdm
#Recommends:	lxdm
Recommends:	lxhotkey
Recommends:	lxinput
#Recommends:	lxmed (new)
Recommends:	lxmenu-data
Recommends:	lxmusic
Recommends:	lxpolkit
Recommends:	lxrandr
Recommends:	lxsession-edit
Recommends:	lxtask
Recommends:	gpicview
Recommends:	menu-cache
Recommends:	pcmanfm

Suggests:	lxcontrol
Suggests:	lxlauncher

# Apps not developed by the LXDE project
# but well integrated with it
Recommends:	catfish
# Recommends:	fskbsetting
Recommends:	leafpad
Recommends:	networkmanager-applet
Recommends:	parcellite
Recommends:	preload
# Suggests:	halevt-user
Recommends:	scrot
#Recommends:	lxscreenshot
Recommends:	volumeicon
Recommends:	xarchiver
Recommends:	xreader
Recommends:	xmessage

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LXDE, the Lightweight X11 Desktop Environment.

%files

#---------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for LXDE Desktop Environment
Group:		Graphical desktop/Other

Requires:	adwaita-gtk3-theme
Requires:	dbus-x11
Requires:	desktop-common-data
Requires:	gnome-themes-standard
Requires:	lxappearance
Requires:	lxde-common
Requires:	lxde-icon-theme
Requires:	lx-control-center
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

