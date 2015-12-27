# TODO: package the vim syntax file.
Summary:	A tool for converting text files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików tekstowych do różnych formatów
Name:		asciidoc
Version:	8.6.9
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/asciidoc/%{name}-%{version}.tar.gz
# Source0-md5:	c59018f105be8d022714b826b0be130a
URL:		http://www.methods.co.nz/asciidoc/index.html
BuildRequires:	rpm-pythonprov
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

sed -i -e '1s|^#!/usr/bin/env python|#!%{__python}|' asciidoc.py a2x.py \
	filters/code/code-filter.py \
	filters/latex/latex2png.py \
	filters/music/music2png.py \
	filters/graphviz/graphviz2png.py

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT%{sysconfdir}/{dblatex,docbook-xsl,filters/{code,graphviz,latex,music,source},stylesheets}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{images/icons/callouts,javascripts}

cp -p asciidoc.py $RPM_BUILD_ROOT%{_bindir}/asciidoc
cp -p a2x.py $RPM_BUILD_ROOT%{_bindir}/a2x
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -p *.conf $RPM_BUILD_ROOT%{sysconfdir}
cp -p dblatex/*.{xsl,sty} $RPM_BUILD_ROOT%{sysconfdir}/dblatex
cp -p docbook-xsl/*.xsl $RPM_BUILD_ROOT%{sysconfdir}/docbook-xsl
cp -p filters/code/*.{py,conf} $RPM_BUILD_ROOT%{sysconfdir}/filters/code
cp -p filters/graphviz/*.{py,conf} $RPM_BUILD_ROOT%{sysconfdir}/filters/graphviz
cp -p filters/latex/*.{py,conf} $RPM_BUILD_ROOT%{sysconfdir}/filters/latex
cp -p filters/music/*.{py,conf} $RPM_BUILD_ROOT%{sysconfdir}/filters/music
cp -p filters/source/*.conf $RPM_BUILD_ROOT%{sysconfdir}/filters/source
cp -p stylesheets/*.css $RPM_BUILD_ROOT%{sysconfdir}/stylesheets
ln -s %{_datadir}/%{name}/images $RPM_BUILD_ROOT%{sysconfdir}/images
ln -s %{_datadir}/%{name}/javascripts $RPM_BUILD_ROOT%{sysconfdir}/javascripts
cp -p images/icons/callouts/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images/icons/callouts
cp -p images/icons/README images/icons/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/images/icons
cp -p javascripts/*.js $RPM_BUILD_ROOT%{_datadir}/%{name}/javascripts

#    if [ -d $VIM_RPM_BUILD_ROOT%{sysconfdir} ]; then
#        install -d $VIM_RPM_BUILD_ROOT%{sysconfdir}/syntax
#        install -m 644 vim/syntax/asciidoc.vim \
#                       $VIM_RPM_BUILD_ROOT%{sysconfdir}/syntax/asciidoc.vim
#        install -d $VIM_RPM_BUILD_ROOT%{sysconfdir}/ftdetect
#        install -m 644 vim/ftdetect/asciidoc_filetype.vim \
#                       $VIM_RPM_BUILD_ROOT%{sysconfdir}/ftdetect/asciidoc_filetype.vim
#    fi
%{__rm} -r examples/website

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG COPYRIGHT README doc/asciidoc.txt examples
%attr(755,root,root) %{_bindir}/a2x
%attr(755,root,root) %{_bindir}/asciidoc
%dir %{sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/*.conf
%dir %{sysconfdir}/dblatex
%{sysconfdir}/dblatex/*.sty
%{sysconfdir}/dblatex/*.xsl
%dir %{sysconfdir}/docbook-xsl
%{sysconfdir}/docbook-xsl/*.xsl
%dir %{sysconfdir}/filters
%dir %{sysconfdir}/filters/code
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/filters/code/code-filter.conf
%attr(755,root,root) %{sysconfdir}/filters/code/code-filter.py
%dir %{sysconfdir}/filters/graphviz
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/filters/graphviz/graphviz-filter.conf
%attr(755,root,root) %{sysconfdir}/filters/graphviz/graphviz2png.py
%dir %{sysconfdir}/filters/music
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/filters/music/music-filter.conf
%attr(755,root,root) %{sysconfdir}/filters/music/music2png.py
%dir %{sysconfdir}/filters/source
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/filters/source/source-highlight-filter.conf
%dir %{sysconfdir}/filters/latex
%config(noreplace) %verify(not md5 mtime size) %{sysconfdir}/filters/latex/latex-filter.conf
%attr(755,root,root) %{sysconfdir}/filters/latex/latex2png.py
%{sysconfdir}/images
%{sysconfdir}/javascripts
%dir %{sysconfdir}/stylesheets
%{sysconfdir}/stylesheets/*.css
%{_datadir}/%{name}
%{_mandir}/man1/a2x.1*
%{_mandir}/man1/asciidoc.1*
