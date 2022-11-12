Name:		texlive-es-tex-faq
Version:	15878
Release:	1
Summary:	CervanTeX (Spanish TeX Group) FAQ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/help/es-tex-faq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/es-tex-faq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/es-tex-faq.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
