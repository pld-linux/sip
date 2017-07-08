#
# Conditional build:
%bcond_without	python2	# CPython 2.x modules
%bcond_without	python3	# CPython 3.x modules

Summary:	Python bindings generator for C++ class libraries
Summary(pl.UTF-8):	Generator powiązań Pythona z bibliotekami klas C++
Name:		sip
Version:	4.19.3
Release:	1
Epoch:		2
License:	SIP (redistributable, see LICENSE) or GPL v2 or GPL v3
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/pyqt/sip-%{version}.tar.gz
# Source0-md5:	4708187f74a4188cb4e294060707106f
Patch0:		%{name}-outoftree.patch
URL:		http://www.riverbankcomputing.com/software/sip/
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
SIP generates Python bindings for C++ class libraries from a set of
class specification files. It supports Python v2 and v3.

%description -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Obsługiwany jest Python 2 i 3.

%package -n python-sip
Summary:	Python 2 module needed by SIP generated bindings
Summary(pl.UTF-8):	Moduł Pythona 2 wymagany przez wiązania wygenerowane przez SIP
Group:		Libraries/Python
Requires:	python-libs

%description -n python-sip
SIP generates Python bindings for C++ class libraries from a set of
class specification files. This package includes Python 2 runtime
library needed by all generated bindings.

%description -n python-sip -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Ten pakiet zawiera bibliotekę Pythona 2
potrzebną do uruchomienia wszystkich wygenerowanych powiązań.

%package -n python-sip-devel
Summary:	Python 2 development files needed to build bindings using SIP
Summary(pl.UTF-8):	Pliki programistyczne Pythona 2 potrzebne do budowania wiązań przy użyciu SIP-a
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-sip = %{epoch}:%{version}-%{release}
Requires:	python-devel >= 1:2.3

%description -n python-sip-devel
Python 2 development files needed to build bindings for C++ classes
using SIP.

%description -n python-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 2 potrzebne do budowania wiązań dla klas
C++ przy użyciu SIP-a.

%package -n python3-sip
Summary:	Python 3 module needed by SIP generated bindings
Summary(pl.UTF-8):	Moduł Pythona 3 wymagany przez wiązania wygenerowane przez SIP
Group:		Libraries/Python
Requires:	python3-libs

%description -n python3-sip
SIP generates Python bindings for C++ class libraries from a set of
class specification files. This package includes Python 3 runtime
library needed by all generated bindings.

%description -n python3-sip -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Ten pakiet zawiera bibliotekę Pythona 3
potrzebną do uruchomienia wszystkich wygenerowanych powiązań.

%package -n python3-sip-devel
Summary:	Python 3 development files needed to build bindings using SIP
Summary(pl.UTF-8):	Pliki programistyczne Pythona 3 potrzebne do budowania wiązań przy użyciu SIP-a
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python3-sip = %{epoch}:%{version}-%{release}
Requires:	python3-devel >= 1:3.2

%description -n python3-sip-devel
Python 3 development files needed to build bindings for C++ classes
using SIP.

%description -n python3-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 3 potrzebne do budowania wiązań dla klas
C++ przy użyciu SIP-a.

%prep
%setup -q
%patch0 -p1

%build
# configure.py notes:
# - macros overrides must be last
# - cannot pass CXXFLAGS+="%{rpmcflags}" or so - builtin -O2 overrides rpmcflags

%if %{with python2}
install -d build-py2
cd build-py2
%{__python} ../configure.py \
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
cd ..
%endif

%if %{with python3}
install -d build-py3
cd build-py3
%{__python3} ../configure.py \
	-b %{_bindir} \
	-e %{py3_incdir} \
	-v %{_sipfilesdir} \
	-d %{py3_sitedir} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
	LINK="%{__cxx}" \
	LINK_SHLIB="%{__cxx}"

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%if %{with python2}
%{__make} -C build-py2 install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%endif

%if %{with python3}
%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README doc/html
%attr(755,root,root) %{_bindir}/sip
%dir %{_sipfilesdir}

%if %{with python2}
%files -n python-sip
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/sip.so

%files -n python-sip-devel
%defattr(644,root,root,755)
%{py_sitedir}/sipconfig.py
%{py_sitedir}/sipconfig.py[co]
%{py_sitedir}/sipdistutils.py
%{py_sitedir}/sipdistutils.py[co]
%{py_sitedir}/sip.pyi
%{py_incdir}/sip.h
%endif

%if %{with python3}
%files -n python3-sip
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/sip.so

%files -n python3-sip-devel
%defattr(644,root,root,755)
%{py3_sitedir}/sipconfig.py
%{py3_sitedir}/sipdistutils.py
%{py3_sitedir}/__pycache__/sipconfig.cpython-*.py[co]
%{py3_sitedir}/__pycache__/sipdistutils.cpython-*.py[co]
%{py3_sitedir}/sip.pyi
%{py3_incdir}/sip.h
%endif
