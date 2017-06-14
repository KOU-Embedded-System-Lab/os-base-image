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
```
