# $Id: $

# Authority: dries
# Upstream: 

Summary: Extensible Perl toolkit for multi-platform GUI development
Name: prima
Version: 1.15
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.prima.eu.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.prima.eu.org/download/Prima.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Screenshot: http://www.prima.eu.org/big-picture/vb_unix_large.gif
# ScreenshotURL: http://www.prima.eu.org/big-picture/

%description
Prima is an extensible Perl toolkit for multi-platform GUI development.
Platforms supported include Linux, Windows NT/9x/2K, OS/2 and UNIX/X11
workstations (FreeBSD, IRIX, SunOS, Solaris and others).

 The toolkit contains a rich set of standard widgets and has emphasis on 2D
image processing tasks. A Perl program using PRIMA looks and behaves
identically on X, Win32 and OS/2 PM.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Wed May 5 2004 Dries Verachtert <dries@ulyssis.org> 1.15-1
- Initial package.

