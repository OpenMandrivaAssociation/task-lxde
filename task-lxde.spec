%define name    task-lxde
%define version 201100
%define release 14

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
#Suggests: gdm
#Suggests: halevt-user
Suggests: scrot
Suggests: xmessage
%if %mdvver >= 201100
Suggests: networkmanager-applet
%endif
Suggests: parcellite
Suggests: volumeicon
Suggests: catfish
#Suggests: lxsession-edit
#Suggests: lxinput
Suggests: mdvinput
Suggests: fskbsetting
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Lightweight X11 Desktop Environment.

%files
%defattr(-,root,root)


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 201100-10mdv2011.0
+ Revision: 693018
- remove lxsession-edit and lxinput and adding mdvinput
- remove suggests for halevt-user due double work with GIO open

* Mon Jul 04 2011 Александр Казанцев <kazancas@mandriva.org> 201100-8
+ Revision: 688694
- add scrot for suggests
- SILEN avoid mdvver error

* Sun Jun 26 2011 Александр Казанцев <kazancas@mandriva.org> 201100-6
+ Revision: 687256
- fix suggested nm-applet for mdvver >= 201100
- fix version for backports needs

* Sat Jun 18 2011 Александр Казанцев <kazancas@mandriva.org> 2011.0-4
+ Revision: 685906
- Update suggests. Add lxinput, lxsession-edit and fskbsetting

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 2011.0-3
+ Revision: 684428
- add search tools catfish

* Fri Apr 29 2011 Александр Казанцев <kazancas@mandriva.org> 2011.0-2
+ Revision: 660759
-add suggested package for networkmanager applet and clipboard manager

* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1
+ Revision: 655953
- bump to 2011 release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-3mdv2011.0
+ Revision: 607978
- rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add Suggests on xmessages
      CCBUG: 60964

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-2mdv2010.1
+ Revision: 524165
- rebuilt for 2010.1

* Wed Oct 21 2009 Olivier Blin <blino@mandriva.org> 2010.0-1mdv2010.0
+ Revision: 458497
- 2010.0
- suggest halevt-user for USB keys automount

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-8mdv2010.0
+ Revision: 423762
- rebuild

* Mon Mar 09 2009 Anne Nicolas <ennael@mandriva.org> 2009.0-7mdv2009.1
+ Revision: 353232
- clean spec file
  add gdm suggests

* Tue Nov 04 2008 Funda Wang <fwang@mandriva.org> 2009.0-6mdv2009.1
+ Revision: 299952
- require lxterminal for the icon on the launch bar

* Tue Oct 28 2008 Funda Wang <fwang@mandriva.org> 2009.0-5mdv2009.1
+ Revision: 297797
- change some requires to suggests

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 2009.0-4mdv2009.0
+ Revision: 289153
- suggest randr
- change lxtask to suggest

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-3mdv2009.0
+ Revision: 269406
- rebuild early 2009.0 package (before pixel changes)

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 2009.0-2mdv2009.0
+ Revision: 200942
- do not require lxnm by default (use our own drakx-net instead)

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 200898
- add spec file
- Created package structure for task-lxde.

