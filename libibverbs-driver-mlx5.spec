# NOTE: for versions >= 17 see rdma-core.spec
Summary:	Userspace driver for the Mellanox Connect-IB InfiniBand HCAs
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart Mellanox Connect-IB InfiniBand HCA
Name:		libibverbs-driver-mlx5
Version:	1.2.1
Release:	1.1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/mlx5/libmlx5-%{version}.tar.gz
# Source0-md5:	eecd015a2c4f2452a0a1cbc121b40712
URL:		https://www.openfabrics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libibverbs-devel >= 1.1.8
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
Requires:	libibverbs >= 1.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmlx5 is a userspace driver for Mellanox Connect-IB InfiniBand
HCAs.  It works as a plug-in module for libibverbs that allows
programs to use Mellanox hardware directly from userspace.

Currently the driver supports HCAs on PCI Express interface based on
MT27600 Connect-IB chip, using mlx5_ib kernel driver.

%description -l pl.UTF-8
libmlx5 to sterownik przestrzeni użytkownika dla kart Mellanox
Connect-IB InfiniBand HCA. Działa jako moduł ładowany przez
libibverbs, pozwalający programom na dostęp z przestrzeni użytkownika
do sprzętu Mellanox.

Obecnie sterownik obsługuje kontrolery HCA na szynie PCI Express
oparte na układzie MT27600 Connect-IB poprzez sterownik jądra mlx5_ib.

%package static
Summary:	Static version of mlx5 driver
Summary(pl.UTF-8):	Statyczna wersja sterownika mlx5
Group:		Development/Libraries
Requires:	libibverbs-static >= 1.1.8

%description static
Static version of mlx5 driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika mlx5, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libmlx5-%{version}

# don't fail on "statement with no effect" warning
#%{__sed} -i -e 's/ -Werror//' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmlx5.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libmlx5-rdmav2.so
%{_sysconfdir}/libibverbs.d/mlx5.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libmlx5.a
