# debian-based kou image

## /etc/apt/sources.list
```
#deb cdrom:[Debian GNU/Linux 9.3.0 _Stretch_ - Official amd64 NETINST 20171209-12:10]/ stretch main

deb http://ftp.de.debian.org/debian/ stretch main contrib non-free
deb-src http://ftp.de.debian.org/debian/ stretch main contrib non-free

deb http://security.debian.org/debian-security stretch/updates main contrib non-free
deb-src http://security.debian.org/debian-security stretch/updates main contrib non-free

# stretch-updates, previously known as 'volatile'
deb http://ftp.de.debian.org/debian/ stretch-updates main contrib non-free
deb-src http://ftp.de.debian.org/debian/ stretch-updates main contrib non-free

# stretch-backports
deb http://ftp.debian.org/debian stretch-backports main contrib non-free
```

## Install needed packages:
```
sudo apt install xfce4 xfce4-goodies
sudo apt install linux-headers-amd64 linux-headers-4.9.0-4-amd64 gcc make
sudo apt install default-jre
sudo apt install gcc-arm-none-eabi gdb-arm-none-eabi
sudo apt install openocd
```

After you can install VirtualBox Additions from CD

## /etc/lightdm/lightdm.conf
```
#greeter-hide-users-false
greeter-hide-users-false
...
#autologin-user=
autologin-user=<user>

```

## Shared folders
```
sudo adduser <user> vboxsf
sudo usermod -a -G vboxsf <user>

```

## GNU MCU Eclipse Plug-ins
```
name: GNU MCU Eclipse Plug-ins
URL: http://gnu-mcu-eclipse.netlify.com/v4-neon-updates/
```
