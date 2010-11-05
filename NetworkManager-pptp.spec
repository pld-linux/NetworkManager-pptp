#
%define		ppp_version	2.4.5
#
Summary:	NetworkManager VPN integration for PPTP
Summary(pl.UTF-8):	Integracja NetworkManagera z protokołem PPTP
Name:		NetworkManager-pptp
Version:	0.8.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-pptp/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	2393021a277f80b6f1dfddbd5e89ac67
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 0.8.2
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:%{ppp_version}
Requires:	NetworkManager >= 0.8.2
Requires:	ppp = 3:%{ppp_version}
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.{a,la}
rm -rf $RPM_BUILD_ROOT%{_libdir}/pppd/*.*.*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-pptp-properties.so
%attr(755,root,root) %{_libdir}/nm-pptp-auth-dialog
%attr(755,root,root) %{_libdir}/nm-pptp-service
%attr(755,root,root) %{_libdir}/pppd/%{ppp_version}/nm-pptp-pppd-plugin.so
%{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-pptp-service.conf
%{_datadir}/gnome-vpn-properties/pptp
