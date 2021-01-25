from __future__ import print_function
import cv2 as cv
import argparse
from PIL import Image

def histogram(source):
    parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
    parser.add_argument('--input', help='Path to input image.', default=source)
    args = parser.parse_args()
    # src = cv.imread(cv.samples.findFile(args.input))
    src = source
    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)
    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(src)

    dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)
    im_pil = Image.fromarray(dst)

    return im_pil