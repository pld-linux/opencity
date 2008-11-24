#
# TODO:
# - unpackaged files:
#    /etc/opencity/config/graphism.conf
#    /etc/opencity/config/graphism.xml
#    /etc/opencity/config/opencity.xml
#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
#
Summary:	A 3D city simulator
Summary(pl.UTF-8):	Trójwymiarowy symulator miasta
Name:		opencity
Version:	0.0.6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/opencity/%{name}-%{version}stable.tar.bz2
# Source0-md5:	929fbe1c305dc0344c9915d8eb6c4dbc
Patch0:		%{name}-config_dir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-as-needed.patch
URL:		http://www.opencity.info/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.9
BuildRequires:	SDL_image-devel
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel}
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCity is a 3D city simulator game project written in standard C++
with OpenGL and SDL. It is not intended to be a clone of any famous
city simulator from Max*s.

%description -l pl.UTF-8
OpenCity jest trójwymiarowym symulatorem miasta napisanym w
standardowym C++ z obsługą OpenGL i SDL. Projekt nie jest klonem
żadnego z popularnych symulatorów miast firmy Max*s.

%prep
%setup -q -n %{name}-0.0.6stable
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

install config/{*.conf,*.xml} $RPM_BUILD_ROOT%{_datadir}/%{name}/config
install opencity.desktop $RPM_BUILD_ROOT%{_desktopdir}
install opencity.png $RPM_BUILD_ROOT%{_pixmapsdir}

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
