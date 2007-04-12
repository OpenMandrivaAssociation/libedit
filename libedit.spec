%define snap    20070302
%define major   0
%define libname %mklibname edit %{major}

Name:           libedit
Version:        2.10
Release:        %mkrel 0.%{snap}.1
Epoch:          0
Summary:        Provides generic line editing functions similar to those found in GNU Readline
License:        BSD-style
Group:          System/Libraries
URL:            http://www.thrysoee.dk/editline/
Source0:        http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:  libncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n %{libname}
Group:      System/Libraries
Summary:    Provides generic line editing functions similar to those found in GNU Readline
Provides:   lib%{name} = %{epoch}:%{version}-%{release}
Requires(post): ldconfig
Requires(postun): ldconfig

%description -n %{libname}
This is an autotool- and libtoolized port of the NetBSD Editline library 
(libedit). This Berkeley-style licensed command line editor library 
provides generic line editing, history, and tokenization functions, 
similar to those found in GNU Readline.

%package -n %{libname}-devel
Summary:        Development files for %{rname}
Group:          Development/C
Obsoletes:      edit-devel
Obsoletes:      %{name}-devel
Provides:       edit-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}edit-devel = %{epoch}:%{version}-%{release}
Requires:       %{libname} = %{epoch}:%{version}-%{release}
Requires:       ncurses-devel

%description -n %{libname}-devel
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

This package contains development files for %{rname}.

%prep
%setup -q -n %{name}-%{snap}-%{version}

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}

# fix one conflicting manpage with readline-devel
%{__rm} -f %{buildroot}%{_mandir}/man3/history.3
%{__ln_s} editline.3 %{buildroot}%{_mandir}/man3/%{name}-history.3

# Allows us to include the examples in separate %%doc directory
find examples -type f ! -name "*.c" -exec %{__rm} -f {} \;
%{__rm} -rf examples/.{deps,libs}

# fix permissions on scripts
%{__chmod} 755 patches/*.sh

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog INSTALL THANKS
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc examples patches
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*
%{_mandir}/man5/*


