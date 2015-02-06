Summary: Audio meta-data library
Name: taglib-gio
Version: 0.2
Release: 4
License: GPLv2+
Group: Sound
Source0: http://redmine.youki.mp/attachments/download/31/%{name}-%{version}.tar.gz
Patch0: taglib-gio-0.2-link.patch
BuildRequires: glib2-devel
BuildRequires: zlib-devel
URL: http://youki.mp/

%description
Audio meta-data library. Used by youki media player.

#---------------------------------------------------------------
%define major 1
%define libname %mklibname %name %major

%package -n %libname
Group: System/Libraries
Summary: Shared libraries for taglib-gio

%description -n %libname
This package contains shared libraries for taglib-gio.

%files -n %libname
%defattr(-, root, root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

#---------------------------------------------------------------
%define develname %mklibname %name -d

%package -n %develname
Group: System/Libraries
Summary: Development files for taglib-gio
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %develname
This package contains development files for taglib-gio.

%files -n %develname
%defattr(-, root, root)
%{_bindir}/%name-config
%{multiarch_bindir}/%{name}-config
%{_libdir}/*.so
%{_includedir}/%name
%{_libdir}/pkgconfig/*.pc

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
%make

%install
rm -rf %buildroot
%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/%name-config

%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 615108
- the mass rebuild of 2010.1 packages

* Sun Jan 31 2010 Funda Wang <fwang@mandriva.org> 0.2-1mdv2010.1
+ Revision: 498715
- import taglib-gio


