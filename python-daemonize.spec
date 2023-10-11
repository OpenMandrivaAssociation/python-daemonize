# Created by pyp2rpm-3.3.4
%global pypi_name daemonize

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        %mkrel 4
Summary:        Library to enable your code run as a daemon process on Unix-like systems
Group:          Development/Python
License:        MIT
URL:            https://github.com/thesharp/daemonize
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Daemonize is a library for writing system daemons in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Daemonize is a library for writing system daemons in Python.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%doc html
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
