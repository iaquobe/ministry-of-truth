#!/usr/bin/python3

import sys
from moviepy import *
import face_recognition
from PIL import Image

if len(sys.argv) < 2:
    print("you forgot to specify a file, can't do much without one")


img = face_recognition.load_image_file(sys.argv[1])
faces = face_recognition.face_locations(img, number_of_times_to_upsample=2)

mask = Image.open("mask.png")

out_img = Image.fromarray(img)

for face in faces:
    t,r,b,l = face

    h = int(2/3 * (b - t))
    m = mask.resize((r - l, h))

    out_img.paste(m, (l, b - h), m)

out_img.save("out.png")

