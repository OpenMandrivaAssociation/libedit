%define snap 20110802

%define major 0
%define libname %mklibname edit %{major}
%define libnamedevel %mklibname edit -d

Summary:	Provides generic line editing functions similar to those found in GNU Readline
Name:		libedit
Version:	3.0
Release:	0.%{snap}.1
Epoch:		0
License:	BSD-style
Group:		System/Libraries
URL:		http://www.thrysoee.dk/editline/
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:	ncurses-devel >= 5.9

%description
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n	%{libname}
Summary:	Provides generic line editing functions similar to those found in GNU Readline
Group:		System/Libraries
Conflicts:	libedit

%description -n	%{libname}
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n	%{libnamedevel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} >= %{epoch}:%{version}-%{release}
Requires:	ncurses-devel
Provides:	edit-devel = %{epoch}:%{version}-%{release}
Provides:	libedit-devel = %{epoch}:%{version}-%{release}
Provides:	editline = %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname edit 0 -d}
Obsoletes:	edit-devel < %{epoch}:%{version}-%{release}
Obsoletes:	editline < %{epoch}:%{version}-%{release}
Obsoletes:	libeditline0
Conflicts:	libedit

%description -n	%{libnamedevel}
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

This package contains development files for %{name}.

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

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

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
