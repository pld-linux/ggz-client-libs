# TODO:
# warning: Installed (but unpackaged) file(s) found:
#	/etc/xdg/menus/applications-merged/ggz.merge.menu
#	/etc/xdg/menus/ggz.menu
#	/usr/share/desktop-directories/ggz-games.directory
#	/usr/share/desktop-directories/ggz.directory
#
# These files are to show in WM menu GGZ clients / games, which have special
# Category entry in desktop files - X-GGZ or X-GGZ-Games
#
# - create subpackage for them (-menus?)
#
Summary:	GGZ client libraries
Summary(pl.UTF-8):	Biblioteki klienckie dla GGZ
Name:		ggz-client-libs
Version:	0.0.14.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	299eaa93721b1d867b5bf7dc6ac764b0
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
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Create ggz.modules
echo "[Games]" > $RPM_BUILD_ROOT%{_sysconfdir}/ggz.modules

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggz.modules
%attr(755,root,root) %{_bindir}/ggz
%attr(755,root,root) %{_bindir}/ggz-config
%attr(755,root,root) %{_bindir}/ggz-wrapper
%dir %{_libdir}/ggz
%attr(755,root,root) %{_libdir}/ggz/ggzwrap
%attr(755,root,root) %{_libdir}/libggzcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggzcore.so.9
%attr(755,root,root) %{_libdir}/libggzmod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggzmod.so.4
%{_mandir}/man1/ggzwrap.1*
%{_mandir}/man5/ggz.modules.5*
%{_mandir}/man6/ggz-config.6*
%{_mandir}/man6/ggz-wrapper.6*
%{_mandir}/man6/ggz.6*
%{_mandir}/man7/ggz.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libggzcore.so
%attr(755,root,root) %{_libdir}/libggzmod.so
%{_libdir}/libggzcore.la
%{_libdir}/libggzmod.la
%{_includedir}/ggzcore.h
%{_includedir}/ggzmod.h
%{_mandir}/man3/ggzcore_h.3*
%{_mandir}/man3/ggzmod_h.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libggzcore.a
%{_libdir}/libggzmod.a
