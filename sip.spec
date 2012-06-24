# TODO:
# - libsip.so.* is built with evil RPATH (inside buildroot)
# - Does %{py_sitedir}/libsip.so needs ldconfig ?

%include        /usr/lib/rpm/macros.python
Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi�za� Pythona z bibliotekami klas C++
Name:		sip
Version:	3.11
%define		_snap       	20040218
Release:	0.%{_snap}.4
License:	GPL
Group:		Development/Languages/Python
# Source0:	http://www.river-bank.demon.co.uk/download/sip/%{name}-x11-gpl-%{version}.tar.gz
# http://www.river-bank.demon.co.uk/download/snapshots/sip/sip-snapshot-20040218.tar.gz
Source0:	http://www.river-bank.demon.co.uk/download/snapshots/sip/%{name}-snapshot-%{_snap}.tar.gz
# Source0-md5:	73dd4a8be8e75fb1a44e46280030e0f2
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
BuildRequires:	python-devel >= 2.2
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
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
#%%setup -q -n %{name}-x11-gpl-%{version}
%setup -q -n %{name}-snapshot-%{_snap}

%build

python configure.py \
	-b %{_bindir} -d %{py_sitedir} \
	-e %{py_incdir} \
	-l qt-mt \

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.*
%{py_sitedir}/sipconfig.py
%{py_incdir}/*.h
%dir %{_sipfilesdir}
