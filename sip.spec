Summary:	Python bindings generator for C++ class libraries.
Summary(pl):	Generator powi±zañ Python'a z bibliotekami klas C++
Name:		sip
Version:	2.5
Release:	1
Copyright:	Phil Thompson <phil@river-bank.demon.co.uk>
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	http://www.river-bank.demon.co.uk/software/%{name}-%{version}.tar.gz
URL:		http://www.thekompany.com/projects/pykde/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python >= 1.5

%description
Generates Python bindings for C++ class libraries from a set of class
specification files. Also includes a runtime support library needed by
all generated bindings.

%description -l pl
Generuje powi±zania Python'a z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Zawiera te¿ bibliotekê potrzebn± do uruchomienia
wszystkich wygenerowanych powi±zañ.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post
ldconfig

%postun
ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(-,root,root) %{_bindir}/sip
%attr(-,root,root) %{_includedir}/sip/sip.h
%attr(-,root,root) %{_includedir}/sip/sipQt.h
%attr(-,root,root) %{_libdir}/libsip.a
%attr(-,root,root) %{_libdir}/libsip.la
%attr(-,root,root) %{_libdir}/libsip.so
%attr(-,root,root) %{_libdir}/libsip.so.6
%attr(-,root,root) %{_libdir}/libsip.so.6.0.0
