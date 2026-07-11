%global tl_name varsfromjobname
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Extract variables from the name of the LaTeX file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/varsfromjobname
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varsfromjobname.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varsfromjobname.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to extract information from the job name,
provided that the name has been structured appropriately: the package
expects the file name to consist of a set of words separated by hyphens.

