Name: num-of-files
Version: 1.0
Release: 1%{?dist}
Summary: Count files in /etc directory

License: MIT
URL: https://github.com/ShadowDrake21/Krapyvianskyi_OS
Source0: https://github.com/ShadowDrake21/Krapyvianskyi_OS/archive/main.zip

%description
A simple script to count files in /etc directory.

%prep
unzip %SOURCE0
cd Krapyvianskyi_OS-main/

%files
/usr/bin/num-of-files

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/Krapyvianskyi_OS-main/num-of-files.sh  %{buildroot}/usr/bin/num-of-files

%changelog
* Wed Nov 24 2023 Dmytro Krapyvianskyi <dimka670020040@gmail.com> - 1.0-1
- Initial release
