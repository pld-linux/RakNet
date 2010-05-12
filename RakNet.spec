# NOTE
# - RakNet 3.x is available, but it is not under GPL License
#
%define		ver	%(echo %{version} | tr . _)
Summary:	Networking engine for game programmers
Summary(pl.UTF-8):	Silnik sieciowy dla programistów gier
Name:		RakNet
Version:	2.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.sumwars.org/data/Raknet%{ver}.tar.gz
# Source0-md5	bfdc95cf31d1381fb97631a3f07bc6c8
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-flags.patch
URL:		http://www.jenkinssoftware.com/
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RakNet is open source, networking engine for game programmers.

%description -l pl.UTF-8
RakNet jest otwartym, sieciowym silnikiem dla programistów gier.

%package devel
Summary:	Header files for RakNet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RakNet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for RakNet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RakNet.

%prep
%setup -q -n Raknet%{ver}
%undos Makefile Source/Makefile Source/RakVoice/Makefile
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/raknet
%attr(755,root,root) %{_libdir}/libraknet.so.*.*.*
%attr(755,root,root) %{_libdir}/librakvoice.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libraknet.so
%{_libdir}/librakvoice.so
%{_pkgconfigdir}/RakNet.pc
