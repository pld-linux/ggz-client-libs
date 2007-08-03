# TODO:
# - there is some man pages need to be checked, also need check what is ggz.merge.menu, ggz.menu in /etc and ggzwrap in libdir

Summary:	GGZ client libraries
Summary(pl.UTF-8):	Biblioteki klienckie dla GGZ
Name:		ggz-client-libs
Version:	0.0.14
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.belnet.be/packages/ggzgamingzone/ggz/0.0.14/%{name}-%{version}.tar.gz
# Source0-md5:	efe325665fc745efe34d59dd9dea4284
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GGZ Gaming Zone core client libraries provides the common procedures
and utilities required to run the GGZ client and games.

%description -l pl.UTF-8
Biblioteki klienckie GGZ Gaming Zone dostarczają ogólne procedury i
narzędzia wymagane do uruchomienia klienta GGZ oraz gier.

%package devel
Summary:	Header files for ggz-client-lib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ggz-client-lib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95
Requires:	libggz-devel >= 0.0.14

%description devel
Header files for ggz-client-lib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ggz-client-lib.

%package static
Summary:	Static ggz-client-lib library
Summary(pl.UTF-8):	Statyczna biblioteka ggz-client-lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ggz-client-lib library.

%description static -l pl.UTF-8
Statyczna biblioteka ggz-client-lib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I m4/ggz
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man6/*.6*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
