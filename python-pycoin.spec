#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
#
%define	module	pycoin
#
Summary:	Bitcoin utility library
Name:		python-pycoin
Version:	0.24
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/richardkiss/pycoin/archive/%{version}.tar.gz
# Source0-md5:	512f17827323eb1ba2bfe7952829575d
URL:		https://github.com/richardkiss/pycoin
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an implementation of a bunch of utility routines that may be
useful when dealing with Bitcoin stuff.

%package -n	python3-%{module}
Summary:	Bitcoin utility library
Group:		Libraries/Python
Requires:	python3

%description -n python3-%{module}
This is an implementation of a bunch of utility routines that may be
useful when dealing with Bitcoin stuff.

%package -n	%{module}
Summary:	Bitcoin utility library - tools
Group:		Libraries/Python
Requires:	python%{?with_python3:3}
Requires:	python%{?with_python3:3}-%{module} = %{version}-%{release}
Requires:	python%{?with_python3:3}-distribute

%description -n %{module}
Tools that use %{module} library.

%prep
%setup  -q -n pycoin-%{version}

%build
%if %{with python2}
%{__python} ./setup.py build --build-base py2
%endif
%if %{with python3}
%{__python3} ./setup.py build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%{__python} ./setup.py build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__python3} ./setup.py build \
	--build-base py3 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%{_examplesdir}/python-%{module}-%{version}
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%{_examplesdir}/python3-%{module}-%{version}
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*egg-info
%endif

%files -n %{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bu
%attr(755,root,root) %{_bindir}/genwallet
%attr(755,root,root) %{_bindir}/spend
