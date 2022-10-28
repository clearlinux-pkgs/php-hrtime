#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-hrtime
Version  : 0.6.0
Release  : 24
URL      : https://pecl.php.net//get/hrtime-0.6.0.tgz
Source0  : https://pecl.php.net//get/hrtime-0.6.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-hrtime-lib = %{version}-%{release}
BuildRequires : buildreq-php
Patch1: PHP-8.patch

%description
# High resolution timer for PHP #
This PHP extension brings the possibility to use a high resolution timer from the user land PHP scripts. The best available APIs are used on differend platforms to achieve this goal.

%package lib
Summary: lib components for the php-hrtime package.
Group: Libraries

%description lib
lib components for the php-hrtime package.


%prep
%setup -q -n hrtime-0.6.0
cd %{_builddir}/hrtime-0.6.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/hrtime.so
