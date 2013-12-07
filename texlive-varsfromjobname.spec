# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/varsfromjobname
# catalog-date 2009-01-12 09:20:39 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-varsfromjobname
Version:	0.5
Release:	5
Summary:	Extract variables from the name of the LaTeX file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/varsfromjobname
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varsfromjobname.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varsfromjobname.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/varsfromjobname/varsfromjobname.sty
%doc %{_texmfdistdir}/doc/latex/varsfromjobname/README
%doc %{_texmfdistdir}/doc/latex/varsfromjobname/varsfromjobname.pdf
%doc %{_texmfdistdir}/doc/latex/varsfromjobname/varsfromjobname.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 757392
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 719874
- texlive-varsfromjobname
- texlive-varsfromjobname
- texlive-varsfromjobname

