%define name xmms-mplayer
%define version 0.3.3
%define release %mkrel 6

Name: %{name}
Summary: An input plug-in for XMMS that plays videos using MPlayer
Version: %{version}
Release: %{release}
License: GPL
Group: Video
Source0: http://thegraveyard.org/files/xmmplayer-%{version}.tar.bz2
URL: http://thegraveyard.org/xmmplayer.php
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:	libxmms-devel
BuildRequires:  automake1.8
Requires: xmms mplayer

%description
XMMPlayer is an input plugin for XMMS that allows you to play video
files from within XMMS using MPlayer as a back-end.

%prep
%setup -q -n xmmplayer-%{version}
aclocal-1.8
autoconf
automake-1.8

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif
rm -f %buildroot%{_libdir}/xmms/Input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING
%{_libdir}/xmms/Input/*


