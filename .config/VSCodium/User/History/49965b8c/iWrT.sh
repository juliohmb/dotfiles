#!/bin/bash

# Get dotfiles
pacman -S stow
cd ../dotfiles/
stow . -t ~

cd ~
git clone https://github.com/juliohmb/dotfiles.git
cd dotfiles
stow . -t ~
