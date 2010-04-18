# TODO:
# - check docs folder for valuable files
#
%define		pname	bpython
Summary:	bpython - a fancy interface to the Python interpreter
Name:		bpython
Version:	0.9.6.2
Release:	1
License:	MIT
Group:		Applications/Shells
Source0:	http://bpython-interpreter.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	d30fdb663fa9957c21c63108ed249b59
URL:		http://bpython-interpreter.org/
BuildRequires:	pydoc
BuildRequires:	python-devel
BuildRequires:	python-devel-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems.

%package -n python-bpython
Summary:	bpython shell modules
Group:		Libraries/Python
Requires:	python-pygments
%pyrequires_eq	python-devel-tools
%pyrequires_eq	pydoc

%description -n python-bpython
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%py_postclean
rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/bpython.desktop
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files -n python-bpython
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{pname}
%{py_sitescriptdir}/*.egg-info
