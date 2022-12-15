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