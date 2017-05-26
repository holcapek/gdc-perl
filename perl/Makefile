topdir       := $(patsubst %/, %, $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))/rpmbuild
builddir     := $(topdir)/BUILD
buildrootdir := $(topdir)/BUILDROOT
rpmdir       := $(topdir)/RPMS
sourcedir    := $(topdir)/SOURCES
specdir      := $(topdir)/SPECS
srcrpmdir    := $(topdir)/SRPMS

init:
	mkdir -v -p $(builddir) $(buildrootdir) $(rpmdir) $(sourcedir) $(specdir) $(srcrpmdir)

getsources:
	spectool -C $(sourcedir) -g gdc-perl.spec

srpm: init getsources
	rpmbuild \
		--define "_topdir $(topdir)" \
		-bs gdc-perl.spec

rpm:
	sudo mock \
		--rebuild \
		--resultdir . \
		~/rpmbuild/SRPMS/gdc-perl-*.src.rpm
	
