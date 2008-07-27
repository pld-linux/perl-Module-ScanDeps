#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	ScanDeps
Summary:	Module::ScanDeps - recursively scan Perl programs for dependencies
Summary(pl.UTF-8):	Module::ScanDeps - rekurencyjne wyszukiwanie zależności programów perlowych
Name:		perl-Module-ScanDeps
Version:	0.56
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0385a6d740afa453f8910920362df562
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application of Module::ScanDeps is to generate executables from
scripts that contains necessary modules; this module supports two such
projects, PAR and App::Packer.  Please see their respective
documentations on CPAN for further information.

%description -l pl.UTF-8
Zastosowanie Module::ScanDeps to generowanie ze skryptów plików
wykonywalnych zawierających wszelkie potrzebne skryptowi moduły.  Ten
moduł wspiera dwa takie projekty: PAR i App::Packer. Więcej informacji
można znaleźć w ich dokumentacji w CPAN.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README AUTHORS
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%attr(755,root,root)%{_bindir}/scandeps.pl
%{_mandir}/man3/*
%{_mandir}/man1/*
