%define snap 20090722

%define major 0
%define libname %mklibname edit %{major}
%define libnamedevel %mklibname edit -d
%define libnamestaticdevel %mklibname edit -d -s

Summary:	Provides generic line editing functions similar to those found in GNU Readline
Name:		libedit
Version:	3.0
Release:	%mkrel 0.%{snap}.1
Epoch:		0
License:	BSD-style
Group:		System/Libraries
URL:		http://www.thrysoee.dk/editline/
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n	%{libname}
Summary:	Provides generic line editing functions similar to those found in GNU Readline
Group:		System/Libraries

%description -n	%{libname}
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n	%{libnamedevel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Requires:	ncurses-devel
Provides:	edit-devel = %{epoch}:%{version}-%{release}
Provides:	libedit-devel = %{epoch}:%{version}-%{release}
Provides:	editline = %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname edit 0 -d}
Obsoletes:	edit-devel < %{epoch}:%{version}-%{release}
Obsoletes:	editline < %{epoch}:%{version}-%{release}
Obsoletes:	libeditline0

%description -n	%{libnamedevel}
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

This package contains development files for %{name}.

%package -n	%{libnamestaticdevel}
Summary:	Static development files for %{name}
Group:		Development/C
Requires:	%{libnamedevel} = %{epoch}:%{version}-%{release}
Provides:	edit-static-devel = %{epoch}:%{version}-%{release}
Provides:	libeditline-devel = %{epoch}:%{version}-%{release}
Obsoletes:	editline-devel
Obsoletes:	libeditline-devel < %{epoch}:%{version}-%{release}
Obsoletes:	libeditline0-devel

%description -n	%{libnamestaticdevel}
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

This package contains static development files for %{name}.

%prep

%setup -q -n %{name}-%{snap}-%{version}

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}

%makeinstall_std

# Allows us to include the examples in separate %%doc directory
%{_bindir}/find examples -type f ! -name "*.c" | %{_bindir}/xargs %{__rm}
%{__rm} -r examples/.{deps,libs}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc ChangeLog INSTALL THANKS
%defattr(-,root,root,0755)
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%defattr(0644,root,root,0755)
%doc examples patches
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/libedit.pc

%files
%defattr(0644,root,root,0755)
%doc ChangeLog INSTALL THANKS
%{_mandir}/man3/*
%{_mandir}/man5/*

%files -n %{libnamestaticdevel}
%defattr(-,root,root,0755)
%{_libdir}/*.a
