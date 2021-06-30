# TODO: package the vim syntax file.
Summary:	A tool for converting text files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików tekstowych do różnych formatów
Name:		asciidoc
Version:	9.1.0
Release:	2
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/asciidoc/asciidoc/releases
Source0:	https://github.com/asciidoc-py/asciidoc-py/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	52fc3849e1f48d8764337ce2b355b2ff
URL:		https://asciidoc.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	/usr/bin/pygmentize
Requires:	docbook-dtd45-xml
Requires:	python3 >= 1:3.5
Requires:	python3-modules >= 1:3.5
Requires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgconfdir	%{_sysconfdir}/asciidoc

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
%setup -q -n %{name}-py-%{version}

%{__sed} -i -e '1s|^#!/usr/bin/env python3\?|#!%{__python3}|' asciidoc.py a2x.py \
	filters/code/code-filter.py \
	filters/latex/latex2img.py \
	filters/music/music2png.py \
	filters/graphviz/graphviz2png.py \
	filters/unwraplatex.py

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install directly instead of symlinks to .py
%{__mv} $RPM_BUILD_ROOT%{_bindir}/a2x{.py,}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/asciidoc{.py,}
# move constant data to /usr
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__mv} $RPM_BUILD_ROOT%{pkgconfdir}/{images,javascripts} $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -sf %{_datadir}/%{name}/images $RPM_BUILD_ROOT%{pkgconfdir}/images
ln -sf %{_datadir}/%{name}/javascripts $RPM_BUILD_ROOT%{pkgconfdir}/javascripts

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/testasciidoc.1

#    if [ -d $VIM_RPM_BUILD_ROOT%{sysconfdir} ]; then
#        install -d $VIM_RPM_BUILD_ROOT%{sysconfdir}/syntax
#        install -m 644 vim/syntax/asciidoc.vim \
#                       $VIM_RPM_BUILD_ROOT%{sysconfdir}/syntax/asciidoc.vim
#        install -d $VIM_RPM_BUILD_ROOT%{sysconfdir}/ftdetect
#        install -m 644 vim/ftdetect/asciidoc_filetype.vim \
#                       $VIM_RPM_BUILD_ROOT%{sysconfdir}/ftdetect/asciidoc_filetype.vim
#    fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.txt CHANGELOG.txt COPYRIGHT README.asciidoc doc/asciidoc.txt
%attr(755,root,root) %{_bindir}/a2x
%attr(755,root,root) %{_bindir}/asciidoc
%dir %{pkgconfdir}
%config(noreplace) %verify(not md5 mtime size) %{pkgconfdir}/*.conf
%dir %{pkgconfdir}/dblatex
%{pkgconfdir}/dblatex/*.sty
%{pkgconfdir}/dblatex/*.xsl
%dir %{pkgconfdir}/docbook-xsl
%{pkgconfdir}/docbook-xsl/*.xsl
%dir %{pkgconfdir}/filters
%dir %{pkgconfdir}/filters/code
%config(noreplace) %verify(not md5 mtime size) %{pkgconfdir}/filters/code/code-filter.conf
%attr(755,root,root) %{pkgconfdir}/filters/code/code-filter.py
%dir %{pkgconfdir}/filters/graphviz
%config(noreplace) %verify(not md5 mtime size) %{pkgconfdir}/filters/graphviz/graphviz-filter.conf
%attr(755,root,root) %{pkgconfdir}/filters/graphviz/graphviz2png.py
%dir %{pkgconfdir}/filters/music
%config(noreplace) %verify(not md5 mtime size) %{pkgconfdir}/filters/music/music-filter.conf
%attr(755,root,root) %{pkgconfdir}/filters/music/music2png.py
%dir %{pkgconfdir}/filters/source
%config(noreplace) %verify(not md5 mtime size) %{pkgconfdir}/filters/source/source-highlight-filter.conf
%dir %{pkgconfdir}/filters/latex
%config(noreplace) %verify(not md5 mtime size) %{pkgconfdir}/filters/latex/latex-filter.conf
%attr(755,root,root) %{pkgconfdir}/filters/latex/latex2img.py
%attr(755,root,root) %{pkgconfdir}/filters/unwraplatex.py
%{pkgconfdir}/images
%{pkgconfdir}/javascripts
%dir %{pkgconfdir}/stylesheets
%{pkgconfdir}/stylesheets/*.css
%{pkgconfdir}/themes
%{_datadir}/%{name}
%{_mandir}/man1/a2x.1*
%{_mandir}/man1/asciidoc.1*
