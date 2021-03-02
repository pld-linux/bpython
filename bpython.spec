# TODO:
# - check docs folder for valuable files
#
Summary:	bpython - a fancy interface to the Python interpreter
Summary(pl.UTF-8):	bpython - fantazyjny interfejs do interpretera Pythona
Name:		bpython
Version:	0.9.7.1
Release:	4
License:	MIT
Group:		Applications/Shells
Source0:	http://bpython-interpreter.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f32ce6aa8ae6af8d2cf65e13f58859d4
URL:		http://bpython-interpreter.org/
BuildRequires:	pydoc
BuildRequires:	python-devel
BuildRequires:	python-devel-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-bpython = %{version}-%{release}
Requires:	python-distribute >= 0.6.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems.

%description -l pl.UTF-8
bpython to fantazyjny interfejs do interpretera Pythona przeznaczony
dla uniksowych systemów operacyjnych.

%package gtk
Summary:	GTK+ bpython interface
Summary(pl.UTF-8):	Interfejs GTK+ bpythona
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.0

%description gtk
GTK+ bpython interface.

%description gtk -l pl.UTF-8
Interfejs GTK+ bpythona.

%package -n python-bpython
Summary:	bpython shell modules
Summary(pl.UTF-8):	Moduły powłoki bpython
Group:		Libraries/Python
Requires:	python-pygments
%pyrequires_eq	pydoc
%pyrequires_eq	python-devel-tools

%description -n python-bpython
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems.

%description -n python-bpython -l pl.UTF-8
bpython to fantazyjny interfejs do interpretera Pythona przeznaczony
dla uniksowych systemów operacyjnych.

%package -n python-bpdb
Summary:	bpdb module - PDB extension
Summary(pl.UTF-8):	Moduł bpdb - rozszerzenie PDB
Group:		Libraries/Python
Requires:	python-bpython = %{version}-%{release}
%pyrequires_eq	pydoc
%pyrequires_eq	python-devel-tools

%description -n python-bpdb
BPDB is an extension to PDB which allows you to press B in a PDB
session which will let you be dropped into a bpython sessions with the
current PDB locals().

%description -n python-bpdb -l pl.UTF-8
BPDB to rozszerzenie PDB pozwalające nacisnąć B w sesji PDB, aby
przejść do sesji bpythona z bieżącą zawartością locals() z PDB.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bpython
%{_desktopdir}/bpython.desktop
%{_mandir}/man1/bpython.1*
%{_mandir}/man5/bpython-config.5*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bpython-gtk

%files -n python-bpython
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README ROADMAP TODO
%{py_sitescriptdir}/bpython
%{py_sitescriptdir}/bpython-%{version}-py*.egg-info

%files -n python-bpdb
%defattr(644,root,root,755)
%{py_sitescriptdir}/bpdb
