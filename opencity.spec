#
# TODO:
# - unpackaged files:
#    /etc/opencity/config/graphism.conf
#    /etc/opencity/config/graphism.xml
#    /etc/opencity/config/opencity.xml
# - pass rpm*flags
#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
#
Summary:	A 3D city simulator
Summary(hu.UTF-8):	3D-s városépítő szimulátor
Summary(pl.UTF-8):	Trójwymiarowy symulator miasta
Name:		opencity
Version:	0.0.6.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/opencity/%{name}-%{version}stable.tar.bz2
# Source0-md5:	d42d592019c27b9e10dbba51846826f1
Patch0:		%{name}-config_dir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-as-needed.patch
URL:		http://www.opencity.info/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.12
BuildRequires:	SDL_image-devel
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel}
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCity is a 3D city simulator game project written in standard C++
with OpenGL and SDL. It is not intended to be a clone of any famous
city simulator from Max*s.

%description -l hu.UTF-8
OpenCity egy 3D-s város-szimulátor játék, amely C++ nyelven írodott,
OpenGL és SDL könyvtárak használatával. Nem akar klónja lenni
bármelyik híres városépítő játéknak sem a Max*s-tól.

%description -l pl.UTF-8
OpenCity jest trójwymiarowym symulatorem miasta napisanym w
standardowym C++ z obsługą OpenGL i SDL. Projekt nie jest klonem
żadnego z popularnych symulatorów miast firmy Max*s.

%prep
%setup -q -n %{name}-%{version}stable
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_SDL_mixer:--disable-sdl-mixer}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/config,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a config/{*.conf,*.xml} $RPM_BUILD_ROOT%{_datadir}/%{name}/config
cp -a opencity.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a opencity.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/*.txt
%attr(755,root,root) %{_bindir}/opencity
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man6/opencity.6*
