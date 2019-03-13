Summary: A utility to collect various Lustre performance data
Name: collectl-lustre
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2+ or Artistic
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/matthdan/collectl-lustre
BuildArch: noarch
Requires: collectl

%description
A utility to collect Lustre performance data

%prep
%setup -q -n %{name}-%{version}

%build
# nothing to do

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/collectl

install -p -m 644 LustreCommon.pm $RPM_BUILD_ROOT%{_datadir}/collectl/
install -p -m 644 LustreSingleton.pm $RPM_BUILD_ROOT%{_datadir}/collectl/
install -p -m 644 lustreClient.ph $RPM_BUILD_ROOT%{_datadir}/collectl/
install -p -m 644 lustreMDS.ph $RPM_BUILD_ROOT%{_datadir}/collectl/
install -p -m 644 lustreOSS.ph $RPM_BUILD_ROOT%{_datadir}/collectl/

%files
%{_datadir}/collectl/LustreCommon.pm
%{_datadir}/collectl/LustreSingleton.pm
%{_datadir}/collectl/lustreClient.ph
%{_datadir}/collectl/lustreMDS.ph
%{_datadir}/collectl/lustreOSS.ph

%changelog
* Tue Mar 12 2019 Matth DANIEL <matth.daniel@gmail.com> - 1.0.0-1
- initial packaging based upon upstream srpm
