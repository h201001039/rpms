# $Id$
# Authority: dag
# Upstream: Dan Dennedy <ddennedy$users,sf,net>

Summary: Simple non-linear video editor
Name: kino
Version: 0.7.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://kino.schirmacher.de/filemanager/download/36/kino-%{version}.tar.gz
Source1: kino.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdv-devel >= 0.102, libavc1394-devel, libraw1394-devel
BuildRequires: libogg-devel, libvorbis-devel, a52dec-devel
BuildRequires: XFree86-devel, libgnomeui-devel >= 2.0, gettext
BuildRequires: libxml2-devel, libsamplerate-devel
BuildRequires: dos2unix
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_quicktime:BuildRequires: libquicktime-devel}
%{!?_without_ffmpeg:BuildRequires: ffmpeg-devel}

Obsoletes: kino-devel <= %{version}

%description
The new generation of digital camcorders use the Digital Video (DV) data
format. Kino allows you to record, create, edit, and play movies recorded
with DV camcorders. Unlike other editors, this program uses many keyboard
commands for fast navigating and editing inside the movie.

%prep
%setup
# Fix up the desktop entry (it has CRLF line ends in 0.7.2, dfi barfs on it!)
dos2unix kino.desktop
# Use the kino icon we include
%{__perl} -pi.orig -e 's|gnome-multimedia.png|kino.png|g' kino.desktop

%build
%configure \
    --with-hotplug-script-dir=%{_sysconfdir}/hotplug/usb \
    --with-hotplug-usermap-dir=%{_libdir}/hotplug/kino \
    %{!?_without_quicktime:--with-quicktime} \
    %{!?_without_ffmpeg:--with-avcodec}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
    hotplugscriptdir=%{buildroot}%{_sysconfdir}/hotplug/usb \
    hotplugusermapdir=%{buildroot}%{_libdir}/hotplug/kino
%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 kino.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/kino.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		kino.desktop
%endif

# Install the pixmap for the menu entry
%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/kino.png

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr (-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README*
%doc %{_mandir}/man?/*
#%doc %{_datadir}/gnome/help/kino/
%config %{_sysconfdir}/hotplug/usb/*
%{_bindir}/*
%dir %{_libdir}/hotplug/
%{_libdir}/hotplug/kino/
%{_datadir}/kino/
%{_datadir}/pixmaps/kino.png
%{_includedir}/kino/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/kino.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/gnome-kino.desktop}

%changelog
* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net> 0.7.2-1
- Update to 0.7.2.
- Spec file changes to match upstream build fixes.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.7.1-3
- Rebuild for x86_64 with quicktime support.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net> 0.7.1-2
- Updated the desktop entry creation to the new current method.
- Fixed build requirements.
- Added custom icon for the menu entry (taken from the logo).

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Obsolete older kino-devel package. (Jeff Moe)

* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to 0.7.0.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to 0.6.5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to 0.6.4.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Initial package. (using DAR)
