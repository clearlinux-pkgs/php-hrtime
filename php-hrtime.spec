#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-hrtime
Version  : 0.6.0
Release  : 49
URL      : https://pecl.php.net//get/hrtime-0.6.0.tgz
Source0  : https://pecl.php.net//get/hrtime-0.6.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-hrtime-lib = %{version}-%{release}
Requires: php-hrtime-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: PHP-8.patch

%description
# High resolution timer for PHP #
This PHP extension brings the possibility to use a high resolution timer from the user land PHP scripts. The best available APIs are used on differend platforms to achieve this goal.

%package lib
Summary: lib components for the php-hrtime package.
Group: Libraries
Requires: php-hrtime-license = %{version}-%{release}

%description lib
lib components for the php-hrtime package.


%package license
Summary: license components for the php-hrtime package.
Group: Default

%description license
license components for the php-hrtime package.


%prep
%setup -q -n hrtime-0.6.0
cd %{_builddir}/hrtime-0.6.0
%patch -P 1 -p1
pushd ..
cp -a hrtime-0.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-hrtime
cp %{_builddir}/hrtime-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-hrtime/4f95a376df6f39604df0f21622b3fc8c6b43fc7a || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/hrtime.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-hrtime/4f95a376df6f39604df0f21622b3fc8c6b43fc7a
