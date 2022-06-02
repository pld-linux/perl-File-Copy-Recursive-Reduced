#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	File
%define		pnam	Copy-Recursive-Reduced
Summary:	File::Copy::Recursive::Reduced - recursive copying of files and directories within Perl 5 toolchain
Summary(pl.UTF-8):	File::Copy::Recursive::Reduced - rekurencyjne kopiowanie plików i katalogów z poziomu narzędzi Perla 5
Name:		perl-File-Copy-Recursive-Reduced
Version:	0.006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a42c7743e4a76f7492d4877ad48d261f
URL:		https://metacpan.org/release/File-Copy-Recursive-Reduced
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Test-Simple >= 0.44
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended as a not-quite-drop-in replacement for
certain functionality provided by CPAN distribution
File-Copy-Recursive. The library provides methods similar enough to
that distribution's fcopy(), dircopy() and rcopy() functions to be
usable in those CPAN distributions often described as being part of
the Perl toolchain.

%description -l pl.UTF-8
Ta biblioteka ma być przybliżonym zamiennikiem dla wybranej części
funkcjonalności dostarczanej przez dystrybucję CPAN
File-Copy-Recursive. Biblioteka dostarcza metody wystarczająco podobne
do funkcji fcopy(), dircopy() i rcopy(), aby dało się ich używać w
dystrubucjach CPAN opisywanych jako część zestawu narzędzi Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%dir %{perl_vendorlib}/File/Copy/Recursive
%{perl_vendorlib}/File/Copy/Recursive/Reduced.pm
%{_mandir}/man3/File::Copy::Recursive::Reduced.3pm*
