#!/bin/bash

# try to install kitty if it doesn't already exist
if ! command -v kitty &> /dev/null
then
  if [[ "$(uname)" == "Darwin" ]]; then
    echo "kitty not found, installing from homebrew..."
    brew install --cask kitty
  else
    echo "kitty not found, installing from apt..."
    sudo apt update
    sudo apt install kitty
  fi
fi

# set this as the default terminal
if command -v gsettings &> /dev/null
then
  gsettings set org.gnome.desktop.default-applications.terminal exec 'kitty'
fi
