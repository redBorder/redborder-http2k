Name: redborder-http2k
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder http2k initscripts and configuration.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-http2k
Source0: %{name}-%{version}.tar.gz

Requires: n2kafka
Requires: librb-http = 1.2.0

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/http2k.service %{buildroot}/usr/lib/systemd/system/http2k.service

%pre

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/http2k.service
%doc

%changelog
* Mon Aug 29 2016 Carlos J. Mateos <cjmateos@redborder.com> - 1.0.0-1
- first spec version
