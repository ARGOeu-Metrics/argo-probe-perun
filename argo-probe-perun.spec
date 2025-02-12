%define dir /usr/libexec/argo/probes/perun

Summary:   ARGO probe for EGI Perun service
Name:      argo-probe-perun
Version:   0.9.0
Release:   1%{?dist}
License:   ASL 2.0
Group:     Network/Monitoring
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch


%description
Package contains probe check_perun that checks Perun service


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./check_perun  ${RPM_BUILD_ROOT}%{dir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{dir}


%changelog
* Thu Jun 27 2024 Katarina Zailac <kzailac@srce.hr> - 0.9.0-1%{?dist}
- AO-977 Move check_perun probe to separate package
