Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi±zañ Pythona z bibliotekami klas C++
Name:		sip
Version:	4.4.2
Release:	1
Epoch:		2
License:	redistributable (see LICENSE)
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.com/Downloads/sip4/sip-%{version}.tar.gz
# Source0-md5:	03c777fec36607a7c3210c65d88f8a66
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
Generates Python bindings for C++ class libraries from a set of class
specification files.

%description -l pl
Generuje powi±zania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas.

%package -n python-sip
Summary:	Python module needed by generated bindings
Summary(pl):	Modu³ Pythona wymagany przez wygenerowane powi±zania
Group:		Libraries/Python
%pyrequires_eq	python-libs

%description -n python-sip
Generates Python bindings for C++ class libraries from a set of class
specification files. This package includes runtime library needed by
all generated bindings.

%description -n python-sip -l pl
Generuje powi±zania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Ten pakiet zawiera bibliotekê potrzebn± do
uruchomienia wszystkich wygenerowanych powi±zañ.

%package -n python-sip-devel
Summary:	Development files needed to build bindings
Summary(pl):	Pliki programistyczne potrzebne do budowania powi±zañ
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-devel >= 2.3
%pyrequires_eq	python-libs

%description -n python-sip-devel
Development files needed to build bindings for C++ classes.

%description -n python-sip-devel -l pl
Pliki programistyczne potrzebne do budowania powi±zañ z klasami C++.

%prep
%setup -q

%build
# configure.py notes:
# - macros overrides must be last
# - cannot pass CXXFLAGS+="%{rpmcflags}" or so - builtin -O2 overrides rpmcflags
python configure.py \
	-b %{_bindir} \
	-e %{py_incdir} \
	-v %{_sipfilesdir} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LINK="%{__cxx}" \
	LINK_SHLIB="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NEWS THANKS doc/*
%attr(755,root,root) %{_bindir}/*

%files -n python-sip
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/sip.so

%files -n python-sip-devel
%defattr(644,root,root,755)
%{py_sitedir}/sip*.py
%{py_incdir}/*.h
%dir %{_sipfilesdir}
