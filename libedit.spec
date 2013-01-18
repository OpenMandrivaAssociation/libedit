%define snap 20110802

%define major 0
%define libname %mklibname edit %{major}
%define libnamedevel %mklibname edit -d

Summary:	Provides generic line editing functions similar to those found in GNU Readline
Name:		libedit
Version:	3.0
Release:	0.%{snap}.2
Epoch:		0
License:	BSD-style
Group:		System/Libraries
URL:		http://www.thrysoee.dk/editline/
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:	pkgconfig(ncurses) >= 5.9

%description
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n	%{libname}
Summary:	Provides generic line editing functions similar to those found in GNU Readline
Group:		System/Libraries
Conflicts:	libedit < %{EVRD}

%description -n	%{libname}
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n	%{libnamedevel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(ncurses)
Provides:	edit-devel = %{EVRD}
Provides:	libedit-devel = %{EVRD}
Provides:	editline = %{EVRD}
Conflicts:	libedit < %{EVRD}

%description -n	%{libnamedevel}
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

This package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{snap}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# Allows us to include the examples in separate %%doc directory
find examples -type f ! -name "*.c" | %{_bindir}/xargs %__rm
%__rm -r examples/.{deps,libs}

%files -n %{libname}
%doc ChangeLog INSTALL THANKS
%{_libdir}/*.so.%{major}*
%{_mandir}/man5/*

%files -n %{libnamedevel}
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libedit.pc
%{_mandir}/man3/*


%changelog
* Sun Dec 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0:3.0-0.20110802.1
+ Revision: 737602
- new snap (20110802)
- fix deps
- drop the static lib, its sub package and the libtool *.la file
- drop the useless libedit package containing only manpages (wtf?)
- various fixes

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0:3.0-0.20090923.3
+ Revision: 660243
- mass rebuild

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0:3.0-0.20090923.2mdv2011.0
+ Revision: 601043
- rebuild

* Sat Mar 20 2010 Emmanuel Andry <eandry@mandriva.org> 0:3.0-0.20090923.1mdv2010.1
+ Revision: 525477
- New version 3.0-0.20090923

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0:3.0-0.20090722.2mdv2010.1
+ Revision: 520140
- rebuilt for 2010.1

* Thu Jul 30 2009 Emmanuel Andry <eandry@mandriva.org> 0:3.0-0.20090722.1mdv2010.0
+ Revision: 404793
- New version 3.0
- check major

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0:2.11-0.20080712.2mdv2009.1
+ Revision: 315552
- rebuild

* Sat Jul 12 2008 Oden Eriksson <oeriksson@mandriva.com> 0:2.11-0.20080712.1mdv2009.0
+ Revision: 234156
- 20080712-2.11

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0:2.10-0.20070831.3mdv2009.0
+ Revision: 209486
- rebuilt with gcc43

* Thu Apr 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0:2.10-0.20070831.2mdv2009.0
+ Revision: 195086
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0:2.10-0.20070831.1mdv2008.1
+ Revision: 128553
- kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 David Walluck <walluck@mandriva.org> 0:2.10-0.20070831.1mdv2008.0
+ Revision: 76614
- Editline 20070831-2.10

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 0:2.10-0.20070813.3mdv2008.0
+ Revision: 68535
- split man into separated pkg to allow biarch
- obsoletes editline, which is same things

* Thu Aug 16 2007 Funda Wang <fwang@mandriva.org> 0:2.10-0.20070813.2mdv2008.0
+ Revision: 64116
- Obsoletes old devel

* Tue Aug 14 2007 David Walluck <walluck@mandriva.org> 0:2.10-0.20070813.1mdv2008.0
+ Revision: 62856
- 20070813-2.10
- update to new lib policy
- add static-devel package
- no more need for manpage fix
- remove executable permissions on scripts in %%doc


* Mon Mar 12 2007 David Walluck <walluck@mandriva.org> 0:2.10-0.20070302.1mdv2007.1
+ Revision: 141588
- 20070302-2.10

* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0:2.9-0.20060603.2mdv2007.1
+ Revision: 93749
- Import libedit

* Mon Jun 05 2006 David Walluck <walluck@mandriva.org> 0:2.9-0.20060213.2mdv2007.0
- 20060603

* Tue Feb 21 2006 David Walluck <walluck@mandriva.org> 0:2.9-0.20060213.1mdk
- 20060213

* Fri Feb 10 2006 David Walluck <walluck@mandriva.org> 0:2.9-0.20060103.1mdk
- 20060103
- add Requires(post{,un}): /sbin/ldconfig
- add Provides: %%{_lib}edit-devel

* Sun Oct 23 2005 David Walluck <walluck@mandriva.org> 0:2.9-0.20051022.1mdk
- 20051022
- update summary
- change license from BSD to BSD-style
- remove unnecessary BuildRequires
- %%version=%%release -> %%{version}-%%{release}
- use %%make and %%makeinstall
- no need to test %%{buildroot} = "/"
- add patches to devel docs

* Fri Jun 03 2005 David Walluck <walluck@mandriva.org> 2.9-0.20050601.1mdk
- 20050601

* Sun May 08 2005 Olivier Thauvin <nanardon@mandriva.org> 2.9-0.20041127.4mdk
- fix specfile

* Sun Jan 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20041127.3mdk
- drop the readline-devel conflict as it brought circular dependencies hell

* Mon Jan 03 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20041127.2mdk
- add a conflict on readline-devel, as this one seems to be picked up first 
  if installed, when for example building postgresql, honeyd, etc.

* Tue Nov 30 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20041127.1mdk
- 20041127

* Mon Nov 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20041014.1mdk
- 20041014
- drop P0, it's implemented upstream

* Sat Sep 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20040908.2mdk
- fix funny naming

* Sat Sep 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20040908.1mdk
- hack the soname

* Sat Sep 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20040908.3mdk
- fix one conflicting manpage with readline-devel

* Sat Sep 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20040908.2mdk
- make it compile on 10.0 too

* Sat Sep 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9-0.20040908.1mdk
- initial mandrake package

