# TODO:
# - check docs folder for valuable files
#
%define		pname	bpython
Summary:	bpython - a fancy interface to the Python interpreter
Name:		bpython
Version:	0.9.7.1
Release:	1
License:	MIT
Group:		Applications/Shells
Source0:	http://bpython-interpreter.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f32ce6aa8ae6af8d2cf65e13f58859d4
URL:		http://bpython-interpreter.org/
BuildRequires:	pydoc
BuildRequires:	python-devel
BuildRequires:	python-devel-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-distribute >= 0.6.10
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

%package -n python-bpdb
Summary:	bpdb module
Group:		Libraries/Python
%pyrequires_eq	python-devel-tools
%pyrequires_eq	pydoc

%description -n python-bpdb
BPDB is an extension to PDB which allows you to press B in a PDB
session which will let you be dropped into a bpython sessions with the
current PDB locals()

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

%files -n python-bpdb
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/bpdb
