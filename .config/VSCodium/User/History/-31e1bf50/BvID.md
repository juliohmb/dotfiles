# Install Arch directly
## Pre installation
### Download ISO
- [Official ISO](https://archlinux.org/download/)
### Verify signature
```
gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig
```
### Connect to the internet
- connect to network interface:
```
ip link
```
```
ip link set interface up
```
- connect to wifi:
```
iwctl
```
```
device list
```
```
station device scan
```
```
station device get-networks
```
```
station device connect SSID
```
```
ping google.com
```
### get the best mirrors:
```
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.default
```
```
reflector --country brazil --sort rate -l 15 --save /etc/pacman.d/mirrorlist
```
## Install arch (archinstall)
```
archinstall
```
## Add User to Wheel group
```
EDITOR=nano visudo
```
```
sudo usermod -aG wheel
```
## Run setup.sh
```
./setup.sh
```

# Install on WSL2
## Run setup.ps1
```
./setup.ps1
```
## Configure Acrh user
## Run setup.sh
```
./setup.sh
```