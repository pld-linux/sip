Summary:	Python bindings generator for C++ class libraries
Summary(pl.UTF-8):	Generator powiązań Pythona z bibliotekami klas C++
Name:		sip
Version:	4.13
Release:	1
Epoch:		2
License:	redistributable (see LICENSE)
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/sip4/sip-%{version}.tar.gz
# Source0-md5:	21b4e2cad56e4156df2220143264b8ff
URL:		http://www.riverbankcomputing.com/software/sip/
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
Generates Python bindings for C++ class libraries from a set of class
specification files. It supports Python v2 and v3.

%description -l pl.UTF-8
Generuje powiązania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Obsługiwany jest Python 2 i 3.

%package -n python-sip
Summary:	Python module needed by generated bindings
Summary(pl.UTF-8):	Moduł Pythona wymagany przez wygenerowane powiązania
Group:		Libraries/Python
%pyrequires_eq	python-libs

%description -n python-sip
Generates Python bindings for C++ class libraries from a set of class
specification files. This package includes runtime library needed by
all generated bindings.

%description -n python-sip -l pl.UTF-8
Generuje powiązania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Ten pakiet zawiera bibliotekę potrzebną do
uruchomienia wszystkich wygenerowanych powiązań.

%package -n python-sip-devel
Summary:	Development files needed to build bindings
Summary(pl.UTF-8):	Pliki programistyczne potrzebne do budowania powiązań
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-devel >= 2.3
%pyrequires_eq	python-libs

%description -n python-sip-devel
Development files needed to build bindings for C++ classes.

%description -n python-sip-devel -l pl.UTF-8
Pliki programistyczne potrzebne do budowania powiązań z klasami C++.

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
	-d %{py_sitedir} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
	LINK="%{__cxx}" \
	LINK_SHLIB="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README doc/html
%attr(755,root,root) %{_bindir}/sip

%files -n python-sip
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/sip.so
%dir %{_sipfilesdir}

%files -n python-sip-devel
%defattr(644,root,root,755)
%{py_sitedir}/sipconfig.py
%{py_sitedir}/sipconfig.py[co]
%{py_sitedir}/sipdistutils.py
%{py_sitedir}/sipdistutils.py[co]
%{py_incdir}/sip.h
