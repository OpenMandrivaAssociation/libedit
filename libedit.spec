%define snap 20140213
%define major	0
%define libname %mklibname edit %{major}
%define devname %mklibname edit -d

Summary:	Provides generic line editing functions similar to those found in GNU Readline

Name:		libedit
Version:	3.1
Release:	0.%{snap}
License:	BSD-style
Group:		System/Libraries
Url:		http://www.thrysoee.dk/editline/
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:	pkgconfig(ncursesw) >= 5.9

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

%package -n	%{devname}
Summary:	Development files for %{name}

Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	libedit < %{EVRD}

%description -n	%{devname}
This package contains development files for %{name}.

%prep
%setup -qn %{name}-%{snap}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# Allows us to include the examples in separate %%doc directory
find examples -type f ! -name "*.c" | %{_bindir}/xargs rm
rm -r examples/.libs

%files -n %{libname}
%{_libdir}/libedit.so.%{major}*

%files -n %{devname}
%doc examples
%doc ChangeLog INSTALL THANKS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libedit.pc
%{_mandir}/man3/*
%{_mandir}/man5/*

