Summary:	Namespace-aware XML parser written in TeX
Name:		xmltex
Version:	20000118
Release:	1
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/macros/xmltex/base.tar.gz
##Source0:	ftp://ftp.tex.ac.uk/tex-archive/macros/xmltex/base.zip
Autoreqprov:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Namespace-aware XML parser written in TeX

%prep
%setup -q -c %{name}-%{version}
mv -f base/* .
rmdir base

%build
pdftex -ini "&pdflatex" pdfxmltex.ini

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/pdftex/xmltex
install -d $RPM_BUILD_ROOT%{_bindir}

install pdf%{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/pdftex/%{name}
ln -s tex ${RPM_BUILD_ROOT}%{_bindir}/pdf%{name}

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
%{_datadir}/texmf/pdftex/*
