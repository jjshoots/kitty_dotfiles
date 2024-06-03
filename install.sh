#!/bin/bash

# install kitty
sudo apt install kitty

# set this as the default terminal
gsettings set org.gnome.desktop.default-applications.terminal exec 'kitty'
