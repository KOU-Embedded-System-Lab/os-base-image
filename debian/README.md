# KOU Embedded VirtualBox image creation
Ata Niyazov 2018-01-18

* [Download **Debian 9**](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-9.3.0-amd64-netinst.iso)
* [Download and install **VirtualBox 5.2.6**](https://www.virtualbox.org/wiki/Downloads)
* [Download and install **VirtualBox 5.2.6 Oracle VM VirtualBox Extension Pack**](https://www.virtualbox.org/wiki/Downloads)

## Create Virtual Machine

```
Name: debian-kou-embedded-v$(date -I)
Type: Linux
Version: Debian (64-bit)

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

#### System >> Motherboard:

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

#### Shared Folders

```
Add Share

Folder Path:
Folder Name:
[ ] Read-only
[v] Auto-mount

```

## Install Debian 9

### Debian GNU/Linux installer boot menu

```
Graphical install
```

### Select a language

```
Language: English
Press -> "Continue"
```

### Select your location

```
Country, territory or area: other
Continent or region: Asia
Country, territory or area: Turkey
Press -> "Continue"
```

### Configure locales

```
Country to base default locale settings on: United States - en_US.UTF-8
Press -> "Continue"
```

### Configure the keyboard

```
Keymap to use: Turkish (Q layout)
Press -> "Continue"
```

### Configure the network

```
Hostname: kou-embedded
Press -> "Continue"

Domain name: (leave blank)
Press -> "Continue"
```

### Set up users and passwords

```
Root password: (leave blank)
Re-enter password to verify: (leave blank)
Press -> "Continue"

Full name for the new user: Student
Press -> "Continue"

Username for your account: student
Press -> "Continue"

Choose a password for the new user: ' ' (space)
Re-enter password to verify: ' ' (space)
Press -> "Continue"
```

### Partition disks

```
Partitioning method: Manual
Press -> "Continue"

Create new empty partition table on this device?
( ) No
(x) Yes
Press -> "Continue"

How to use this free space: Create a new partition
Press -> "Continue"

New partition size: 10.7 GB
Press -> "Continue"

Type for the new partition: Primary
Press -> "Continue"

Mount options: noatime,nodiratime
Press -> "Continue"

Done setting up the partition
Press -> "Continue"

Finish partitioning and write changes to disk
Press -> "Continue"

Do you want to return to the partitioning menu?
(x) No
( ) Yes
Press -> "Continue"

Write the changes to disks?
( ) No
(x) Yes
Press -> "Continue"
```

### Configure the package manager

```
Scan another CD or DVD?
(x) No
( ) Yes
Press -> "Continue"

Debian archive mirror country: Germany
Press -> "Continue"

Debian archive mirror:
ftp.de.debian.org
ftp2.de.debian.org
Press -> "Continue"

HTTP proxy information (blank for none): (leave blank)
Press -> "Continue"
```

### Configuring popularity-contest

```
Participate in the package usage survey?
(x) No
( ) Yes
Press -> "Continue"
```

### Software selection

```
[ ] Debian desktop environment
...
[ ] print server
...
[v] standard system utilities

Press -> "Continue"
```

### Configuring popularity-contest

```
Participate in the package usage survey?
(x) No
( ) Yes
Press -> "Continue"
```

### Install the GRUB boot loader on a hard disk

```
Install the GRUB boot loader to the master boot record?
( ) No
(x) Yes
Press -> "Continue"

Device for boot loader installation: /dev/sda
Press -> "Continue"
```

### Finish the installation

```
Installation complete
Press -> "Continue"
```

# /etc/apt/sources.list
# If you also want the contrib and non-free components, add contrib non-free
# after main.

```
deb http://ftp.de.debian.org/debian/ stretch main contrib non-free
deb-src http://ftp.de.debian.org/debian/ stretch main contrib non-free

deb http://security.debian.org/debian-security stretch/updates main contrib non-free
deb-src http://security.debian.org/debian-security stretch/updates main contrib non-free

# stretch-updates, previously known as 'volatile'
deb http://ftp.de.debian.org/debian/ stretch-updates main contrib non-free
deb-src http://ftp.de.debian.org/debian/ stretch-updates main contrib non-free

# stretch-backports
deb http://ftp.debian.org/debian/ stretch-backports main contrib non-free
```

## ReduceDebian
Reducing the size of the Debian Installation Footprint

It may be useful to reduce the size of the installation footprint on Embedded systems, or on older computers or laptops with limited drive space, or in cases where a small installation is preferred. 
### To disable apt recommends & suggests:

You can configure apt via apt.conf files.
Here is a command I use on my server (as root):

```
cat > /etc/apt/apt.conf.d/01norecommend << EOF
APT::Install-Recommends "0" ;
APT::Install-Suggests "0" ;
EOF

```

### To see if apt reads this, enter this in command line (as root or regular user):

```
sudo apt-config dump | grep Recommends
```

### 2nd way (as root):
### Reconfigure apt so that it does not install additional packages

```
nano /etc/apt/apt.conf.d/10norecommends

APT::Install-Recommends "0";
APT::Install-Suggests "0";
```

## Update, upgrade & dist-upgrade
```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade

systemctl reboot

sudo apt autoremove
sudo apt autoclean
sudo apt clean
sudo apt update
```

## Install needed packages:
```
sudo apt install xfce4 xfce4-goodies bash-completion
sudo apt install linux-headers-amd64 linux-headers-`uname -r` firmware-linux
sudo apt install gcc make gcc-arm-none-eabi gdb-arm-none-eabi
#sudo apt install libc6:i386 libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386
#sudo apt-get install lib32ncurses5 lib32ncurses5-dev
sudo apt install openocd xterm gksu gtkterm aria2
sudo apt install default-jre
```

## VirtualBox Guest Additions Installation
Insert Guest Additional CD image...
```
#sudo apt-get install build-essential module-assistant dkms
#sudo apt install virtualbox-guest-dkms virtualbox-guest-x11
cd /media/cdrom0
sudo sh autorun.sh
```


## /etc/lightdm/lightdm.conf
lightdm greeter autologin & users activation
```
...
#greeter-hide-users-false
greeter-hide-users-false
...
#allow-guest=true
allow-guest=false
...
#autologin-user=
autologin-user=<USERNAME>
...
```

## Shared folders
```
sudo adduser <USERNAME> vboxsf
sudo usermod -a -G vboxsf <USERNAME>
```

## GNU MCU Eclipse Plug-ins
```
name: GNU MCU Eclipse Plug-ins
URL: http://gnu-mcu-eclipse.netlify.com/v4-neon-updates/
```

## Look & Feel
```
sudo apt install git

sudo apt install gtk2-engines-murrine 

mkdir ~/.themes
cd ~/.themes/
git clone https://github.com/LinxGem33/OSX-Arc-White.git

mkdir ~/.icons
cd ~/.icons/
git clone https://github.com/keeferrourke/la-capitaine-icon-theme.git
git clone https://github.com/keeferrourke/capitaine-cursors.git
mv ~/.icons/capitaine-cursors/dist/cursors/ ~/.icons/la-capitaine-icon-theme/
rm -rf ~/.icons/capitaine-cursors/
gtk-update-icon-cache ~/.icons/la-capitaine-icon-theme/

cd /usr/share/themes/
sudo ln -s ~/.themes/OSX-Arc-White/ .

cd /usr/share/icons/
sudo ln -s ~/.icons/la-capitaine-icon-theme/ .

sudo apt install lightdm-gtk-greeter-settings
```

## TO-DO:
1. change theme
2. change icon theme
3. change cursor theme
4. change window manager style
5. change greeter theme & icons
6. change background
7. add whisker menu as main menu
8. change settings for power manager
9. change settings for session and startup
