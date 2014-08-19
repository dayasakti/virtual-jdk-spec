virtual-jdk-spec
================

Virtual package which provides 'jdk' package (such as provided by Oracle JDK rpm) but on top of the Open JDK

Building RPM
================

```
rpmbuild -ba virtual-jdk.spec
```

Prerequisite
=============

RPMDEVTOOLS

to install:
```
yum -y install rpmdevtools
```
