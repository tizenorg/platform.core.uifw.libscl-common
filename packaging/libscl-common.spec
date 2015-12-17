%define _optdir /opt
%define _appdir %{_optdir}/apps

Name:       libscl-common
Summary:    A library for developing software keyboards
Version:    0.4.0
Release:    1
Group:      Graphics & UI Framework/Input
License:    Apache-2.0
Source0:    libscl-common-%{version}.tar.gz
BuildRequires:  gettext-tools
BuildRequires:  cmake
BuildRequires:  pkgconfig(elementary)


%description
A library that helps developing S/W Keyboard

%package devel
Summary:    SCL-Common header file
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
A devel package of libscl-common library that helps developing S/W Keyboard

%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR:PATH=%{_libdir}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

%make_install



%post

%postun

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libscl-common.so
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/libscl-common.pc
