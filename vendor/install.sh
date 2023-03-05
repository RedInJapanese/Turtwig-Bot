#!/bin/bash


# run this script if you don't have pip or the required dependancies installed.

DIR=/usr/bin/pip
if  [ -f "$DIR" ]
then 
	echo "Confirmed. Pip is installed."
else
	echo "Installing pip. If you are using a package manager other than sudo, please change the script."
	sudo apt install pip
fi

echo "Installing discord..."
pip install discord