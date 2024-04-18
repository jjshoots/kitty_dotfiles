#!/bin/bash

# install kitty
sudo apt install kitty

# set this as the default terminal
gsettings set org.gnome.desktop.default-applications.terminal exec 'kitty'

# make nerd fonts
mkdir -p ~/System
cd ~/System
git clone https://github.com/ryanoasis/nerd-fonts.git --depth 1
cd nerd-fonts
./install.sh Mononoki
