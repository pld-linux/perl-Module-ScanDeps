#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	ScanDeps
Summary:	Recursively scan Perl programs for dependencies
Summary(pl):	Rekurencyjne wyszukiwanie zale¿no¶ci programów perlowych
Name:		perl-%{pdir}-%{pnam}
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	460e84cbdb138c37af7bd6afedaf54e1
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application of Module::ScanDeps is to generate executables from
scripts that contains necessary modules; this module supports two such
projects, PAR and App::Packer.  Please see their respective
documentations on CPAN for further information.

%description -l pl
Stosowanie Module::ScanDeps polega na generowaniu binariów ze skryptów
zawieraj±cych odpowiednie modu³y. Ten modu³ wspiera dwa takie
projekty: PAR i App::Packer. Wiêcej informacji mo¿na znale¼æ w ich
dokumentacji w CPAN.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README AUTHORS
%{perl_vendorlib}/Module/*.pm
%attr(755,root,root)%{_bindir}/scandeps.pl
%{_mandir}/man3/*
%{_mandir}/man1/*
