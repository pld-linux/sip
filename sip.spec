#%%define snap 20030405

%include        /usr/lib/rpm/macros.python
Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi±zañ Pythona z bibliotekami klas C++
Name:		sip
Version:	3.6
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.river-bank.demon.co.uk/download/sip/%{name}-x11-gpl-%{version}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
BuildRequires:	python >= 2.2
BuildRequires:	python-devel >= 2.2
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define          _prefix         /usr/X11R6
%define          _sipfilesdir         /usr/share/sip

%description
Generates Python bindings for C++ class libraries from a set of class
specification files. Also includes a runtime support library needed by
all generated bindings.

%description -l pl
Generuje powi±zania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Zawiera te¿ bibliotekê potrzebn± do
uruchomienia wszystkich wygenerowanych powi±zañ.

%prep
%setup -q -n %{name}-x11-gpl-%{version}

%build
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{py_incdir}}

echo 'yes' | python build.py \
	-i %{_includedir}/qt -q %{_prefix} -l qt-mt -m /usr/bin/make \
	-b $RPM_BUILD_ROOT%{_bindir} -d $RPM_BUILD_ROOT%{py_sitedir} \
	-e $RPM_BUILD_ROOT%{py_incdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{py_incdir},%{_sipfilesdir}}

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.*
%{py_incdir}/*.h
%dir %{_sipfilesdir}
