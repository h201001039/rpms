# $Id$
# Authority: shuff
# Upstream: Jonathan Coome <jcoome$users,berlios,de>
# ExcludeDist: el3 el4 el5
# Rationale: needs glib2 >= 2.16


Summary: Scrobbling Music Player Daemon client
Name: scmpc
Version: 0.3.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://scmpc.berlios.de/

Source: http://download.berlios.de/scmpc/scmpc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: curl-devel >= 7.15.4
BuildRequires: glib2-devel >= 2.16
BuildRequires: libconfuse-devel
BuildRequires: pkgconfig >= 0.9.0

%description
scmpc is a client for MPD which submits your tracks to Audioscrobbler.

'Another one?', I hear you cry? Yes, I know about mpdscribble, but it doesn't
do entirely what I want it to. It doesn't run as a daemon, for example, and it
currently doesn't work if you enable crossfading in MPD. I didn't add the
support for these in mpdscribble, partly because GNU coding style scares me,
and I got slightly lost in the source code, but also because I created this as
a way of teaching myself C programming. scmpc is also very different to
mpdscribble internally because I made it multithreaded, whereas mpdscribble is
not.

Features

* Can be run as a daemon, either as a user or as root.
* Keeps unsubmitted songs in a queue which is saved to a file at a configurable
  interval.
* Will try to reconnect to MPD and Audioscrobbler if the network connection
  fails.
* Works with a password-protected MPD server.
* Works when crossfading is enabled.


%prep
%setup


%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall 

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README TODO scmpc.conf.example
%doc %{_mandir}/man?/*
%{_bindir}/*


%changelog
* Wed Apr 27 2011 Steve Huff <shuff@vecna.org> - 0.3.0-1
- Updated to release 0.3.0 (el6 only).

* Fri May 07 2010 Steve Huff <shuff@vecna.org> - 0.2.2-1
- Initial package.
