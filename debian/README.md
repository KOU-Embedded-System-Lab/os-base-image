# KOU Embedded VirtualBox image creation
Ata Niyazov 2018-04-11

* [Download **Debian 9**](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-9.4.0-amd64-netinst.iso)
* [Download and install **VirtualBox 5.2.8**](https://www.virtualbox.org/wiki/Downloads)
* [Download and install **VirtualBox 5.2.8 Oracle VM VirtualBox Extension Pack**](https://www.virtualbox.org/wiki/Downloads)

## Create Virtual Machine

```
Name: debian-kou-embedded-v$(date -I)
Type: Linux
Version: Debian (64-bit)

Memory size: 1536 MB (1.5 GB)

Hard disk: Create a virtual hard disk now

Hard disk file type: VDI (VirtualBox Disk image)
Storage on physical hard disk: Dynamically allocated
File location and size: 8.00 GB
```

### Settings

#### General >> Advanced:

```
Shared Clipboard: Bidirectional
Drag'n'Drop: Bidirectional

Description:
debian-kou-embedded-v$(date -I)

Username: student
Password: ' ' (space)
Hostname: kou-embedded

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
Disable Audio Output (just uncheck the box with **Enable Audio Output**)
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

Full name for the new user: student
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

New partition size: 8.6 GB
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

## Login: Debian GNU/Linux 9 kou-embedded tty1

```
kou-embedded login: student
Password: ' ' (space)

student@kou-embedded:~$ _
```

## /etc/apt/sources.list

If you also want the contrib and non-free components, add contrib non-free
after main.

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

Note: This section is optional. *DO NOT* apply this configurations if you do not know what you are doing.

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
nano /etc/apt/apt.conf.d/01norecommends

APT::Install-Recommends "0";
APT::Install-Suggests "0";
```

## Update, upgrade & dist-upgrade

```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade

sudo reboot

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
sudo apt install openocd gksu gtkterm
sudo apt install default-jre
```

## Fonts

```
sudo apt-get install ttf-mscorefonts-installer ttf-xfree86-nonfree ttf-dejavu xfonts-terminus xfonts-terminus-oblique
```

## VirtualBox Guest Additions Installation

Insert Guest Additional CD image...

```
#sudo apt-get install build-essential module-assistant dkms
#sudo apt install virtualbox-guest-dkms virtualbox-guest-x11
cd /media/cdrom0
sudo sh autorun.sh
```

## Configurations

### /etc/default/grub

disable grub boot timeout

```
...
#GRUB_TIMEOUT=5
GRUB_TIMEOUT=0
...

sudo update-grub
```

### /etc/lightdm/lightdm.conf

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
sudo adduser $USER vboxsf
sudo usermod -a -G vboxsf $USER
```

## GNU MCU Eclipse

```
mkdir ~/Resources/
cd ~/Resources/
mkdir ~/Resources/library
mkdir ~/Resources/template
```

### GNU MCU Eclipse IDE for C/C++ Developers

Link: https://gnu-mcu-eclipse.github.io/downloads/

```
GNU MCU Eclipse IDE for C/C++ Developers Oxygen.2 20180125

wget https://github.com/gnu-mcu-eclipse/org.eclipse.epp.packages/releases/download/v4.3.2-20180125-o2/20180125-1917-gnumcueclipse-4.3.2-oxygen-2-linux.gtk.x86_64.tar.gz

tar -xvzf *.tar.gz
```

### Manual install links:
```
name: GNU MCU Eclipse Plug-ins
URL: http://gnu-mcu-eclipse.netlify.com/v4-neon-updates/
```

### Create Launcher

```
Name: KOU-Eclipse
Comment: System programming course IDE
Command: /home/student/Resources/eclipse/eclipse
...
Icon: icon.xpm
...
Description: System programming course IDE
...
[v] Allow this file to run as a program
```

### Library

```
```

### Add user to dialout group

```
sudo adduser $USER dialout
sudo usermod -a -G dialout $USER
```

## Look & Feel

```
sudo apt install git

sudo apt install gtk2-engines-murrine arc-theme

mkdir ~/.themes
cd ~/.themes/

#git clone https://github.com/LinxGem33/OSX-Arc-White.git

wget https://codeload.github.com/LinxGem33/OSX-Arc-White/zip/master
unzip master
rm master
mv ~/.themes/OSX-Arc-White-master/ ~/.themes/OSX-Arc-White/

mkdir ~/.icons
cd ~/.icons/

#git clone https://github.com/keeferrourke/la-capitaine-icon-theme.git

wget https://codeload.github.com/keeferrourke/la-capitaine-icon-theme/zip/master
unzip master
rm master
mv ~/.icons/la-capitaine-icon-theme-master/ ~/.icons/La\ Capitaine/

#git clone https://github.com/keeferrourke/capitaine-cursors.git

wget https://codeload.github.com/keeferrourke/capitaine-cursors/zip/master
unzip master
rm master
mv ~/.icons/capitaine-cursors-master/dist/cursors/ ~/.icons/La\ Capitaine/
rm -rf ~/.icons/capitaine-cursors-master/
gtk-update-icon-cache ~/.icons/La\ Capitaine/

cd /usr/share/themes/
sudo ln -s ~/.themes/OSX-Arc-White/ .

cd /usr/share/icons/
sudo ln -s ~/.icons/La\ Capitaine/ .

sudo apt install lightdm-gtk-greeter-settings
```

## Remove list

```
sudo apt remove --auto-remove --purge
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
10. disable grub timeout

