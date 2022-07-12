Name: c_helloworld
Version: 1.0
Release: alt1

Summary: helloworld

License: license
Group: group

Source: helloworld.c

BuildArch: noarch

%description
description

%prep

%build
gcc %SOURCE0 -o %name

%install
mkdir -p %buildroot%_bindir
install -m755 %{SOURCE0} %buildroot%_bindir/

%files
%_bindir/helloworld.c
