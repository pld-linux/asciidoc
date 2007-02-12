Summary:	A tool for converting text files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików tekstowych do różnych formatów
Name:		asciidoc
Version:	7.1.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.methods.co.nz/asciidoc/%{name}-%{version}.tar.gz
# Source0-md5:	554af81fb0e578a77ede4359ef79db69
URL:		http://www.methods.co.nz/asciidoc/index.html
Requires:	python >= 2.3
Requires:	python-modules >= 2.3
Requires:	xmlto
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

%description -l pl.UTF-8
AsciiDoc jest formatem dokumentów tekstowych do pisania krótkich
dokumentów, artykułów, książek i podręczników systemu UNIX. Pliki
AsciiDoc mogą być tłumaczone do HTML-a (z lub bez CSS), DocBooka i
LinuxDoca używając polecenia asciidoc(1). AsciiDoc jest wysoce
konfigurowalny: zarówno składnia plików źródłowych, jak i znaczniki
backendów (które mogą być dowolnego typu SGML/XML) mogą być
dostosowywane i rozszerzane przez użytkownika.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/asciidoc/{docbook-xsl,javascripts,filters,stylesheets}
install -d $RPM_BUILD_ROOT%{_datadir}/asciidoc/images/icons/callouts

install *.conf $RPM_BUILD_ROOT%{_sysconfdir}
install asciidoc.py $RPM_BUILD_ROOT%{_datadir}/%{name}
for i in docbook-xsl filters images javascripts stylesheets
do
	find $i -type f -exec install {} $RPM_BUILD_ROOT%{_datadir}/%{name}/{} \;;
done
install doc/asciidoc.1 $RPM_BUILD_ROOT%{_mandir}/man1
ln -sf %{_datadir}/asciidoc/asciidoc.py $RPM_BUILD_ROOT%{_bindir}/asciidoc
ln -sf %{_datadir}/%{name}/stylesheets $RPM_BUILD_ROOT%{_sysconfdir}/stylesheets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README doc/asciidoc.html examples
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/asciidoc.py
%{_datadir}/%{name}/docbook-xsl
%{_datadir}/%{name}/filters
%{_datadir}/%{name}/images
%{_datadir}/%{name}/javascripts
%{_datadir}/%{name}/stylesheets
%{_mandir}/man1/*
