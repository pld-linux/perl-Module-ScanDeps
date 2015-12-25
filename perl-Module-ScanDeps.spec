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
Version:	1.10
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f01f36a25bf372712ff6b1e4aad8d89c
URL:		http://search.cpan.org/dist/Module-ScanDeps/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Temp
BuildRequires:	perl-Module-Build
BuildRequires:	perl-PathTools
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-version
%endif
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
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/scandeps.pl
%{perl_vendorlib}/Module/ScanDeps.pm
%{perl_vendorlib}/Module/ScanDeps
%{_mandir}/man1/scandeps.pl.1p*
%{_mandir}/man3/Module::ScanDeps.3pm*
