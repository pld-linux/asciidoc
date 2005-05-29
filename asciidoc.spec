#
Summary:	A tool for converting text files to various formats
Summary(pl):	Narz�dzie do konwersji plik�w tekstowych do r�nych format�w
Name:		asciidoc
Version:	6.0.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.methods.co.nz/asciidoc/%{name}-%{version}.tar.gz
# Source0-md5:	7b8d918f68a24c1d13be6999248788f8
URL:		http://www.methods.co.nz/asciidoc/index.html
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/asciidoc

%description
AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages. AsciiDoc files can be translated to HTML (with
or without stylesheets), DocBook and LinuxDoc markup using the asciidoc(1)
command. AsciiDoc is highly configurable: both the AsciiDoc source file
syntax and the backend output markups (which can be almost any type
of SGML/XML markup) can be customized and extended by the user.

%description -l pl
AsciiDoc jest formatem dokument�w tekstowych do pisania kr�tkich dokument�w,
artyku��w, ksi��ek i podr�cznik�w systemu UNIX. Pliki AsciiDoc mog� by�
t�umaczone do HTML-u (z lub bez CSS), DocBook-a i LinuxDoc-a u�ywaj�c
polecenia asciidoc(1). AsciiDoc jest wysoce konfigurowalny: zar�wno sk�adnia
plik�w �r�d�owych, jak i znaczniki backend�w (kt�re mog� by� dowolnego typu
SGML/XML) mog� by� dostosowywane i rozszerzane przez u�ytkownika.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/asciidoc/{filters,stylesheets},%{_mandir}/man1,%{_sysconfdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/asciidoc/images/{callouts,jimmac,plain}

install *.conf $RPM_BUILD_ROOT%{_sysconfdir}
install asciidoc.py $RPM_BUILD_ROOT%{_datadir}/%{name}
find filters -type f -exec install {} $RPM_BUILD_ROOT%{_datadir}/%{name}/{} \;;
find images -type f -exec install {} $RPM_BUILD_ROOT%{_datadir}/%{name}/{} \;;
install doc/asciidoc.1 $RPM_BUILD_ROOT%{_mandir}/man1
ln -sf %{_datadir}/asciidoc/asciidoc.py $RPM_BUILD_ROOT%{_bindir}/asciidoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README
%dir %{_sysconfdir}
%config %{_sysconfdir}/*
%{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/asciidoc.py
%{_bindir}/%{name}
%{_mandir}/man1/*
