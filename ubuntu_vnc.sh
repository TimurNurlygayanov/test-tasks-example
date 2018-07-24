#!/usr/bin/env bash

#
# This scripts shares the idea how to easily
# setup and run VNC server on Ubuntu 16.04
#

sudo apt-get install vino

# to configure:
# vino-preferences

# --- without root!

gconftool-2 --set --type=bool /desktop/gnome/remote_access/enabled true

PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

gsettings set org.gnome.Vino require-encryption false
gsettings set org.gnome.Vino enabled true


export DISPLAY=:0
/usr/lib/vino/vino-server --sm-disable


# --- without root!
