%define upstream_name 	 XML-Driver-HTML
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	SAX Driver for non wellformed HTML
License:	GPL	
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
XML::Driver::HTML is a SAX Driver for HTML. There is no need
for the HTML input to be weel formed, as XML::Driver::HTML
is generating its SAX events by walking a HTML::TreeBuilder object.
The simplest kind of use, is a filter from HTML to XHTML
using XML::Handler::YAWriter as a SAX Handler.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make


%install
install -d %{buildroot}%{perl_archlib}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README MANIFEST 
%{perl_vendorlib}/XML/Driver/HTML.pm
%{_mandir}/man1/html2xhtml.*
%{_mandir}/man3/XML::Driver::HTML.*
%{_bindir}/html2xhtml


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 401867
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-10mdv2009.0
+ Revision: 242198
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.06-8mdv2008.0
+ Revision: 64812
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-7mdv2008.0
+ Revision: 23531
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-6mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Fri Sep 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.06-5mdk
- rebuild

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.06-4mdk
- Use %%makeinstall_std now that it works on klama
- Remove PREFIX from Makefile.PL

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.06-3mdk
- Clean out Requires
- Use %%make
- Macroize
- Removal local detection of the archlib
- Use perl macros so it'll build across perl versions
- perllocal.pod
- URL
- Correct license, it's GPLed.

