%global __perllib_exclude_path %{__gdcperllib_path}

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

