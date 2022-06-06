%global optflags %{optflags} -Oz

%define major 207
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Embeddable Javascript engine
Name:		duktape
Version:	2.7.0
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://duktape.org/
Source0:	http://duktape.org/%{name}-%{version}.tar.xz
Patch0:		duktape-2.7.0-build-flags.patch

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package -n %{libname}
Summary:	Embeddable Javascript engine
Group:		System/Libraries

%description -n %{libname}
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package -n %{develname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{EVRD}
Provides:	duktape-devel = %{EVRD}

%description -n %{develname}
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1

cp Makefile.sharedlibrary Makefile

%build
%set_build_flags
%make_build INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%install
%make_install INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%files -n %{libname}
%license LICENSE.txt
%{_libdir}/libduktape.so.%{major}{,.*}
%{_libdir}/libduktaped.so.%{major}{,.*}

%files -n %{develname}
%doc AUTHORS.rst README.rst
%doc examples/
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc
