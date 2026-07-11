%global tl_name yazd-thesis
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	A template for the Yazd University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/yazd-thesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yazd-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yazd-thesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers a document class for typesetting theses and
dissertations at the Yazd University. The class requires use of XeLaTeX.

