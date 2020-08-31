#!/usr/bin/python3

import os
import sys
from moviepy.editor import *
import face_recognition
from PIL import Image
import numpy as np

def transform_image(path):
    img = face_recognition.load_image_file(path)
    faces = face_recognition.face_locations(img, number_of_times_to_upsample=2)

    out_img = Image.fromarray(img)

    for face in faces:
        t,r,b,l = face

        h = int(2/3 * (b - t))
        m = mask.resize((r - l, h))

        out_img.paste(m, (l, b - h), m)

    out_img.save("out.png")


def transform_video(path):
    def mask_faces(get_frame, t):
        image = get_frame(t)


        x = int(t*4)
        if x not in mask_locations:
            faces = face_recognition.face_locations(image, number_of_times_to_upsample=2)
        elif len(mask_locations[x]) == 0:
            return image
        else:
            faces = mask_locations[x]

        out_img = Image.fromarray(image)
        if verbose and len(faces) > 0:
            print("%s faces recognized" % len(faces))
        for face in faces:
            t,r,b,l = face

            h = int(2/3 * (b - t))
            m = mask.resize((r - l, h))

            out_img.paste(m, (l, b - h), m)

        return np.array(out_img)
        

    mask_locations = dict()
    clip = VideoFileClip(path)
    clip = clip.fl(mask_faces)
    clip.write_videofile("out.mp4")




if len(sys.argv) < 2:
    print("you forgot to specify a file, can't do much without one")


verbose = False
mask = Image.open("mask.png")

path = sys.argv[1]
extension = os.path.splitext(path)[-1]  

if extension == ".png" or extension == ".jpg":
    transform_image(path)
else:
    transform_video(path)
