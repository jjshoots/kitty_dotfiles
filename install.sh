#!/bin/bash

# try to install kitty if it doesn't already exist
if ! command -v kitty &> /dev/null
then
  echo "kitty not found, installing from apt..."
  sudo apt update
  sudo apt install kitty
fi

# set this as the default terminal
gsettings set org.gnome.desktop.default-applications.terminal exec 'kitty'
