Summary:	Remote Subversion repository dump
Name:		rsvndump
Version:	0.6
Release:	1
License:	GPLv3
Group:		System/Servers
URL:		http://rsvndump.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/rsvndump/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	apr-devel
BuildRequires:	subversion-devel
BuildRequires:	gettext-devel

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
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog THANKS doc/rsvndump.txt
%{_bindir}/rsvndump
