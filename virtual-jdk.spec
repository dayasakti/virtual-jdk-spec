%define release_number 1
%define java_version 1.7

Version: %{java_version}
Name: virtual-jdk
Release: %{release_number}
Group: Development/Languages
Summary: Virtual package which provides 'jdk' package (such as provided by Oracle JDK) on top of the the Open JDK
License: None
BuildArch: noarch
Provides: jdk
Requires: java >= %{java_version}

%description
Virtual package which provides 'jdk' package (such as provided by Oracle JDK rpm) but on top of the Open JDK

%prep

%build

%pre

%post

%install

%files

%changelog
* Sat Jul 19 2014 dayasakti <dayasakti@github>
- Initial implementation
