#!/usr/bin/python3

import sys
from moviepy import *

if len(sys.argv) < 2:
    print("you forgot to specify a file, can't do much without one")

clip = VideoFileClip(sys.argv[1])

