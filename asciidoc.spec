# TODO: package the vim syntax file.
Summary:	A tool for converting text files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików tekstowych do różnych formatów
Name:		asciidoc
Version:	8.2.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6810883dc0705aa6f9a4d621cf3e569c
URL:		http://www.methods.co.nz/asciidoc/index.html
BuildRequires:	sed >= 4.0
Requires:	python >= 2.3
Requires:	python-modules >= 2.3
Requires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		sysconfdir	/etc/asciidoc

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

%build
sed -i -e '1s|^#!/usr/bin/env python|#!/usr/bin/python|' asciidoc.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{sysconfdir}}
install -d $RPM_BUILD_ROOT%{sysconfdir}/{docbook-xsl,javascripts,filters,stylesheets}
install -d $RPM_BUILD_ROOT%{sysconfdir}/images/icons/callouts

install asciidoc.py $RPM_BUILD_ROOT%{_bindir}/asciidoc
install a2x $RPM_BUILD_ROOT%{_bindir}/a2x
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install *.conf $RPM_BUILD_ROOT%{sysconfdir}
install filters/*.py $RPM_BUILD_ROOT%{sysconfdir}/filters
install filters/*.conf $RPM_BUILD_ROOT%{sysconfdir}/filters
install docbook-xsl/*.xsl $RPM_BUILD_ROOT%{sysconfdir}/docbook-xsl
install stylesheets/*.css $RPM_BUILD_ROOT%{sysconfdir}/stylesheets
install javascripts/*.js $RPM_BUILD_ROOT%{sysconfdir}/javascripts
install images/icons/callouts/* $RPM_BUILD_ROOT%{sysconfdir}/images/icons/callouts
install images/icons/README images/icons/*.png $RPM_BUILD_ROOT%{sysconfdir}/images/icons

#    if [ -d $VIM_RPM_BUILD_ROOT%{sysconfdir} ]; then
#        install -d $VIM_RPM_BUILD_ROOT%{sysconfdir}/syntax
#        install -m 644 vim/syntax/asciidoc.vim \
#                       $VIM_RPM_BUILD_ROOT%{sysconfdir}/syntax/asciidoc.vim
#        install -d $VIM_RPM_BUILD_ROOT%{sysconfdir}/ftdetect
#        install -m 644 vim/ftdetect/asciidoc_filetype.vim \
#                       $VIM_RPM_BUILD_ROOT%{sysconfdir}/ftdetect/asciidoc_filetype.vim
#    fi
rm -rf examples/website

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README doc/asciidoc.html examples
%attr(755,root,root) %{_bindir}/*
%dir %{sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/*.conf
%{_mandir}/man1/*
