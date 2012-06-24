# TODO:
# - %build shouldn't use $RPM_BUILD_ROOT
# - libsip.so.* is built with evil RPATH (inside buildroot)

%include        /usr/lib/rpm/macros.python
Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi�za� Pythona z bibliotekami klas C++
Name:		sip
Version:	3.11
%define		_snap       	20040218
Release:	0.%{_snap}.3
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
BuildRequires:	sed >= 4.0
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
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{py_incdir},%{_bindir},%{py_libdir}}

echo 'yes' | python build.py \
	-i %{_includedir}/qt -q %{_prefix} -l qt-mt -m /usr/bin/make \
	-r %{_libdir} -t %{py_libdir} \
	-b $RPM_BUILD_ROOT%{_bindir} -d $RPM_BUILD_ROOT%{py_sitedir} \
	-e $RPM_BUILD_ROOT%{py_incdir}


%{__make}
sed -i "s:$RPM_BUILD_ROOT::g" sipconfig.py

%install
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{py_incdir},%{_sipfilesdir}}
install sipconfig.py $RPM_BUILD_ROOT%{py_sitedir}

%{__make} install

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
