Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi�za� Pythona z bibliotekami klas C++
Name:		sip
Version:	4.2
Release:	1
Epoch:		2
License:	redistributable (see LICENSE)
Group:		Development/Languages/Python
Source0:	http://www.river-bank.demon.co.uk/download/sip/%{name}-%{version}.tar.gz
# Source0-md5:	b884cc15228a166c9d6fc88aaaeccc96
# Source0:	http://www.river-bank.demon.co.uk/download/snapshots/sip/%{name}-snapshot-%{_snap}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
BuildRequires:	python-devel >= 2.2
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpm-pythonprov
BuildRequires:	tmake
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
Generates Python bindings for C++ class libraries from a set of class
specification files. Also includes a runtime support library needed by
all generated bindings.

%description -l pl
Generuje powi�zania Pythona z bibliotekami klas C++ ze zbioru plik�w
ze specyfikacjami klas. Zawiera te� bibliotek� potrzebn� do
uruchomienia wszystkich wygenerowanych powi�za�.

%prep
%setup -q 

%build
# configure.py notes:
# - macros overrides must be last
# - cannot pass CXXFLAGS+="%{rpmcflags}" or so - builtin -O2 overrides rpmcflags
QTDIR=%{_prefix} \
TMAKEPATH=/usr/share/tmake \
python configure.py \
	-b %{_bindir} \
	-d %{py_sitedir} \
	-e %{py_incdir} \
	-l qt-mt \
	LIBDIR_QT="%{_libdir}" \
	LIBDIR_X11="/usr/X11R6/%{_lib}"

%{__make} -C sipgen \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -pipe -w" \
	LINK="%{__cc}"

%{__make} -C siplib \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -fPIC -pipe -w -D_REENTRANT" \
	CXXFLAGS="%{rpmcflags} -fPIC -pipe -w -D_REENTRANT" \
	LINK="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/sip.so
%{py_sitedir}/sipconfig.py
%{py_incdir}/*.h
%dir %{_sipfilesdir}
