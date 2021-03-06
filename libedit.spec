%define snap 20191231
%define major 0
%define libname %mklibname edit %{major}
%define devname %mklibname edit -d
%global optflags %{optflags} -Oz

Summary:	Provides generic line editing functions similar to those found in GNU Readline
Name:		libedit
Version:	3.1
Release:	1.%{snap}.5
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

%package -n %{libname}
Summary:	Provides generic line editing functions similar to those found in GNU Readline
Group:		System/Libraries
Conflicts:	libedit < %{EVRD}

%description -n %{libname}
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	libedit < %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -n %{name}-%{snap}-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install

# Allows us to include the examples in separate %%doc directory
find examples -type f ! -name "*.c" | %{_bindir}/xargs rm
rm -r examples/.libs

# Fix conflict with libreadline
mv %{buildroot}%{_mandir}/man3/history.3 %{buildroot}%{_mandir}/man3/libedit-history.3

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
%{_mandir}/man7/*
