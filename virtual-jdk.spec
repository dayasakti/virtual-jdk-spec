%%define release_number 1
%%define java_version 1.7

Version: %{java_version}
Name: virtual-jdk
Release: %{release_number}
Group: Development/Languages
Summary: Virtual package which provides JDK package (such as provided by Oracle JDK) but uses the Open JDK
License: None
BuildArch: noarch
Provides: jdk
Requires: java >= %{java_version}

%description
Virtual package which provides JDK package (such as provided by Oracle JDK) but uses the Open JDK

%prep

%build

%pre

%post

%install

%files

%changelog
* 2014-07-19 dayasakti <dayasakti@github>
Initial implementation
