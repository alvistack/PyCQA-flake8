%global debug_package %{nil}

Name: python-flake8
Epoch: 100
Version: 3.9.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Python code checking using pyflakes, pycodestyle, and mccabe
License: MIT
URL: https://github.com/PyCQA/flake8/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Flake8 is a wrapper around PyFlakes, pycodestyle, and Ned's McCabe
script. It runs all the tools by launching the single flake8 script, and
displays the warnings in a per-file, merged output.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-flake8
Summary: Python code checking using pyflakes, pycodestyle, and mccabe
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-mccabe >= 0.6.0
Requires: python3-pycodestyle >= 2.7.0
Requires: python3-pyflakes >= 2.3.0
Provides: python3-flake8 = %{epoch}:%{version}-%{release}
Provides: python3dist(flake8) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flake8 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flake8) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flake8 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flake8) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-flake8
Flake8 is a wrapper around PyFlakes, pycodestyle, and Ned's McCabe
script. It runs all the tools by launching the single flake8 script, and
displays the warnings in a per-file, merged output.

%files -n python%{python3_version_nodots}-flake8
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-flake8
Summary: Python code checking using pyflakes, pycodestyle, and mccabe
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-mccabe >= 0.6.0
Requires: python3-pycodestyle >= 2.7.0
Requires: python3-pyflakes >= 2.3.0
Provides: python3-flake8 = %{epoch}:%{version}-%{release}
Provides: python3dist(flake8) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flake8 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flake8) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flake8 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flake8) = %{epoch}:%{version}-%{release}

%description -n python3-flake8
Flake8 is a wrapper around PyFlakes, pycodestyle, and Ned's McCabe
script. It runs all the tools by launching the single flake8 script, and
displays the warnings in a per-file, merged output.

%files -n python3-flake8
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
