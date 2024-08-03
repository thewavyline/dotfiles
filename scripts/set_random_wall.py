#!/usr/bin/python3

import random
import os

WALLPAPER_DIR = os.getenv("HOME") + "/.dotfiles/wallpapers"
SCRIPTS_DIR = os.getenv("HOME") + "/.dotfiles/scripts"

file = open(SCRIPTS_DIR + "/../set-random-wall.pid", "w")
file.write(str(os.getpid()))
file.close()

os.system("swaybg -i " + WALLPAPER_DIR + "/" + random.choices(os.listdir(WALLPAPER_DIR))[0])
