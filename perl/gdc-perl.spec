%global __perllib_exclude_path %{__gdcperllib_path}
%global __perl_exclude_path    %{__gdcperl_path}

# inspired by a piece from global section of
# http://pkgs.fedoraproject.org/cgit/rpms/perl.git/tree/perl.spec
%global __requires_exclude gdc-perl\\((VMS::|Mac::)
%global __provides_exclude perl\\((VMS|Win32|BSD::|DB\\)$)

# taken from %%package Locale-Codes section of
# http://pkgs.fedoraproject.org/cgit/rpms/perl.git/tree/perl.spec
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^gdc-perl\\(Locale::Codes::Country_Retired\\)|^gdc-perl\\(Locale::Codes::LangFam_Retired\\)|^gdc-perl\\(Locale::Codes::Script_Retired\\)|^gdc-perl\\(Locale::Codes::LangExt_Codes\\)|^gdc-perl\\(Locale::Codes::LangFam_Codes\\)|^gdc-perl\\(Locale::Codes::Script_Codes\\)|^gdc-perl\\(Locale::Codes::Language_Codes\\)|^gdc-perl\\(Locale::Codes::LangExt_Retired\\)|^gdc-perl\\(Locale::Codes::Currency_Codes\\)|^gdc-perl\\(Locale::Codes::LangVar_Retired\\)|^gdc-perl\\(Locale::Codes::Language_Retired\\)|^gdc-perl\\(Locale::Codes::Country_Codes\\)|^gdc-perl\\(Locale::Codes::LangVar_Codes\\)|^gdc-perl\\(Locale::Codes::Currency_Retired\\)


# taken from %%package libs section of
# http://pkgs.fedoraproject.org/cgit/rpms/perl.git/tree/perl.spec
Provides:       gdc-perl(unicore::Name)

Name:		gdc-perl
Version:	5.26.0
Release:	1%{?dist}
Summary:	GoodData Perl 5
Group:		Development/Languages
License:	(GPL+ or Artistic)
URL:		http://www.perl.org/
Source0:	http://www.cpan.org/src/5.0/perl-%{version}.tar.gz

# to run Configure
BuildRequires:	bash

BuildRequires:	gdbm-devel

%description


%prep
%setup -q -n perl-%{version}



%build
/bin/sh Configure \
	-des \
	-Dprefix=/opt/gdc/perl

make %{?_smp_mflags}

%check
#make test

%install
make install DESTDIR=%{buildroot}


%files
/opt/gdc/perl


%changelog

