# Makefile to build the RPM for collectl addon
NAME=collectl-lustre
VERSION=1.0.0
SPECFILE=$(NAME).spec
RPMTOPDIR=$$PWD/RPMBUILD
TARBALL=$(NAME)-$(VERSION).tar.gz

$(RPMTOPDIR):
	mkdir -p $(RPMTOPDIR)/{BUILD,RPMS,SRPMS,SPECS}

tar: 
	mkdir -p $(NAME)-$(VERSION)
	cp -rv ../*.pm $(NAME)-$(VERSION)
	cp -rv ../*.ph $(NAME)-$(VERSION)
	tar -zcvf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)

rpm: tar $(RPMTOPDIR)
	cp $(NAME)-$(VERSION).tar.gz $(RPMTOPDIR)/BUILD/
	rpmbuild --define "_topdir $(RPMTOPDIR)" --define "_sourcedir $$PWD" -ba $(SPECFILE) 
	mkdir -p ./RPMs
	cp -rv $(RPMTOPDIR)/RPMS/*/*.rpm ./RPMs
	mkdir -p ./SRPMs
	cp -rv $(RPMTOPDIR)/SRPMS/*.src.rpm ./SRPMs

.PHONY: rpm clean all

clean:
	rm -rf $(RPMTOPDIR) $(NAME)-$(VERSION)
	rm -rf $(TARBALL)
	rm -rf ./SRPMs ./RPMs
