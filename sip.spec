Summary:	Python bindings generator for C++ class libraries.
Summary(pl):	Generator powi±zañ Pythona z bibliotekami klas C++
Name:		sip
Version:	3.0
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://www.river-bank.demon.co.uk/software/%{name}-%{version}.tar.gz
URL:		http://www.thekompany.com/projects/pykde/
Requires:	python >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generates Python bindings for C++ class libraries from a set of class
specification files. Also includes a runtime support library needed by
all generated bindings.

%description -l pl
Generuje powi±zania Pythona z bibliotekami klas C++ ze zbioru plików
ze specyfikacjami klas. Zawiera te¿ bibliotekê potrzebn± do uruchomienia
wszystkich wygenerowanych powi±zañ.

%prep
%setup -q

%build
%configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sip
%dir %{_includedir}
%{_includedir}/sip/sip.h
%{_includedir}/sip/sipQt.h
%{_libdir}/libsip.a
%attr(755,root,root) %{_libdir}/libsip.la
%attr(755,root,root) %{_libdir}/libsip.so
%attr(755,root,root) %{_libdir}/libsip.so.7
%attr(755,root,root) %{_libdir}/libsip.so.7.0.0
