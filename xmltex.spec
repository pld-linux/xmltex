Summary:	Namespace-aware XML parser written in TeX
Name:		xmltex
Version:	20000118
Release:	2
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
##Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/macros/xmltex/base.tar.gz
Source0:	ftp://ftp.tex.ac.uk/tex-archive/macros/xmltex.tar.gz
Requires:	/usr/bin/pdftex
Requires:	/usr/bin/tex
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
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/web2c
install -d $RPM_BUILD_ROOT%{_bindir}

install *.xmt $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install pdf%{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/
install %{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/
ln -s pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdf%{name}
ln -s tex ${RPM_BUILD_ROOT}%{_bindir}/%{name}

gzip -9nf readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc *.gz *.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
