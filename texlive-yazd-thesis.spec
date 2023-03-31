Name:		texlive-yazd-thesis
Version:	61719
Release:	2
Summary:	A template for the Yazd University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yazd-thesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yazd-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yazd-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers a document class for typesetting theses and
dissertations at the Yazd University. The class requires use of
XeLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/yazd-thesis
%doc %{_texmfdistdir}/doc/xelatex/yazd-thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
