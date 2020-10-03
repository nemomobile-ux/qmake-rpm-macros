Name:           qmake-rpm-macros
Version:        1
Release:        0
Summary:        The common Qmake RPM macros
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package contains the unversioned Qmake RPM macros, that most
implementations should rely on.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 macros.qmake %{buildroot}%{_rpmmacrodir}
install -m 644 macros.nemomobile %{buildroot}%{_rpmmacrodir}

%files
%{_rpmmacrodir}/macros.qmake
%{_rpmmacrodir}/macros.nemomobile
