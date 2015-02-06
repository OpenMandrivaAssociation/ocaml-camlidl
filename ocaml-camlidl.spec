%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Stub code generator and COM binding for Objective Caml
Name:		ocaml-camlidl
Version:	1.05
Release:	7
License:	QPL and LGPLv2+ with exceptions
Group:		Development/Other
Url:		http://caml.inria.fr/pub/old_caml_site/camlidl/
Source0:	http://caml.inria.fr/pub/old_caml_site/distrib/bazar-ocaml/camlidl-%{version}.tar.gz
Source1:	http://caml.inria.fr/pub/old_caml_site/distrib/bazar-ocaml/camlidl-%{version}.doc.pdf
BuildRequires:	ocaml

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

%files
%doc LICENSE
%{_libdir}/ocaml/*.cmi
%{_libdir}/ocaml/*.cma
%{_bindir}/camlidl

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE README Changes camlidl-%{version}.doc.pdf tests
%{_libdir}/ocaml/caml/*.h
%{_libdir}/ocaml/*.a
%{_libdir}/ocaml/*.cmxa

#----------------------------------------------------------------------------

%prep
%setup -q -n camlidl-%{version}
cp config/Makefile.unix config/Makefile
#sed -e 's|^OCAMLLIB=.*|OCAMLLIB=%{_libdir}/ocaml|' \
#    -e 's|^BINDIR=.*|BINDIR=%{_bindir}|' \
#    < config/Makefile.unix \
#    > config/Makefile
cp %{SOURCE1} .

%build
make all OCAMLLIB=%{_libdir}/ocaml BINDIR=%{_bindir}

%install
install -d -m 755 %{buildroot}%{_libdir}/ocaml
install -d -m 755 %{buildroot}%{_libdir}/ocaml/caml
install -d -m 755 %{buildroot}%{_bindir}

make OCAMLLIB=%{buildroot}%{_libdir}/ocaml \
	BINDIR=%{buildroot}%{_bindir} \
	install

