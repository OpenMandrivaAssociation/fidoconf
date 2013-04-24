%define name    fidoconf
%define version 1.4.0
%define preversion rc5

%define rel 3
%define release 0.%{preversion}.%{rel}

%define major 1.4
%define libname %mklibname %name %major

Summary:	Library to access the fidoconfig
Name:       %{name}
Version:    %{version}
Release:    %{release}
License:	GPL
Group:		File tools
Source0:		%{name}-%{major}-%{preversion}.tar.bz2
Patch0:		fidoconf-20021015-main.patch
Patch1:		fidoconf-20021015-doc.patch
Patch2:		fidoconf-20021015-man.patch
Patch3:		fidoconf-20021022-config.patch
Patch4:		fidoconf-20030523-fc2fgate.patch
Patch5:		fidoconf-tparser.diff
Patch6:		fidoconf-Makefile.diff
patch7:		fidoconf-1.4-rc5.huskymak.patch
patch8:		fidoconf-1.4-rc5.printf.patch
BuildRequires:	huskybse smapi-devel texinfo
URL:		http://sourceforge.net/projects/husky/

%description
The design goal of fidoconfig was to provide one config-file for several
different fido software packages like editor, tosser etc.
An additional aim was to have one library (fidoconfig) which can be used by
all programs.
The advantage is you only have to edit one config-file, so changing your
system is much easier than with common software packages. Also bugs can only
creep in one library and not in thousands over thousands libraries.

%package -n %libname
Summary: Library to access the fidoconfig
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n %libname
The design goal of fidoconfig was to provide one config-file for several
different fido software packages like editor, tosser etc.
An additional aim was to have one library (fidoconfig) which can be used by
all programs.
The advantage is you only have to edit one config-file, so changing your
system is much easier than with common software packages. Also bugs can only
creep in one library and not in thousands over thousands libraries.

%package -n %libname-devel
Summary: Library to access the fidoconfig, development files
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: lib%name-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release} 

%description -n %libname-devel
The design goal of fidoconfig was to provide one config-file for several
different fido software packages like editor, tosser etc.
An additional aim was to have one library (fidoconfig) which can be used by
all programs.
The advantage is you only have to edit one config-file, so changing your
system is much easier than with common software packages. Also bugs can only
creep in one library and not in thousands over thousands libraries.

This Package contains the Development Files. Only needed if you want to
compile the Husky-Programs yourself

%prep
%setup -q -n %name
#% patch0 -p1
#% patch1 -p1
#% patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1 -b .huskymak
%patch8 -p1 -b .printf

%build
MANDIR=$RPM_BUILD_ROOT%{_mandir} BINDIR=$RPM_BUILD_ROOT%{_bindir} INCDIR=$RPM_BUILD_ROOT%{_includedir} LIBDIR=$RPM_BUILD_ROOT%{_libdir} INFODIR=$RPM_BUILD_ROOT%{_infodir}
%make OPTCFLAGS=" -s -c -fPIC $RPM_OPT_FLAGS"

%install
make BINDIR=$RPM_BUILD_ROOT%{_bindir} INCDIR=$RPM_BUILD_ROOT%{_includedir} LIBDIR=$RPM_BUILD_ROOT%{_libdir} INFODIR=$RPM_BUILD_ROOT%{_infodir} install
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
make MANDIR=$RPM_BUILD_ROOT%{_mandir} install-man

chmod 755 $RPM_BUILD_ROOT%_bindir/*
chmod 755 $RPM_BUILD_ROOT%_libdir/*



%files
%defattr(-,root,root)
%doc COPYING ChangeLog HISTORY INSTALL README.TXT TODO VERSION fconf2dir fconf2fidogate.cfg.sample doc/config
%{_bindir}/*
%{_infodir}/fidoconfig.info*
%{_mandir}/*/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libfidoconfig.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/libfidoconfig.so
%dir %{_includedir}/fidoconf
%{_includedir}/fidoconf/*
%{_libdir}/libfidoconfig.a




%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4.0-0.rc5.3mdv2009.0
+ Revision: 245132
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4.0-0.rc5.1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode bz2 extension


* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 16:36:07 (53348)
- 1.4-rc5

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 16:30:11 (53343)
Import fidoconf

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 1.4.0-0.rc2.3mdk
- rebuild

* Sun Jan 30 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.4.0-0.rc2.2mdk
- birthday rebuild

* Tue Dec 23 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.4.0-0.rc2.1mdk
- %%mklibname
- From Iouri Goussev <elendal@polygonized.com>
  - First MDK version
  - original SPEC by Sergey Zhemchugov <Sergey_Zhemchugov@p8.f822.n463.z2.fidonet.org>

