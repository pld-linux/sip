#
# Conditional build:
%bcond_without	python2	# CPython 2.x modules
%bcond_without	python3	# CPython 3.x modules
%bcond_without	pyqt4	# PyQt4.sip module
%bcond_without	pyqt5	# PyQt5.sip module

Summary:	Python bindings generator for C++ class libraries
Summary(pl.UTF-8):	Generator powiązań Pythona z bibliotekami klas C++
Name:		sip
Version:	4.19.25
Release:	1
Epoch:		2
License:	SIP (redistributable, see LICENSE) or GPL v2 or GPL v3
Group:		Development/Languages/Python
#Source0Download: https://riverbankcomputing.com/software/sip/download
Source0:	https://www.riverbankcomputing.com/static/Downloads/sip/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1891a7b71c72d83951d5851ae10b2f0c
URL:		https://riverbankcomputing.com/software/sip/
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
Requires:	python-devel >= 1:2.3

%description -n python-sip-devel
Python 2 development files needed to build bindings for C++ classes
using SIP.

%description -n python-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 2 potrzebne do budowania wiązań dla klas
C++ przy użyciu SIP-a.

%package -n python-PyQt4-sip
Summary:	Python 2 module needed by SIP generated bindings for PyQt4
Summary(pl.UTF-8):	Moduł Pythona 2 wymagany przez wiązania wygenerowane przez SIP dla PyQt4
Group:		Libraries/Python
Requires:	python-libs

%description -n python-PyQt4-sip
SIP generates Python bindings for C++ class libraries from a set of
class specification files. This package includes Python 2 runtime
library needed by all generated bindings for PyQt4.

%description -n python-PyQt4-sip -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Ten pakiet zawiera bibliotekę Pythona 2
potrzebną do uruchomienia wszystkich wygenerowanych wiązań dla PyQt4.

%package -n python-PyQt4-sip-devel
Summary:	Python 2 development files needed to build bindings for PyQt4 using SIP
Summary(pl.UTF-8):	Pliki programistyczne Pythona 2 potrzebne do budowania wiązań dla PyQt4 przy użyciu SIP-a
Group:		Development/Libraries
Requires:	python-PyQt4-sip = %{epoch}:%{version}-%{release}
Requires:	python-sip-devel = %{epoch}:%{version}-%{release}

%description -n python-PyQt4-sip-devel
Python 2 development files needed to build bindings for C++ classes
for PyQt4 using SIP.

%description -n python-PyQt4-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 2 potrzebne do budowania wiązań dla klas
C++ dla PyQt4 przy użyciu SIP-a.

%package -n python-PyQt5-sip
Summary:	Python 2 module needed by SIP generated bindings for PyQt5
Summary(pl.UTF-8):	Moduł Pythona 2 wymagany przez wiązania wygenerowane przez SIP dla PyQt5
Group:		Libraries/Python
Requires:	python-libs

%description -n python-PyQt5-sip
SIP generates Python bindings for C++ class libraries from a set of
class specification files. This package includes Python 2 runtime
library needed by all generated bindings for PyQt5.

%description -n python-PyQt5-sip -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Ten pakiet zawiera bibliotekę Pythona 2
potrzebną do uruchomienia wszystkich wygenerowanych wiązań dla PyQt5.

%package -n python-PyQt5-sip-devel
Summary:	Python 2 development files needed to build bindings for PyQt5 using SIP
Summary(pl.UTF-8):	Pliki programistyczne Pythona 2 potrzebne do budowania wiązań dla PyQt5 przy użyciu SIP-a
Group:		Development/Libraries
Requires:	python-PyQt5-sip = %{epoch}:%{version}-%{release}
Requires:	python-sip-devel = %{epoch}:%{version}-%{release}

%description -n python-PyQt5-sip-devel
Python 2 development files needed to build bindings for C++ classes
for PyQt5 using SIP.

%description -n python-PyQt5-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 2 potrzebne do budowania wiązań dla klas
C++ dla PyQt5 przy użyciu SIP-a.

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

%package -n python3-PyQt4-sip
Summary:	Python 3 module needed by SIP generated bindings for PyQt4
Summary(pl.UTF-8):	Moduł Pythona 3 wymagany przez wiązania wygenerowane przez SIP dla PyQt4
Group:		Libraries/Python
Requires:	python3-libs

%description -n python3-PyQt4-sip
SIP generates Python bindings for C++ class libraries from a set of
class specification files. This package includes Python 2 runtime
library needed by all generated bindings for PyQt4.

%description -n python3-PyQt4-sip -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Ten pakiet zawiera bibliotekę Pythona 2
potrzebną do uruchomienia wszystkich wygenerowanych wiązań dla PyQt4.

%package -n python3-PyQt4-sip-devel
Summary:	Python 3 development files needed to build bindings for PyQt4 using SIP
Summary(pl.UTF-8):	Pliki programistyczne Pythona 3 potrzebne do budowania wiązań dla PyQt4 przy użyciu SIP-a
Group:		Development/Libraries
Requires:	python3-PyQt4-sip = %{epoch}:%{version}-%{release}
Requires:	python3-sip-devel = %{epoch}:%{version}-%{release}

%description -n python3-PyQt4-sip-devel
Python 3 development files needed to build bindings for C++ classes
for PyQt4 using SIP.

%description -n python3-PyQt4-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 3 potrzebne do budowania wiązań dla klas
C++ dla PyQt4 przy użyciu SIP-a.

%package -n python3-PyQt5-sip
Summary:	Python 3 module needed by SIP generated bindings for PyQt5
Summary(pl.UTF-8):	Moduł Pythona 3 wymagany przez wiązania wygenerowane przez SIP dla PyQt5
Group:		Libraries/Python
Requires:	python3-libs

%description -n python3-PyQt5-sip
SIP generates Python bindings for C++ class libraries from a set of
class specification files. This package includes Python 2 runtime
library needed by all generated bindings for PyQt5.

%description -n python3-PyQt5-sip -l pl.UTF-8
SIP generuje powiązania Pythona z bibliotekami klas C++ ze zbioru
plików ze specyfikacjami klas. Ten pakiet zawiera bibliotekę Pythona 2
potrzebną do uruchomienia wszystkich wygenerowanych wiązań dla PyQt5.

%package -n python3-PyQt5-sip-devel
Summary:	Python 3 development files needed to build bindings for PyQt5 using SIP
Summary(pl.UTF-8):	Pliki programistyczne Pythona 3 potrzebne do budowania wiązań dla PyQt5 przy użyciu SIP-a
Group:		Development/Libraries
Requires:	python3-PyQt5-sip = %{epoch}:%{version}-%{release}
Requires:	python3-sip-devel = %{epoch}:%{version}-%{release}

%description -n python3-PyQt5-sip-devel
Python 3 development files needed to build bindings for C++ classes
for PyQt5 using SIP.

%description -n python3-PyQt5-sip-devel -l pl.UTF-8
Pliki programistyczne Pythona 3 potrzebne do budowania wiązań dla klas
C++ dla PyQt5 przy użyciu SIP-a.

%prep
%setup -q

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

%if %{with pyqt4} || %{with pyqt5}
for mod in %{?with_pyqt4:PyQt4} %{?with_pyqt5:PyQt5} ; do
install -d build-py2-${mod}
cd build-py2-${mod}
%{__python} ../configure.py \
	--sip-module=${mod}.sip \
	--no-dist-info \
	--no-tools \
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
done
%endif
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

%if %{with pyqt4} || %{with pyqt5}
for mod in %{?with_pyqt4:PyQt4} %{?with_pyqt5:PyQt5} ; do
install -d build-py3-${mod}
cd build-py3-${mod}
%{__python3} ../configure.py \
	--sip-module=${mod}.sip \
	--no-dist-info \
	--no-tools \
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
done
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%if %{with python2}
%{__make} -C build-py2 install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with pyqt4} || %{with pyqt5}
for mod in %{?with_pyqt4:PyQt4} %{?with_pyqt5:PyQt5} ; do
%{__make} -C build-py2-${mod} install \
	DESTDIR=$RPM_BUILD_ROOT

# ensure content is the same and hardlink
cmp $RPM_BUILD_ROOT%{py_sitedir}/sip.pyi $RPM_BUILD_ROOT%{py_sitedir}/${mod}/sip.pyi
ln -f $RPM_BUILD_ROOT%{py_sitedir}/sip.pyi $RPM_BUILD_ROOT%{py_sitedir}/${mod}/sip.pyi
done
%endif

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/sip-%{version}.dist-info
%endif

%if %{with python3}
%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with pyqt4} || %{with pyqt5}
for mod in %{?with_pyqt4:PyQt4} %{?with_pyqt5:PyQt5} ; do
%{__make} -C build-py3-${mod} install \
	DESTDIR=$RPM_BUILD_ROOT

# ensure content is the same and hardlink
cmp $RPM_BUILD_ROOT%{py3_sitedir}/sip.pyi $RPM_BUILD_ROOT%{py3_sitedir}/${mod}/sip.pyi
ln -f $RPM_BUILD_ROOT%{py3_sitedir}/sip.pyi $RPM_BUILD_ROOT%{py3_sitedir}/${mod}/sip.pyi
done
%endif

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/sip-%{version}.dist-info
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

%if %{with pyqt4}
%files -n python-PyQt4-sip
%defattr(644,root,root,755)
%dir %{py_sitedir}/PyQt4
%attr(755,root,root) %{py_sitedir}/PyQt4/sip.so

%files -n python-PyQt4-sip-devel
%defattr(644,root,root,755)
%{py_sitedir}/PyQt4/sip.pyi
%endif

%if %{with pyqt5}
%files -n python-PyQt5-sip
%defattr(644,root,root,755)
%dir %{py_sitedir}/PyQt5
%attr(755,root,root) %{py_sitedir}/PyQt5/sip.so

%files -n python-PyQt5-sip-devel
%defattr(644,root,root,755)
%{py_sitedir}/PyQt5/sip.pyi
%endif
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

%if %{with pyqt4}
%files -n python3-PyQt4-sip
%defattr(644,root,root,755)
%dir %{py3_sitedir}/PyQt4
%attr(755,root,root) %{py3_sitedir}/PyQt4/sip.so

%files -n python3-PyQt4-sip-devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt4/sip.pyi
%endif

%if %{with pyqt5}
%files -n python3-PyQt5-sip
%defattr(644,root,root,755)
%dir %{py3_sitedir}/PyQt5
%attr(755,root,root) %{py3_sitedir}/PyQt5/sip.so

%files -n python3-PyQt5-sip-devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/sip.pyi
%endif
%endif
