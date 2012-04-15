%define name libnotifymm
%define version 0.6.1
%define release %mkrel 5

%define api_version 1.0
%define major 7
%define libname %mklibname notifymm %{api_version} %{major}
%define libnamedev %mklibname -d notifymm %{api_version}

Name:		%name
Summary:	C++ interface for libnotify
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libnotifymm-0.6.1-bodgenewapi.patch
BuildRequires:	glibmm2.4-devel >= 2.12.8
BuildRequires:  gtkmm2.4-devel >= 2.10
BuildRequires:	libnotify-devel >= 0.6.0

%description
Libnotifymm provides a C++ interface to the libnotify library.

%package	-n %{libname}
Summary:	C++ interface for libnotify
Group:		System/Libraries
Provides:	%{name}%{api_version} = %{version}-%{release}

%description	-n %{libname}
Libnotifymm provides a C++ interface to the libnotify library.

This package contains the library needed to run programs dynamically
linked with %{name}.


%package	-n %{libnamedev}
Summary:	Headers and development files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Provides:	%name-devel = %version-%release

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p2

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING README
# NEWS
%{_libdir}/%{name}-%{api_version}.so.%{major}*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc AUTHORS ChangeLog
%{_includedir}/%{name}-%api_version
%{_libdir}/*.so
%{_libdir}/%{name}-%{api_version}
%{_libdir}/pkgconfig/%{name}-%{api_version}.pc
