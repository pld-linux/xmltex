Summary:	Namespace-aware XML parser written in TeX
Name:		xmltex
Version:	20000118
Release:	5
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.tex.ac.uk/tex-archive/macros/%{name}.tar.gz
Requires:	/usr/bin/pdftex
Requires:	/usr/bin/tex
%requires_eq	tetex
%requires_eq	tetex-pdftex
Autoreqprov:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Namespace-aware XML parser written in TeX

%prep
%setup -q -c %{name}-%{version}
mv -f xmltex/base/* .


%build
pdftex -ini "&pdflatex" pdfxmltex.ini
tex -ini "&hugelatex" xmltex.ini

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/{tex/xmltex,web2c},%{_bindir}}

install *.xmt $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install %{name}.cfg $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install pdf%{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/
install %{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/

ln -s pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdf%{name}
ln -s tex ${RPM_BUILD_ROOT}%{_bindir}/%{name}

gzip -9nf readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postin
cat >> /usr/share/texmf/web2c/texmf.cnf  << END

% xmltext & pdfxmltex config 

TEXINPUTS.pdfxmltex   = .;$TEXMF/{pdftex,tex}/{xmltex,latex,generic,}//
% xmltex & pdfxmltex
 main_memory.xmltex = 1500000
 param_size.xmltex = 1500
 stack_size.xmltex = 1500
 hash_extra.xmltex = 50000
 string_vacancies.xmltex = 45000
 pool_free.xmltex = 47500
 nest_size.xmltex = 500
 save_size.xmltex = 10000
 pool_size.xmltex = 500000
 max_strings.xmltex = 55000
 main_memory.pdfxmltex = 2500000
 param_size.pdfxmltex = 1500
 stack_size.pdfxmltex = 1500
 hash_extra.pdfxmltex = 50000
 string_vacancies.pdfxmltex = 45000
 pool_free.pdfxmltex = 47500
 nest_size.pdfxmltex = 500
 save_size.pdfxmltex = 10000
 pool_size.pdfxmltex = 500000
 max_strings.pdfxmltex = 55000
 % end of xmltex config
END

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc *.gz *.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/xmltex
