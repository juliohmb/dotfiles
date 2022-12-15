#!/bin/bash

# Get dotfiles
pacman -S stow
cd ../dotfiles/
stow . -t ~

cd ~
git clone https://github.com/juliohmb/dotfiles.git
cd dotfiles
stow . -t ~

# Install and Configure Git
sudo pacman -S git
git config --global user.name "Julio Henrique Moro Balarini"
git config --global user.email juliohmb@gmail.com

# Install Nerd Fonts
mkdir ~/.local/share/fonts
wget -c https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf -P ~/.local/share/fonts
wget -c https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf -P ~/.local/share/fonts
wget -c https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf -P ~/.local/share/fonts
wget -c https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf -P ~/.local/share/fonts
fc-cache -f -v