%define snap 20221030
%define major 0
%define oldlibname %mklibname edit 0
%define libname %mklibname edit
%define devname %mklibname edit -d
%global optflags %{optflags} -Oz
# libedit is used by llvm
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%define lib32name libedit
%define dev32name libedit-devel

Summary:	Provides generic line editing functions similar to those found in GNU Readline
Name:		libedit
Version:	3.1
Release:	1.%{snap}.1
License:	BSD-style
Group:		System/Libraries
Url:		https://www.thrysoee.dk/editline/
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:	pkgconfig(ncursesw) >= 5.9
%if %{with compat32}
BuildRequires:	devel(libncurses)
%endif

%description
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n %{libname}
Summary:	Provides generic line editing functions similar to those found in GNU Readline
Group:		System/Libraries
Conflicts:	libedit < %{EVRD}
%rename %{oldlibname}

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

%package -n %{dev32name}
Summary:	32-bit development files for %{name}
Group:		Development/C
Requires:	%{lib32name} = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n %{dev32name}
32-bit development files for %{name}

%prep
%autosetup -n %{name}-%{snap}-%{version} -p1

%build
export CONFIGURE_TOP=$(pwd)
%if %{with compat32}
mkdir build32
cd build32
%configure32 --disable-static
%make_build
cd ..
%endif

mkdir build
cd build
%configure --disable-static
%make_build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

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
%doc %{_mandir}/man3/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man7/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/*.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/libedit.pc
%endif
