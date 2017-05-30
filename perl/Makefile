topdir       := $(patsubst %/, %, $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))/rpmbuild
builddir     := $(topdir)/BUILD
buildrootdir := $(topdir)/BUILDROOT
rpmdir       := $(topdir)/RPMS
sourcedir    := $(topdir)/SOURCES
specdir      := $(topdir)/SPECS
srcrpmdir    := $(topdir)/SRPMS

spec    := gdc-perl.spec
# traling `head` is there due to gdc-perl-debuginfo package being included
# in the output
version := $(shell rpm -q --specfile --qf '%{version}\n' $(spec) | head -n 1)
release := $(shell rpm -q --specfile --qf '%{release}\n' $(spec) | head -n 1)
arch    := $(shell rpm --eval '%{_arch}')

tarball := perl-$(version).tar.gz
srpm    := $(srcrpmdir)/gdc-perl-$(version)-$(release).src.rpm
rpm     := $(rpmdir)/$(arch)/gdc-perl-$(version)-$(release).$(arch).rpm

vars:
	@echo version=$(version)
	@echo release=$(release)
	@echo    srpm=$(srpm)
	@echo     rpm=$(rpm)

$(builddir) $(buildrootdir) $(rpmdir) $(sourcedir) $(specdir) $(srcrpmdir):
	mkdir -v -p $(builddir) $(buildrootdir) $(rpmdir) $(sourcedir) $(specdir) $(srcrpmdir)

$(sourcedir)/$(tarball): $(sourcedir)
	spectool -C $(sourcedir) -g gdc-perl.spec

$(srpm): $(sourcedir)/$(tarball) $(srcrpmdir)
	rpmbuild \
		--define "_topdir $(topdir)" \
		-bs gdc-perl.spec

srpm: $(srpm)

$(rpm): $(srpm) $(builddir) $(buildrootdir) $(rpmdir)
	sudo mock \
		--copyin perl.req perl.prov /usr/lib/rpm/
	sudo mock \
		--resultdir . \
		--rebuild \
		$(srpm)

rpm: $(rpm)

clean:
	rm -rf $(topdir) *.log *.rpm
