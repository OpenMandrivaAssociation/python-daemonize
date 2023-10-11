# Created by pyp2rpm-3.3.4
%global pypi_name daemonize

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        1
Summary:        Library to enable your code run as a daemon process on Unix-like systems
Group:          Development/Python
License:        MIT
URL:            https://github.com/thesharp/daemonize
Source0:        https://pypi.io/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Daemonize is a library for writing system daemons in Python.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

%build
%py_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%files
%license LICENSE
%doc README.rst
%doc html
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
