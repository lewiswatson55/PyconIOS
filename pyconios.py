#Python program for generating ios icons

import sys
import os
from PIL import Image


#im = Image.open(inputimage)


def checkinput():
    if (len(sys.argv) >= 2):
        print('Attempting to open input image:', str(sys.argv[1]))
        inputimage = sys.argv[1]
        im = Image.open(inputimage)

    else:
        print("Please specify an input image i.e try:\n pyconios.py testicon.png")


#checkinput()