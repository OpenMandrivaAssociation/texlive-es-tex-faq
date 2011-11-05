# revision 15878
# category Package
# catalog-ctan /help/es-tex-faq
# catalog-date 2006-10-29 10:21:33 +0100
# catalog-license lppl
# catalog-version 1.97
Name:		texlive-es-tex-faq
Version:	1.97
Release:	1
Summary:	CervanTeX (Spanish TeX Group) FAQ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/help/es-tex-faq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/es-tex-faq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/es-tex-faq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
SGML source, converted LaTeX version, and readable copies of
the FAQ from the Spanish TeX users group.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/es-tex-faq/FAQ-CervanTeX.html
%doc %{_texmfdistdir}/doc/generic/es-tex-faq/FAQ-CervanTeX.latin1
%doc %{_texmfdistdir}/doc/generic/es-tex-faq/FAQ-CervanTeX.pdf
%doc %{_texmfdistdir}/doc/generic/es-tex-faq/FAQ-CervanTeX.sgml
%doc %{_texmfdistdir}/doc/generic/es-tex-faq/FAQ-CervanTeX.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
