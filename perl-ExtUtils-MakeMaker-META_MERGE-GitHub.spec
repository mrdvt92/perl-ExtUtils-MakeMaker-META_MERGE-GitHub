Name:           perl-ExtUtils-MakeMaker-META_MERGE-GitHub
Version:        0.01
Release:        1%{?dist}
Summary:        Perl package to generate ExtUtils::MakeMaker META_MERGE for GitHub repositories
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-MakeMaker-META_MERGE-GitHub/
Source0:        http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-MakeMaker-META_MERGE-GitHub-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Generates the META_MERGE key and hash value for a normal GitHub repository.

%prep
%setup -q -n ExtUtils-MakeMaker-META_MERGE-GitHub-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu May 19 2022 Michael R. Davis <mrdvt@cpan.org> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
