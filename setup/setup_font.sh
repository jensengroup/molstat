#!/usr/bin/env bash

echo "Install Fira Sans to ~/.fonts"

wget -O fira.zip https://github.com/mozilla/Fira/archive/master.zip
unzip fira.zip 

# Copy-paste ttf to .fonts so latex can find them

cp Fira-master/ttf/*.ttf ~/.fonts
rm -r Fira-master
rm -r fira.zip

