#
# Conditional build:
%bcond_without	gtk4	# Gtk4 version of editor plugin (GNOME 42+)

Summary:	NetworkManager VPN integration for PPTP
Summary(pl.UTF-8):	Integracja NetworkManagera z protokołem PPTP
Name:		NetworkManager-pptp
Version:	1.2.12
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/NetworkManager-pptp/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	cde35b1d92b2a1f49118a59547be3e60
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	glib2-devel >= 1:2.34
BuildRequires:	gtk+3-devel >= 3.4
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
%{?with_gtk4:BuildRequires:	libnma-gtk4-devel >= 1.8.33}
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:2.4.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.0.0
Requires:	NetworkManager-gtk-lib >= 1.0.6
Requires:	glib2 >= 1:2.34
Requires:	gtk+3 >= 3.4
Requires:	libsecret >= 0.18
%requires_eq	ppp
Requires:	pptp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for PPTP.

%description -l pl.UTF-8
Integracja NetworkManagera z protokołem PPTP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	%{?with_gtk4:--with-gtk4} \
	--with-pppd-plugin-dir=%{_libdir}/pppd/plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pppd/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-pptp.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-pptp-editor.so
%if %{with gtk4}
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-pptp-editor.so
%endif
%attr(755,root,root) %{_libdir}/pppd/plugins/nm-pptp-pppd-plugin.so
%attr(755,root,root) %{_libexecdir}/nm-pptp-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-pptp-service
%{_prefix}/lib/NetworkManager/VPN/nm-pptp-service.name
%{_datadir}/dbus-1/system.d/nm-pptp-service.conf
%{_datadir}/metainfo/network-manager-pptp.metainfo.xml
