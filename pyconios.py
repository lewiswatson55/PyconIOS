#Python program for generating ios icons

import sys
import os
from PIL import Image

im = None

def getinput():
    global im
    try:
        inputimage = sys.argv[1]
        im = Image.open(inputimage)
    except:
        print("\nFailed to open photo...\nPlease specify an input image i.e try:\n    pyconios.py testicon.png")
        exit()

def resizeimage(size):
    #resize image
    out = im.resize((size,size))
    out.save('./output/icon_{0}.png'.format(size))


def generateicons(requiredsizes):

    print("Generating images...")
    for i in range(len(requiredsizes)):
        resizeimage(requiredsizes[i])
    print("Finished.")


def main():

    #Required sizes list
    requiredsizes = [40, 60, 58, 87, 80, 120, 180, 20, 29, 58, 76, 152, 167, 1024]

    #Verify Image Imput
    getinput()

    #Generate icons from list
    generateicons(requiredsizes)



if __name__ == "__main__":
    main()