Name:           sailfishpen
Version:        1.0.0
Release:        1
Summary:        SailfishPen is Samsung's Spen support for Galaxy Note 4.
License:        GPLv3
URL:            https://github.com/edp17/sailfishpen
BuildArch:      armv7hl
Source0:        harbour-spen-menu
Source1:        evtest
Source2:        harbour-spen-menu.qml
Source3:        CoverPage.qml
Source4:        Main.qml
Source5:        About.qml
Source6:        sailfishpen.service
Source7:        sailfishpen-daemon.sh
Source8:        sailfishpen-start-service.sh
Source9:        harbour-sailfishpen.png

%description
SailfisPen is inspired by Samsung's S-Pen and is created for Sailfish Os.

%prep
%setup
%patch0 -p1

%install
mkdir -p %{buildroot}/usr/bin/droid
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/share/harbour-spen-menu
mkdir -p %{buildroot}/usr/share/icons/hicolor/86x86/apps

install -D -m775 %{SOURCE0} %{buildroot}/usr/bin/harbour-spen-menu
install -D -m775 %{SOURCE1} %{buildroot}/usr/bin/evtest
install -D -m644 %{SOURCE2} %{buildroot}/usr/share/harbour-spen-menu/qml/harbour-spen-menu.qml
install -D -m644 %{SOURCE3} %{buildroot}/usr/share/harbour-spen-menu/qml/cover/CoverPage.qml
install -D -m644 %{SOURCE4} %{buildroot}/usr/share/harbour-spen-menu/qml/pages/Main.qml
install -D -m644 %{SOURCE5} %{buildroot}/usr/share/harbour-spen-menu/qml/pages/About.qml
install -D -m644 %{SOURCE6} %{buildroot}/%{_unitdir}/sailfishpen.service
install -D -m775 %{SOURCE7} %{buildroot}/usr/bin/droid/sailfishpen-daemon.sh
install -D -m775 %{SOURCE8} %{buildroot}/usr/bin/droid/sailfishpen-start-service.sh
install -D -m644 %{SOURCE9} %{buildroot}/usr/share/icons/hicolor/86x86/apps/harbour-sailfishpen.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
systemctl daemon-reload
systemctl-user daemon-reload
systemctl enable sailfishpen

%files
%defattr(-,root,root,-)
%{_bindir}/harbour-spen-menu
%{_bindir}/evtest
%{_bindir}/droid/sailfishpen-daemon.sh
%{_bindir}/droid/sailfishpen-start-service.sh
%{_unitdir}/sailfishpen.service
%{_datadir}/harbour-spen-menu/qml/harbour-spen-menu.qml
%{_datadir}/harbour-spen-menu/qml/cover/CoverPage.qml
%{_datadir}/harbour-spen-menu/qml/pages/Main.qml
%{_datadir}/harbour-spen-menu/qml/pages/About.qml
%{_datadir}/icons/hicolor/86x86/apps/harbour-sailfishpen.png