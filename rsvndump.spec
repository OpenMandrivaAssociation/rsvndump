Summary:	Remote Subversion repository dump
Name:		rsvndump
Version:	0.6
Release:	2
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


%changelog
* Mon May 21 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.6-1
+ Revision: 799750
- update to 0.6

* Tue Mar 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.8-1
+ Revision: 784582
- version update 0.5.8

* Sun Jul 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-1
+ Revision: 690177
- 0.5.6

* Mon Mar 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-1
+ Revision: 642434
- 0.5.5

* Thu Feb 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.4-1
+ Revision: 638151
- 0.5.4

* Thu Dec 02 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.5.3-2mdv2011.0
+ Revision: 605308
- Rebuild with apr with workaround to issue with gcc type based

* Sat Dec 19 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-1mdv2010.1
+ Revision: 480134
- 0.5.3

* Sat Jul 25 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdv2010.0
+ Revision: 399786
- 0.5.2

* Sun Jul 12 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdv2010.0
+ Revision: 395119
- import rsvndump


* Sun Jul 12 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdv2009.0
- initial Mandriva package
