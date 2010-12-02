Summary:	Remote Subversion repository dump
Name:		rsvndump
Version:	0.5.3
Release:	%mkrel 2
License:	GPLv3
Group:		System/Servers
URL:		http://rsvndump.sourceforge.net/
Source0:	http://rsvndump.sourceforge.net/%{name}-%{version}.tar.gz
BuildRequires:	apr-devel
BuildRequires:	subversion-devel
BuildRequires:	gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rsvndump is a command line tool that is able to dump a subversion repository
that resides on a remote server. All data is dumped in the format that can be
read/written by svnadmin, so the data produced by rsvndump can easily be
imported into a new subversion repository.

%prep

%setup -q


%build
%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}


%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog THANKS doc/rsvndump.txt
%{_bindir}/rsvndump

