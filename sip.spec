%include        /usr/lib/rpm/macros.python
Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi±zañ Pythona z bibliotekami klas C++
Name:		sip
Version:	3.5
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.co.uk/download/sip/%{name}-x11-gpl-%{version}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
Requires:	python >= 2.2
BuildRequires:	qt-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-x11-gpl-%{version}-root-%(id -u -n)

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

#QMAKESPEC=%{_prefix}/X11R6/share/qt/mkspecs/linux-g++
#export QMAKESPEC
install -d  $RPM_BUILD_ROOT%{_libdir}/python2.2/site-packages
install -d $RPM_BUILD_ROOT%{_includedir}/python2.2

python build.py  -i %{_includedir}/qt -q %{_prefix} -l qt-mt -m %{_bindir}/make -b $RPM_BUILD_ROOT%{_bindir}/ -d $RPM_BUILD_ROOT%{_libdir}/python2.2/site-packages -e $RPM_BUILD_ROOT%{_includedir}/python2.2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_libdir}/python2.2/site-packages
install -d $RPM_BUILD_ROOT%{_includedir}/python2.2

%{__make} install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog  NEWS  README  THANKS
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*/*.h
%attr(755,root,root) %{py_sitedir}/lib*.*
