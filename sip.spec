%include        /usr/lib/rpm/macros.python
Summary:	Python bindings generator for C++ class libraries
Summary(pl):	Generator powi±zañ Pythona z bibliotekami klas C++
Name:		sip
Version:	3.1
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.co.uk/download/sip/%{name}-%{version}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
Requires:	python >= 2.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRequires:  rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure \
	--with-qt-includes=%{_prefix}/X11R6/include/qt \
	--with-qt-libraries=%{_prefix}/X11R6/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*/*.h
%attr(755,root,root) %{py_sitedir}/lib*.*
