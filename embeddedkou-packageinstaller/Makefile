DESTDIR=/
INSTALL_LOCATION=$(DESTDIR)/usr/

#CFLAGS:=$(shell dpkg-buildflags --get CFLAGS)
#LDFLAGS:=$(shell dpkg-buildflags --get LDFLAGS)

all:
	sleep 0

install: EmbeddedKOU-packageinstaller

EmbeddedKOU-packageinstaller:
	mkdir -p $(INSTALL_LOCATION)/bin
	cp main.py $(INSTALL_LOCATION)/bin/EmbeddedKOU-packageinstaller
	chmod 755 $(INSTALL_LOCATION)/bin/EmbeddedKOU-packageinstaller

clean:
	sleep 0

distclean: clean
