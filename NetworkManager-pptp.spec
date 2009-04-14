Summary:	NetworkManager VPN integration for PPTP
Summary(pl.UTF-8):	Integracja NetworkManagera z protokołem PPTP
Name:		NetworkManager-pptp
Version:	0.7.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-pptp/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	7deb878bed3e1a5fe32414424fa514d4
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 0.7.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires:	NetworkManager >= 0.7.1
Requires:	ppp
Requires:	pptp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for PPTP.

%description -l pl.UTF-8
Integracja NetworkManagera z protokołem PPTP.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.{a,la}
rm -rf $RPM_BUILD_ROOT%{_libdir}/pppd/2.4.4/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-pptp-properties.so
%attr(755,root,root) %{_libdir}/nm-pptp-auth-dialog
%attr(755,root,root) %{_libdir}/nm-pptp-service
%attr(755,root,root) %{_libdir}/pppd/2.4.4/nm-pptp-pppd-plugin.so
%{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-pptp-service.conf
%{_desktopdir}/nm-pptp.desktop
%{_datadir}/gnome-vpn-properties/pptp
%{_iconsdir}/hicolor/*/*/*.png
