%define name	ocaml-camlidl
%define version	1.05
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Stub code generator and COM binding for Objective Caml
Group:      Development/Other
License:    QPL and LGPLv2 with exceptions
URL:        http://caml.inria.fr/pub/old_caml_site/camlidl/
Source0:    http://caml.inria.fr/pub/old_caml_site/distrib/bazar-ocaml/camlidl-%{version}.tar.gz
Source1:    http://caml.inria.fr/pub/old_caml_site/distrib/bazar-ocaml/camlidl-%{version}.doc.pdf
Patch:      %{name}-1.05-sitelib.patch
BuildRequires:  ocaml
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CamlIDL is a stub code generator and COM binding for Objective Caml.

CamlIDL comprises two parts:

* A stub code generator that generates the C stub code required for
  the Caml/C interface, based on an MIDL specification. (MIDL stands
  for Microsoft's Interface Description Language; it looks like C
  header files with some extra annotations, plus a notion of object
  interfaces that look like C++ classes without inheritance.)

* A (currently small) library of functions and tools to import COM
  components in Caml applications, and export Caml code as COM
  components.


%package        devel
Summary:    Development files for %{name}
Group:      Development/Other
Requires:   %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n camlidl-%{version}
%patch -p 1
sed -e 's|^OCAMLLIB=.*|OCAMLLIB=%{_libdir}/ocaml|' \
    -e 's|^BINDIR=.*|BINDIR=%{_bindir}|' \
    < config/Makefile.unix \
    > config/Makefile
cp %{SOURCE1} .


%build
make all

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_libdir}/ocaml/caml
install -d -m 755 %{buildroot}%{ocaml_sitelib}/camlidl
install -d -m 755 %{buildroot}%{ocaml_sitelib}/stublibs
install -d -m 755 %{buildroot}%{_bindir}

make OCAMLLIB=%{buildroot}%{_libdir}/ocaml \
     BINDIR=%{buildroot}%{_bindir} \
     install


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{ocaml_sitelib}/camlidl
%{ocaml_sitelib}/camlidl/*.cmi
%{_bindir}/camlidl

%files devel
%defattr(-,root,root)
%doc LICENSE README Changes camlidl-%{version}.doc.pdf tests
%{_libdir}/ocaml/caml/*.h
%{ocaml_sitelib}/camlidl/*
%exclude %{ocaml_sitelib}/camlidl/*.cmi

