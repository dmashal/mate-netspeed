Summary: Applet that shows traffic on a network device
Name: netspeed_applet
Version: 0.15.2
Release: 1
URL: http://mfcn.ilo.de/netspeed_applet/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Gnome/Applets
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}
BuildRequires: pkgconfig
BuildRequires: intltool
BuildRequires: gnome-panel-devel
BuildRequires: libgnomeui-devel
BuildRequires: libgtop-devel

%description
netspeed_applet is a little GNOME applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

%prep
%setup -q

%build
%configure
%__make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang netspeed_applet

%clean
rm -rf %{buildroot}

%files -f netspeed_applet.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{prefix}/libexec/*
%{prefix}/lib/bonobo/servers/*
%{prefix}/share/pixmaps/*
