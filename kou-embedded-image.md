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
#### General -> Advanced:

```
Shared Clipboard: Bidirectional
Drag'n'Drop: Bidirectional

Description:
```

#### Display -> Screen

```
Video Memory: 64 MB or 128 MB
```

#### Audio

```
Disable Audio (just uncheck the box with **Enable Audio**)
```
