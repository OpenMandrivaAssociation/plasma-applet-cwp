%define oname	cwp
Summary:        Yet another weather plasmoid highly customizable this time
Name:           plasma-applet-cwp
Version:        1.10.1
Release:        1
Source0:        http://kde-look.org/CONTENT/content-files/98925-%{oname}-%{version}.tar.bz2
License:        GPLv3+
Group:          Graphical desktop/KDE
URL:            http://kde-look.org/content/show.php/Customizable+Weather+Plasmoid+(CWP)?content=98925
BuildRequires:  kdebase4-workspace-devel
Provides:       plasma-applet-customizable-weather
Requires:       kdebase4-workspace >= 4.11.4

%description
This is another weather plasmoid.
It aims to be highly customizable, but a little harder 
to setup than other weather plasmoids.
Nearly any weather forecast provider can be used, 
as long as the data is provided as html files (no flash).
The information how to extract the information 
from these html files is stored inside xml files.
Commands like grep, head, tail, sed, awk, 
... will do this job.

For now, xml files for the weather providers

%prep
%setup -qn %{oname}-%{version}
# deprecated
perl -pi -e "s|Encoding=UTF-8||"  plasma-applet-cwp.desktop
# fix attr
chmod 644 COPYING plasma-cwp.cpp plasma-cwp.h

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang plasma_applet_cwp

%files -f plasma_applet_cwp.lang
%doc COPYING ChangeLog README
%dir %{_kde_appsdir}/desktoptheme
%dir %{_kde_appsdir}/desktoptheme/default
%dir %{_kde_appsdir}/desktoptheme/default/widgets
%{_kde_appsdir}/desktoptheme/default/widgets/*.svgz
%{_kde_appsdir}/plasma-cwp/
%{_kde_iconsdir}/oxygen/128x128/status/weather-windy.png
%{_kde_iconsdir}/oxygen/scalable/status/weather-windy.svgz
%{_kde_libdir}/kde4/plasma_applet_cwp.so
%{_kde_services}/plasma-applet-cwp.desktop
