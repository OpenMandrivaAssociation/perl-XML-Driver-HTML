%define upstream_name 	 XML-Driver-HTML
%define upstream_version 0.06

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	SAX Driver for non wellformed HTML
License: 	GPL	
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML::Driver::HTML is a SAX Driver for HTML. There is no need
for the HTML input to be weel formed, as XML::Driver::HTML
is generating its SAX events by walking a HTML::TreeBuilder object.
The simplest kind of use, is a filter from HTML to XHTML
using XML::Handler::YAWriter as a SAX Handler.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{perl_archlib}
%makeinstall_std
%{__rm} -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean 
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST 
%{perl_vendorlib}/XML/Driver/HTML.pm
%_mandir/man1/html2xhtml.*
%_mandir/man3/XML::Driver::HTML.*
%_bindir/html2xhtml
