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

### Remove old kernels and headers:

```
sudo apt-get autoremove --purge linux-image-generic-hwe-16.0 linux-headers-generic-lts-vivid linux-image-`uname -r` linux-headers-`uname -r`
sudo reboot
```

#### Remove programs

```
sudo apt remove --autoremove --purge abiword blueman xfce4-dict evince evince-common firefox gigolo gimp gmusicbrowser gnome-calculator gnumeric light-locker gnome-mines xfce4-notes onboard orage parole pidgin xfce4-power-manager system-config-printer-* xfce4-mailwatch-plugin xfce4-quicklauncher-plugin xfce4-screenshooter xfce4-weather-plugin xfce4-verve-plugin xfce4-cpugraph-plugin xfce4-netload-plugin simple-scan gnome-sudoku thunderbird transmission-* xchat xfburn  avahi-daemon avahi-autoipd bluez bluez-cups cups chromium-codecs-ffmpeg-extra cups-bsd cups-client cups-common cups-filters cups-filters-core-drivers catfish ristretto gucharmap xubuntu-community-wallpapers
```

#### Remove them carefully:

```
sudo apt-get autoremove --purge apt-xapian-index g++-4.8 xfce4-appfinder printer-driver-* gstreamer* accountsservice app-install-data-partner apport brltty espeak espeak-data gdisk genisoimage geoip-database lintian  dictionaries-common dmidecode dmz-cursor-theme firefox-locale-en firefox-locale-tr flashplugin-installer fonts-kacst fonts-kacst-one fonts-khmeros-core fonts-lao fonts-lklug-sinhala fonts-nanum fonts-sil-abyssinica fonts-sil-padauk fonts-takao-pgothic fonts-thai-tlwg fonts-tibetan-machine fonts-tlwg* foomatic-db-compressed-ppds gimp-help-common gimp-help-en gnome-accessibility-themes hdparm language-pack-gnome-tr language-pack-gnome-tr-base language-pack-tr language-pack-tr-base libabiword-3.0 libaccountsservice0 libavcodec54 libavformat54 libavutil52 libbluetooth3 libbrlapi0.6 libburn4 libcamel-1.2 libc6-dbg libflac8 libflite1 memtest86+ modemmanager nautilus-data network-manager-pptp network-manager-pptp-gnome os-prober pidgin-otr oxideqt-codecs-extra poppler-data poppler-utils popularity-contest sane-utils ttf-punjabi-fonts ttf-indic-fonts-core toshset ubuntu-restricted-addons vim-common wamerican whoopsie xbrlapi xserver-xorg-video-cirrus xserver-xorg-video-intel xserver-xorg-video-mach64 xserver-xorg-video-mga xserver-xorg-video-neomagic xserver-xorg-video-nouveau xserver-xorg-video-openchrome xserver-xorg-video-qxl xserver-xorg-video-r128 xserver-xorg-video-s3 xserver-xorg-video-savage xserver-xorg-video-siliconmotion xserver-xorg-video-sis xserver-xorg-video-sisusb xserver-xorg-video-tdfx xserver-xorg-video-trident xserver-xorg-video-vesa xserver-xorg-video-vmware xubuntu-docs xubuntu-community-wallpapers humanity-icon-theme language-pack-gnome-en-base language-pack-gnome-en
```

