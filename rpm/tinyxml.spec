Name:       tinyxml
Version:    2.6.2
Release:    1%{?dist}
Summary:    TinyXML is a simple, small, C++ XML parser that can be easily integrated into other programs.

License:    zlib
URL:        https://sourceforge.net/projects/tinyxml/
Source0:    ${name}-${version}.tar.bz2

%package devel
Summary: tinyxml development files
%description devel
tinyxml development files

%description
TinyXML is a simple, small, C++ XML parser that can be easily integrated into other programs.

%prep
%autosetup -p1 -n ${name}-${version}/tinyxml

%build
make %{?_smp_mflags} RELEASE_CFLAGS="$CXXFLAGS -fPIC" 
g++ -fPIC "$CXXFLAGS" -shared -o "libtinyxml.so.0.2.6.2" \
      -Wl,-soname,"libtinyxml.so.0" $(ls *.o | grep -v xmltest)

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $RPM_BUILD_ROOT/usr/{lib,include}
install -m 0755 "libtinyxml.so.0.2.6.2" $RPM_BUILD_ROOT/usr/lib/
install -m 0644 tinyxml.h tinystr.h $RPM_BUILD_ROOT/usr/include
install -Dm644 "../tinyxml.pc" $RPM_BUILD_ROOT/usr/lib/pkgconfig/tinyxml.pc
ln -s libtinyxml.so.0.2.6.2 $RPM_BUILD_ROOT/usr/lib/libtinyxml.so

%files
%defattr(-,root,root,-)
%{_libdir}/libtinyxml.so.0.2.6.2

%files devel
%defattr(-,root,root,-)
%{_libdir}/libtinyxml.so
%{_libdir}/pkgconfig/tinyxml.pc
%{_includedir}/tinyxml.h
%{_includedir}/tinystr.h

