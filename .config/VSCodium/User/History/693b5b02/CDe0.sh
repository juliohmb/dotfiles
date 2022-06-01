#!/bin/bash
# Install Yay
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
cd ~/essentials/_Arch

yay -Sy
# Install Pacman pkgs
while IFS= read -r line
do
  sudo pacman -S --noconfirm --needed $line
done < "./pacman.txt"

# Install Yay pkgs
while IFS= read -r line
do
  yay -S --needed --noconfirm $line
done < "./yay.txt"