%define module 	XML-Driver-HTML
%define version 0.06
%define release %mkrel 8

Summary:	SAX Driver for non wellformed HTML
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL	
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 2:5.8.0
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArchitectures: noarch

%description
XML::Driver::HTML is a SAX Driver for HTML. There is no need
for the HTML input to be weel formed, as XML::Driver::HTML
is generating its SAX events by walking a HTML::TreeBuilder object.
The simplest kind of use, is a filter from HTML to XHTML
using XML::Handler::YAWriter as a SAX Handler.

%prep
%setup -q  -n %{module}-%{version}

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
