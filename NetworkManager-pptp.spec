Summary:	NetworkManager VPN integration for PPTP
Summary(pl.UTF-8):	Integracja NetworkManagera z protokołem PPTP
Name:		NetworkManager-pptp
Version:	0.9.4.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-pptp/0.9/%{name}-%{version}.tar.xz
# Source0-md5:	030eb9778d782b5f47a4d8da84fe7c26
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 2:0.9.4.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:2.4.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:0.9.4.0
Requires:	dbus-glib >= 0.74
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-pppd-plugin-dir=%{_libdir}/pppd/plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pppd/*.*.*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-pptp-properties.so
%attr(755,root,root) %{_libdir}/nm-pptp-auth-dialog
%attr(755,root,root) %{_libdir}/nm-pptp-service
%attr(755,root,root) %{_libdir}/pppd/plugins/nm-pptp-pppd-plugin.so
%{_sysconfdir}/NetworkManager/VPN/nm-pptp-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-pptp-service.conf
%{_datadir}/gnome-vpn-properties/pptp
