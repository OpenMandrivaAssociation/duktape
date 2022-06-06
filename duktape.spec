%define major 206
%define develname %mklibname duktape -d

Summary:	Embeddable Javascript engine
Name:		duktape
Version:	2.7.0
Release:	1
License:	MIT
Url:		http://duktape.org/
Source0:	http://duktape.org/%{name}-%{version}.tar.xz
Patch0:		duktape-build.patch

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%libpackage libducktape %{major}
%{_libdir}/libduktaped.so.%{major}

%package -n %{develname}
Summary:	Development files for %{name}
Requires:	%{mklibname %{name} %{major}} = %{EVRD}
Provides:	duktape-devel = %{EVRD}

%description -n %{develname}
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1

sed -e '/^INSTALL_PREFIX/s|[^=]*$|%{_prefix}|' \
    -e '/install\:/a\\tinstall -d $(DESTDIR)$(INSTALL_PREFIX)/%{_lib}\n\tinstall -d $(DESTDIR)$(INSTALL_PREFIX)/include' \
    -e 's/\(\$.INSTALL_PREFIX.\)/$(DESTDIR)\1/g' \
    -e 's/\/lib\b/\/%{_lib}/g' \
     < Makefile.sharedlibrary > Makefile

%build
%set_build_flags
%make_build

%install
%make_install

%files -n %{develname}
%doc examples/ README.rst
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

