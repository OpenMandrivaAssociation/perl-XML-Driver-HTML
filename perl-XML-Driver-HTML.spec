%define upstream_name 	 XML-Driver-HTML
%define upstream_version 0.06
Name:		perl-%{upstream_name}
Version:	0.06
Release:	3

Summary:	SAX Driver for non wellformed HTML
License:	GPL	
Group:		Development/Perl
URL:		https://metacpan.org/dist/XML-Driver-HTML
Source0:	https://cpan.metacpan.org/authors/id/K/KR/KRAEHE/XML-Driver-HTML-0.06.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
XML::Driver::HTML is a SAX Driver for HTML. There is no need
for the HTML input to be weel formed, as XML::Driver::HTML
is generating its SAX events by walking a HTML::TreeBuilder object.
The simplest kind of use, is a filter from HTML to XHTML
using XML::Handler::YAWriter as a SAX Handler.

%prep
%setup -q -n XML-Driver-HTML-0.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make


%install
install -d %{buildroot}%{perl_archlib}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%check
make test || :

%files
%doc README MANIFEST 
%{perl_vendorlib}/XML/Driver/HTML.pm
%{_mandir}/man1/html2xhtml.*
%{_mandir}/man3/XML::Driver::HTML.*
%{_bindir}/html2xhtml


