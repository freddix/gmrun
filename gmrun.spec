Summary:	Application launcher
Name:		gmrun
Version:	0.9.2
Release:	12
License:	GPL v2
Group:		Applications
Source0:	http://heanet.dl.sourceforge.net/gmrun/%{name}-%{version}.tar.gz
# Source0-md5:	6cef37a968006d9496fc56a7099c603c
Patch0:		%{name}-gcc43.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-escaping.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small and fast, yet featureful application launcher for use under X11,
which uses GTK+ widget toolkit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's,^AC_PATH_STLPORT,dnl REMOVED ,g' configure.in
sed -i -e 's,@STLPORT_[A-Z]\+@,,g' src/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gmrun
%{_datadir}/%{name}

