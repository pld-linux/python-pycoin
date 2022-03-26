#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define		module	pycoin
Summary:	Bitcoin utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa Bitcoin
Name:		python-pycoin
Version:	0.24
Release:	14
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/richardkiss/pycoin/releases
#TODO: use	https://github.com/richardkiss/pycoin/archive/%{version}/pycoin-%{version}.tar.gz
Source0:	https://github.com/richardkiss/pycoin/archive/%{version}.tar.gz
# Source0-md5:	512f17827323eb1ba2bfe7952829575d
URL:		https://github.com/richardkiss/pycoin
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an implementation of a bunch of utility routines that may be
useful when dealing with Bitcoin stuff.

%description -l pl.UTF-8
Implementacja zbioru funkcji narzędziowych, które mogą być przydatne
przy operowaniu na Bitcoinach.

%package -n python3-%{module}
Summary:	Bitcoin utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa Bitcoin
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This is an implementation of a bunch of utility routines that may be
useful when dealing with Bitcoin stuff.

%description -n python3-%{module} -l pl.UTF-8
Implementacja zbioru funkcji narzędziowych, które mogą być przydatne
przy operowaniu na Bitcoinach.

%package -n %{module}
Summary:	Bitcoin utility library - tools
Summary(pl.UTF-8):	Biblioteka narzędziowa Bitcoin - narzędzia
Group:		Libraries/Python
Requires:	python%{?with_python3:3}
Requires:	python%{?with_python3:3}-%{module} = %{version}-%{release}
Requires:	python%{?with_python3:3}-distribute

%description -n %{module}
Tools that use pycoin library.

%description -n %{module} -l pl.UTF-8
Narzędzia wykorzystująca bibliotekę pycoin.

%prep
%setup  -q -n pycoin-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_install
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*egg-info
%{_examplesdir}/python-%{module}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif

%files -n %{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bu
%attr(755,root,root) %{_bindir}/genwallet
%attr(755,root,root) %{_bindir}/spend
