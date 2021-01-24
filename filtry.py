from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

def filtry (source, type):
    # img = Image.open(source)
    img = source

    if type == 1:
        img1 = img.filter(BLUR)

    if type == 2:
        img1 = img.filter(CONTOUR)

    if type == 3:
        img1 = img.filter(DETAIL)

    if type == 4:
        img1 = img.filter(EDGE_ENHANCE)

    if type == 5:
        img1 = img.filter(EDGE_ENHANCE_MORE)

    if type == 6:
        img1 = img.filter(EMBOSS)

    if type == 7:
        img1 = img.filter(FIND_EDGES)

    if type == 8:
        img1 = img.filter(SMOOTH)

    if type == 9:
        img1 = img.filter(SMOOTH_MORE)

    if type == 10:
        img1 = img.filter(SHARPEN)

    return img1
