
#
# TODO: 
# - split into format packages
#

Summary:	Namespace-aware XML parser written in TeX
Summary(pl):	Uwzglêdniaj±cy przestrzenie nazw parser XML napisany w TeXu
Name:		xmltex
Version:	20020625
Release:	3
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.tex.ac.uk/tex-archive/macros/%{name}.tar.gz
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-format-pdftex
BuildRequires:	tetex-format-pdflatex
Requires(post):	grep
Requires(post):	textutils
Requires(post,postun):	/usr/bin/texhash
Autoreqprov:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Namespace-aware XML parser written in TeX.

%description -l pl
Uwzglêdniaj±cy przestrzenie nazw parser XML napisany w TeXu.

%prep
%setup -q -c %{name}-%{version}
mv -f xmltex/base/* .

%build
pdftex -ini "&pdflatex" pdfxmltex.ini
tex -ini "&latex" xmltex.ini

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/{tex/xmltex,web2c},%{_bindir}}

install *.xmt $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install %{name}.cfg $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install pdf%{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/
install %{name}.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/

ln -sf pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdf%{name}
ln -sf tex ${RPM_BUILD_ROOT}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

if ! grep -q 'TEXINPUTS\.pdfxmltex' /usr/share/texmf/web2c ; then
cat >> /usr/share/texmf/web2c/texmf.cnf  << END

% xmltext & pdfxmltex config

TEXINPUTS.pdfxmltex   = .;\$TEXMF/{pdftex,tex}/{xmltex,latex,generic,}//
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
fi

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc readme.txt *.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/xmltex
