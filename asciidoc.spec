# TODO: package the vim syntax file.
Summary:	A tool for converting text files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików tekstowych do różnych formatów
Name:		asciidoc
Version:	10.2.0
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/asciidoc-py/asciidoc-py/releases
Source0:	https://github.com/asciidoc-py/asciidoc-py/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	dce6bfe35fd2fe4fc71e1ca8c8ead683
URL:		https://asciidoc.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	/usr/bin/pygmentize
Requires:	docbook-dtd45-xml
Requires:	python3 >= 1:3.5
Requires:	python3-modules >= 1:3.5
Requires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%{__sed} -i -e '1s|/usr/bin/env python3|%{__python3}|' \
	asciidoc/resources/filters/code/code-filter.py \
	asciidoc/resources/filters/graphviz/graphviz2png.py \
	asciidoc/resources/filters/latex/latex2img.py \
	asciidoc/resources/filters/music/music2png.py \
	asciidoc/resources/filters/unwraplatex.py

%build
# make man pages
%{__autoconf}
%configure
%{__make}

%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/a*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.adoc CHANGELOG.adoc COPYRIGHT README.md doc/{asciidoc,asciidocapi,asciimath}.txt
%attr(755,root,root) %{_bindir}/a2x
%attr(755,root,root) %{_bindir}/asciidoc
%dir %{py3_sitescriptdir}/asciidoc
%{py3_sitescriptdir}/asciidoc/*.py
%{py3_sitescriptdir}/asciidoc/__pycache__
%{py3_sitescriptdir}/asciidoc/blocks
%dir %{py3_sitescriptdir}/asciidoc/resources
%{py3_sitescriptdir}/asciidoc/resources/*.conf
%{py3_sitescriptdir}/asciidoc/resources/dblatex
%{py3_sitescriptdir}/asciidoc/resources/docbook-xsl
%dir %{py3_sitescriptdir}/asciidoc/resources/filters
%attr(755,root,root) %{py3_sitescriptdir}/asciidoc/resources/filters/unwraplatex.py
%{py3_sitescriptdir}/asciidoc/resources/filters/__pycache__
%dir %{py3_sitescriptdir}/asciidoc/resources/filters/code
%attr(755,root,root) %{py3_sitescriptdir}/asciidoc/resources/filters/code/code-filter.py
%{py3_sitescriptdir}/asciidoc/resources/filters/code/__pycache__
%{py3_sitescriptdir}/asciidoc/resources/filters/code/*.conf
%{py3_sitescriptdir}/asciidoc/resources/filters/code/*.txt
%dir %{py3_sitescriptdir}/asciidoc/resources/filters/graphviz
%attr(755,root,root) %{py3_sitescriptdir}/asciidoc/resources/filters/graphviz/graphviz2png.py
%{py3_sitescriptdir}/asciidoc/resources/filters/graphviz/__pycache__
%{py3_sitescriptdir}/asciidoc/resources/filters/graphviz/*.conf
%{py3_sitescriptdir}/asciidoc/resources/filters/graphviz/*.txt
%dir %{py3_sitescriptdir}/asciidoc/resources/filters/latex
%attr(755,root,root) %{py3_sitescriptdir}/asciidoc/resources/filters/latex/latex2img.py
%{py3_sitescriptdir}/asciidoc/resources/filters/latex/__pycache__
%{py3_sitescriptdir}/asciidoc/resources/filters/latex/*.conf
%dir %{py3_sitescriptdir}/asciidoc/resources/filters/music
%attr(755,root,root) %{py3_sitescriptdir}/asciidoc/resources/filters/music/music2png.py
%{py3_sitescriptdir}/asciidoc/resources/filters/music/__pycache__
%{py3_sitescriptdir}/asciidoc/resources/filters/music/*.conf
%{py3_sitescriptdir}/asciidoc/resources/filters/music/*.txt
%{py3_sitescriptdir}/asciidoc/resources/filters/source
%{py3_sitescriptdir}/asciidoc/resources/icons
%{py3_sitescriptdir}/asciidoc/resources/javascripts
%{py3_sitescriptdir}/asciidoc/resources/stylesheets
%{py3_sitescriptdir}/asciidoc/resources/themes
%{py3_sitescriptdir}/asciidoc-%{version}-py*.egg-info
%{_mandir}/man1/a2x.1*
%{_mandir}/man1/asciidoc.1*
