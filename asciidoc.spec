Summary:	A tool for converting text files to various formats
Summary(pl):	Narzêdzie do konwersji plików tekstowych do ró¿nych formatów
Name:		asciidoc
Version:	7.0.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.methods.co.nz/asciidoc/%{name}-%{version}.tar.gz
# Source0-md5:	fdce1bb38f9ec8b333ced4f22f5e95a0
URL:		http://www.methods.co.nz/asciidoc/index.html
Requires:	python >= 2.3
Requires:	python-modules >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/asciidoc

%description
AsciiDoc is a text document format for writing short documents,
articles, books and UNIX man pages. AsciiDoc files can be translated
to HTML (with or without stylesheets), DocBook and LinuxDoc markup
using the asciidoc(1) command. AsciiDoc is highly configurable: both
the AsciiDoc source file syntax and the backend output markups (which
can be almost any type of SGML/XML markup) can be customized and
extended by the user.

%description -l pl
AsciiDoc jest formatem dokumentów tekstowych do pisania krótkich
dokumentów, artyku³ów, ksi±¿ek i podrêczników systemu UNIX. Pliki
AsciiDoc mog± byæ t³umaczone do HTML-a (z lub bez CSS), DocBooka i
LinuxDoca u¿ywaj±c polecenia asciidoc(1). AsciiDoc jest wysoce
konfigurowalny: zarówno sk³adnia plików ¼ród³owych, jak i znaczniki
backendów (które mog± byæ dowolnego typu SGML/XML) mog± byæ
dostosowywane i rozszerzane przez u¿ytkownika.

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
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/asciidoc.py
%{_datadir}/%{name}/filters
%{_datadir}/%{name}/images
%{_datadir}/%{name}/stylesheets
%{_mandir}/man1/*
