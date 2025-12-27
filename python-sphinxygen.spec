%define	pyname	sphinxygen	

Summary:	A script to generate Sphinx ReST from Doxygen XML
Name:	python-%{pyname}
Version:	1.0.12
Release:	1
License:	ISC
Group:	Development/Python
Url:		https://gitlab.com/drobilla/sphinxygen
Source0:	https://files.pythonhosted.org/packages/94/9f/f773d81507df80867e674653adbde56087b75e90d0453ef22f02fb25d725/%{pyname}-%{version}.tar.gz
BuildRequires:		python
BuildRequires:		python-pyproject-api
BuildRequires:		python-setuptools
BuildRequires:		python-setuptools_scm
#Requires:	doxygen
BuildArch:	noarch

%description
A python script to generate Sphinx ReST from Doxygen XML.

%files
%doc README.md
%license LICENSES/*.txt
%{_bindir}/%{pyname}
%{py_puresitedir}/%{pyname}
%{py_puresitedir}/%{pyname}-%{version}.dist-info

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pyname}-%{version}


%build
%py_build


%install
%py_install
