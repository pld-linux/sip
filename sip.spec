%include        /usr/lib/rpm/macros.python
Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi±zañ Pythona z bibliotekami klas C++
Name:		sip
Version:	4.0.1
#%%define		_snap       	20040218
#Release:	0.%{_snap}.7
Release:	1
Epoch:  	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.river-bank.demon.co.uk/download/sip/%{name}-%{version}.tar.gz
# Source0-md5:	a2aa4ef53cb4f18e7ce25bc2e123548e
# Source0:	http://www.river-bank.demon.co.uk/download/snapshots/sip/%{name}-snapshot-%{_snap}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
BuildRequires:	python-devel >= 2.2
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpm-pythonprov
BuildRequires:	tmake
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
Generates Python bindings for C++ class libraries from a set of class
specification files. Also includes a runtime support library needed by
all generated bindings.

%description -l pl
Generuje powi±zania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Zawiera te¿ bibliotekê potrzebn± do
uruchomienia wszystkich wygenerowanych powi±zañ.

%prep
%setup -q 
#%%setup -q -n %{name}-snapshot-%{_snap}

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
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/sip.so
%{py_sitedir}/sipconfig.py
%{py_incdir}/*.h
%dir %{_sipfilesdir}
