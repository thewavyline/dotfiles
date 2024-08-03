#!/usr/bin/python3

import os

SCRIPTS_DIR = os.getenv("HOME") + "/.dotfiles/scripts"

file = open(SCRIPTS_DIR + "/../set-random-wall.pid")
os.system("kill " + file.read())
file.close()

os.system(SCRIPTS_DIR + "/set_random_wall.py &")
