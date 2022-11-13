Name:		texlive-varsfromjobname
Version:	44154
Release:	1
Summary:	Extract variables from the name of the LaTeX file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/varsfromjobname
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varsfromjobname.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varsfromjobname.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to extract information from the job
name, provided that the name has been structured appropriately:
the package expects the file name to consist of a set of words
separated by hyphens.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/varsfromjobname
%doc %{_texmfdistdir}/doc/latex/varsfromjobname

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
