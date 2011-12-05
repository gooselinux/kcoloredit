# Review Request:
# https://bugzilla.redhat.com/show_bug.cgi?id=432137

%define iversion 2.0.0

Name:           kcoloredit
Version:        4.3.3
Release:        2%{?dist}
Summary:        A color palette Editor

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://www.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/%{version}/src/extragear/kcoloredit-%{iversion}-kde%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  kde-filesystem >= 4
BuildRequires:  kdelibs4-devel >= 4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  cmake

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
Requires: kdelibs4 >= %{version}
Requires(post): xdg-utils
Requires(postun): xdg-utils
Requires:       %{name}-doc = %{version}-%{release}


%description
KColorEdit is a palette files editor. It can be used for editing 
color palettes and for color choosing and naming.

%package doc
Group:          System Environment/Libraries
Summary:        Documentation files for kcoloredit
BuildArch:      noarch

%description doc
This package includes the documentation for kcoloredit.

%prep
%setup -qn kcoloredit-%{iversion}-kde%{version}

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd


make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}

# validate desktop file
desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications/kde4 \
    %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop


%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :

%postun
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_kde4_bindir}/kcoloredit
%{_kde4_appsdir}/kcoloredit/
%{_kde4_datadir}/applications/kde4/kcoloredit.desktop
%{_kde4_iconsdir}/hicolor/*/*/kcoloredit.png

%files doc
%defattr(-,root,root,-)
%{_docdir}/HTML/*/kcoloredit/

%changelog
* Thu Jun 17 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.3-2
- Resolves: #605063 - RPMdiff run failed for package kcoloredit-4.3.3-1.el6
  (create a noarch doc subpackage to fix multilib issues)

* Thu Nov 05 2009 Sebastian Vahl <svahl@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Tue Sep 01 2009 Sebastian Vahl <svahl@fedoraproject.org> - 4.3.1-1
- 4.3.1

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 4.2.4-1
- 4.2.4

* Tue May 12 2009 Sebastian Vahl <fedora@deadbabylon.de> - 4.2.3-1
- 4.2.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Mon Nov 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.3-2
- dependency fixes, cosmetics

* Fri Nov 14 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Sat Oct 04 2008 Than Ngo <than@redhat.com> 4.1.2-1
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Thu Aug 28 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.1-1
- 4.1 (final)

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-1
- update to 4.0.3
- rebuild for NDEBUG and _kde4_libexecdir

* Tue Mar 04 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.2-1
- new upstream version: 4.0.2

* Thu Feb 14 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.1-2
- remove reference to KDE 4 in summary

* Fri Feb 08 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.1-1
- new upstream version: 4.0.1

* Fri Jan 25 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.0-1
- Initial version of kde-4.0.0 version
