# KOU Embedded VirtualBox image creation

* [Download **xubuntu 16.04.2 32-bit**](http://torrent.ubuntu.com/xubuntu/releases/xenial/release/desktop/xubuntu-16.04.2-desktop-i386.iso.torrent)
* [Download and install **VirtualBox 5.1.22**](https://www.virtualbox.org/wiki/Downloads)
* [Download and install **VirtualBox 5.1.22 Oracle VM VirtualBox Extension Pack**](https://www.virtualbox.org/wiki/Downloads)

## Create Virtual Machine

```
Name: kou-embedded-image
Type: Linux
Version: Ubuntu (32-bit)

Memory size: 1536 MB (1.5 GB)

Hard disk: Create a virtual hard disk now

Hard disk file type: VDI (VirtualBox Disk image)
Storage on physical hard disk: Dynamically allocated
File location and size: 10.00 GB
```

### Settings
#### General >> Advanced:

```
Shared Clipboard: Bidirectional
Drag'n'Drop: Bidirectional

Description:

```

### System >> Motherboard:

```
Disable Floppy (just uncheck the box with **Floppy**)
```

#### Display >> Screen:

```
Video Memory: 64 MB or 128 MB
```

#### Audio

```
Disable Audio (just uncheck the box with **Enable Audio**)
```

## Install Xubuntu

### "Hoş Geldiniz":

```
Language: Türkçe
Press -> "Xubuntu'yu Kur"
```

### "Xubuntu kurulumu için hazırlanılıyor"

```
Check the box with: "Download updates while installing Xubuntu. This saves time after installation."
```

### "Kurulum türü":

```
Check the box with: "Diski sil ve Xubuntu yükle"

Press -> "Şimdi Yükle"

On message "Değişiklikler diske kaydedilsin mi?":
Press -> "Devam Et"
```

### "Neredesiniz?":

```
Just write in a box below a map:
Istanbul
```

### "Klavye düzeni":

```
"Klavye düzeninizi seçin: Türkçe Q Klavye -> Türkçe Q Klavye"
Press -> "Devam Et"
```

### "Kimsiniz?":

```
"Adınız: kou"
"Bilgisayarınızın adı: kou-embedded"
"Bir kullanıcı adı seçin: kou"
"Bir parola seçin: ' ' (boşluk)"
"Parolanızı doğrulayın: ' ' (boşluk)"

Check the box with: "Otomatik giriş yap"

Press -> "Devam Et"
```

### "Kurulum Tamamlandı":

```
Press -> "Şimdi Yeniden Başlat"

Please remove the installation medium, then press ENTER:
Press -> "Enter"
```

## Configuration:

Download this file to virtual machine to copy/paste instruction steps:

```
wget https://raw.githubusercontent.com/KOU-Embedded-System-Lab/os-base-image/master/kou-embedded-image.md
```

#### Yazılım ve Güncelleştirmeler:

```
Ubuntu Yazılımı ->
  İndirme adresi: Almanya sunucusu (de.archive.ubuntu.com or de2.archive.ubuntu.com)

Diğer Yazılımlar ->
  Tick - "Canonical Ortakları"
  Tick - "Canonical Ortakları (Kaynak Kodu)"

Güncelleştirmeler ->
  Güncellemeleri otomatik olarak kontrol et: Hiçbir zaman
  Güvenlik güncellemeleri olduğunda: O an göster
  Diğer güncellemeler olduğunda: Her iki haftada bir göster
  
  Beni, yeni bir Ubuntu sürümü olunca bilgilendir: Hiçbir zaman
  
Press -> "Kapat" -> "Yenile"
```

### Update & Upgrade 

```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade

reboot

sudo apt autoremove
sudo apt autoclean
sudo apt clean

reboot

sudo apt update

poweroff
```

**Please take a snapshot or clone your virtual machine before continue. Instruction steps below may damage your image.**

### Remove old kernels and headers:

```
sudo apt-get autoremove --purge linux-image-4.8.0-XX-generic linux-headers-4.8.0-XX linux-headers-4.8.0-XX-generic linux-image-extra-4.8.0-XX-generic 
sudo reboot
```

```
linux-image-`uname -r` linux-headers-`uname -r` linux-image-extra-`uname -r`
```

#### Remove programs

```
sudo apt remove --autoremove --purge abiword blueman xfce4-dict evince evince-common firefox gigolo gimp gmusicbrowser gnome-calculator gnumeric light-locker gnome-mines xfce4-notes onboard orage parole pidgin xfce4-power-manager system-config-printer-* xfce4-mailwatch-plugin xfce4-quicklauncher-plugin xfce4-screenshooter xfce4-weather-plugin xfce4-verve-plugin xfce4-cpugraph-plugin xfce4-netload-plugin simple-scan gnome-sudoku thunderbird transmission-* xchat xfburn  avahi-daemon avahi-autoipd bluez bluez-cups cups chromium-codecs-ffmpeg-extra cups-bsd cups-client cups-common cups-filters cups-filters-core-drivers catfish ristretto gucharmap xubuntu-community-wallpapers dmidecode 
```

```
sudo apt remove --autoremove --purge alsa-base alsa-utils apparmor apport apport-gtk apport-symptoms aspell aspell-en avahi-autoipd avahi-daemon avahi-utils blueman bluez bluez-cups bluez-obexd brltty brltty-x11 catfish cheese-common colord colord-data cups cups-browsed cups-bsd cups-client cups-common cups-core-drivers cups-daemon cups-filters cups-filters-core-drivers cups-ppdc cups-server-common dc dictionaries-common dirmngr dmidecode efibootmgr enchant espeak espeak-data ethtool evince evince-common evolution-data-server-common firefox firefox-locale-en firefox-locale-tr fonts-guru fonts-guru-extra fonts-kacst fonts-kacst-one fonts-khmeros-core fonts-lao fonts-lklug-sinhala fonts-lohit-guru fonts-nanum fonts-sil-abyssinica fonts-sil-padauk fonts-takao-pgothic fonts-thai-tlwg fonts-tibetan-machine fonts-tlwg-garuda fonts-tlwg-garuda-ttf fonts-tlwg-kinnari fonts-tlwg-kinnari-ttf fonts-tlwg-laksaman fonts-tlwg-laksaman-ttf fonts-tlwg-loma fonts-tlwg-loma-ttf fonts-tlwg-mono fonts-tlwg-mono-ttf fonts-tlwg-norasi fonts-tlwg-norasi-ttf fonts-tlwg-purisa fonts-tlwg-purisa-ttf fonts-tlwg-sawasdee fonts-tlwg-sawasdee-ttf fonts-tlwg-typewriter fonts-tlwg-typewriter-ttf fonts-tlwg-typist fonts-tlwg-typist-ttf fonts-tlwg-typo fonts-tlwg-typo-ttf fonts-tlwg-umpush fonts-tlwg-umpush-ttf fonts-tlwg-waree fonts-tlwg-waree-ttf foomatic-db-compressed-ppds friendly-recovery fuse fwupd fwupdate fwupdate-signed gawk gcr gdb gdbserver gdisk geoip-database ghostscript ghostscript-x gigolo gnome-accessibility-themes gnome-calculator gnome-desktop3-data gnome-keyring gnome-menus gnome-mines gnome-software gnome-software-common gnome-sudoku gnome-system-tools gnome-user-guide gnupg-agent gnupg2 gsfonts gstreamer1.0-libav:i386 gstreamer1.0-nice:i386 gstreamer1.0-plugins-base:i386 gstreamer1.0-plugins-good:i386 gstreamer1.0-pulseaudio:i386 gstreamer1.0-x:i386 gucharmap gvfs:i386 gvfs-backends gvfs-bin gvfs-common gvfs-daemons gvfs-fuse gvfs-libs:i386 hardening-includes hddtemp hdparm hplip hplip-data hunspell-en-us hwdata hyphen-en-us i965-va-driver:i386 imagemagick imagemagick-6.q16 imagemagick-common indicator-application indicator-messages indicator-sound inxi krb5-locales laptop-detect libaa1:i386 libaacs0:i386 libabw-0.1-1v5:i386 libao-common libao4:i386 libapt-pkg-perl libarchive-zip-perl libart-2.0-2:i386 libavc1394-0:i386 libavcodec-ffmpeg56:i386 libavfilter-ffmpeg5:i386 libavformat-ffmpeg56:i386 libavresample-ffmpeg2:i386 libavutil-ffmpeg54:i386 libbabeltrace-ctf1:i386 libbabeltrace1:i386 libbdplus0:i386 libbluetooth3:i386 libbluray1:i386 libboost-date-time1.58.0:i386 libboost-filesystem1.58.0:i386 libboost-iostreams1.58.0:i386 libboost-system1.58.0:i386 libbrlapi0.6:i386 libbs2b0:i386 libburn4:i386 libcaca0:i386 libcamel-1.2-54:i386 libcanberra-gtk3-0:i386 libcanberra-gtk3-module:i386 libcanberra0:i386 libcdio-cdda1:i386 libcdio-paranoia1:i386 libcdio13:i386 libcdparanoia0:i386 libcgi-fast-perl libcgi-pm-perl libcgmanager0:i386 libcheese8:i386 libcilkrts5:i386 libclass-accessor-perl libclone-perl libclucene-contribs1v5:i386 libclucene-core1v5:i386 libclutter-1.0-0:i386 libclutter-1.0-common libclutter-gst-3.0-0:i386 libclutter-gtk-1.0-0:i386 libcmis-0.5-5v5:i386 libcogl-common libcogl-pango20:i386 libcogl-path20:i386 libcogl20:i386 libcolamd2.9.1:i386 libflac8:i386 libflite1:i386 libreoffice-base-core libreoffice-calc libreoffice-common libreoffice-core libreoffice-gtk libreoffice-help-en-us libreoffice-help-tr libreoffice-l10n-tr libreoffice-math libreoffice-style-elementary libreoffice-style-galaxy libreoffice-writer libsane:i386 libsane-common libsane-hpaio:i386 libsasl2-2:i386 libsasl2-modules:i386 libsasl2-modules-db:i386 libschroedinger-1.0-0:i386 libsmbclient:i386 libsnapd-glib1:i386 libsnappy1v5:i386 libsnmp-base libsnmp30:i386 libspectre1:i386 libspeechd2:i386 libspeex1:i386 libspeexdsp1:i386 libsqlite3-0:i386 libstdc++6:i386 libtag1v5:i386 libtag1v5-vanilla:i386 libtagc0:i386 libtcl8.6:i386 libthai-data libthai0:i386 libtheora0:i386 libtk8.6:i386 libunity-protocol-private0:i386 libunity-scopes-json-def-desktop libunity9:i386 libv4l-0:i386 libv4lconvert0:i386 libva1:i386 libvdpau1:i386 libvisual-0.4-0:i386 libvorbis0a:i386 libvorbisenc2:i386 libvorbisfile3:i386 libwacom-bin libwacom-common libwacom2:i386 libwavpack1:i386 
```

#### Remove them carefully:

```
sudo apt-get autoremove --purge apt-xapian-index g++-4.8 xfce4-appfinder printer-driver-* gstreamer* accountsservice app-install-data-partner apport brltty espeak espeak-data gdisk genisoimage geoip-database lintian  dictionaries-common dmidecode dmz-cursor-theme firefox-locale-en firefox-locale-tr flashplugin-installer fonts-kacst fonts-kacst-one fonts-khmeros-core fonts-lao fonts-lklug-sinhala fonts-nanum fonts-sil-abyssinica fonts-sil-padauk fonts-takao-pgothic fonts-thai-tlwg fonts-tibetan-machine fonts-tlwg* foomatic-db-compressed-ppds gimp-help-common gimp-help-en gnome-accessibility-themes hdparm language-pack-gnome-tr language-pack-gnome-tr-base language-pack-tr language-pack-tr-base libabiword-3.0 libaccountsservice0 libavcodec54 libavformat54 libavutil52 libbluetooth3 libbrlapi0.6 libburn4 libcamel-1.2 libc6-dbg libflac8 libflite1 memtest86+ modemmanager nautilus-data network-manager-pptp network-manager-pptp-gnome os-prober pidgin-otr oxideqt-codecs-extra poppler-data poppler-utils popularity-contest sane-utils ttf-punjabi-fonts ttf-indic-fonts-core toshset ubuntu-restricted-addons vim-common wamerican whoopsie xbrlapi xserver-xorg-video-cirrus xserver-xorg-video-intel xserver-xorg-video-mach64 xserver-xorg-video-mga xserver-xorg-video-neomagic xserver-xorg-video-nouveau xserver-xorg-video-openchrome xserver-xorg-video-qxl xserver-xorg-video-r128 xserver-xorg-video-s3 xserver-xorg-video-savage xserver-xorg-video-siliconmotion xserver-xorg-video-sis xserver-xorg-video-sisusb xserver-xorg-video-tdfx xserver-xorg-video-trident xserver-xorg-video-vesa xserver-xorg-video-vmware xubuntu-docs xubuntu-community-wallpapers humanity-icon-theme language-pack-gnome-en-base language-pack-gnome-en
```

