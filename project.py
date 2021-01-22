from PIL import Image
import cv2 as cv
import numpy as np
import random as rng



# Każda operacja na obrazach PIL jest super wolna bo python, więc lepiej ich nie używać.
def scale_pil(source, ratio):
    image = cv_to_pil(source)
    width = image.size[0] * ratio
    height = image.size[1] * ratio
    image = image.resize((int(width), int(height)), Image.ANTIALIAS)

    image = np.array(image)
    return image


def scale_cv(source, ratio):
    image = cv.resize(source, (int(source.shape[1] * ratio),int(source.shape[0] * ratio)))

    return image

def scale(source, ratio):
    # check if pil or cv, apply correct scale function
    return


def gray_pil(source):
    image = cv_to_pil(source)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColor = image.getpixel((i, j))
            newpixel = round((pixelColor[0] + pixelColor[1] + pixelColor[2]) / 3)
            image.putpixel((i, j), (newpixel, newpixel, newpixel))

    image = np.array(image)
    return image


def gray_cv(source):
    image = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

    return image


def luminesence(source, ratio):
    image = cv_to_pil(source)
    newpixel = [1, 2, 3]
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColor = image.getpixel((i, j))
            for k in range(0, 3):
                newpixel[k] = round(float(pixelColor[k]) * float(ratio) / 100)

            image.putpixel((i, j), (newpixel[0], newpixel[1], newpixel[2]))

    image = np.array(image)
    return image


def negative(source):
    image = cv_to_pil(source)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelcolor = image.getpixel((i, j))
            red = 255 - pixelcolor[0]
            green = 255 - pixelcolor[1]
            blue = 255 - pixelcolor[2]
            image.putpixel((i, j), (red, green, blue))

    image = np.array(image)
    return image


def threshold(source, edge_min=0, edge_max=255):
    image = cv_to_pil(source)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelcolor = image.getpixel((i, j))
            avgpixel = sum(pixelcolor) / 3
            if avgpixel < edge_min:
                pixel = 0
            elif avgpixel > edge_max:
                pixel = 0
            else:
                pixel = 255
            image.putpixel((i, j), (pixel, pixel, pixel))

    image = np.array(image)
    return image


def threshold_cv(source):
    if len(source.shape) == 3:
        source = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(source, (7, 7), 0)
    image = cv.threshold(blur, 80, 120, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    return image


def gaussian_cv(source, blocksize, C):
    if len(source.shape) == 3:
        source = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

    if blocksize % 2 == 0:
        blocksize+=1

    image = cv.adaptiveThreshold(source, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blocksize, C)

    return image


def cv_to_pil(source):
    image = Image.fromarray(source)

    return image


def pil_to_cv(source):
    image = np.array(source)

    return image


# Ukradnięte z https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html


def erosion(source, erosion_size):
    shape = 0  # 0 = square, 1 = cross, 2 = circle
    element = cv.getStructuringElement(shape, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                       (erosion_size, erosion_size))

    image = cv.erode(source, element)

    return image


def dilatation(source, dilatation_size):
    shape = 0  # 0 = square, 1 = cross, 2 = circle
    element = cv.getStructuringElement(shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    image = cv.dilate(source, element)

    return image


# Koniec ukradnięcia


def edges(source, thresh_val=125):
    if len(source.shape) == 3:
        source = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
    image = cv.Canny(source, thresh_val, thresh_val * 2)
    return image


def find_contours_to_draw(source):
    edged = edges(source)
    _, contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    return contours


def find_contours(source):
    _, contours, _ = cv.findContours(source, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    return contours


def draw_contours(source):
    contours = find_contours_to_draw(source)
    cv.drawContours(source, contours, -1, (0, 255, 0), 3)

    return source


def draw_rectangles(source, thresh_value=125):
    image = edges(source, thresh_value)
    imageContours = find_contours(image)

    contours_poly = [None] * len(imageContours)
    boundRect = [None] * len(imageContours)
    centers = [None] * len(imageContours)
    radius = [None] * len(imageContours)

    for i, c in enumerate(imageContours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

    drawing = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    for i in range(len(imageContours)):
        color = (255, 0, 0)
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
                     (int(boundRect[i][0] + boundRect[i][2]), int(boundRect[i][1] + boundRect[i][3])), color, 2)

    return drawing


def biggest_rect(source, thresh_val=125):
    image = edges(source, thresh_val)
    imageContours = find_contours(image)

    contours_poly = [None] * len(imageContours)
    boundRect = [None] * len(imageContours)

    for i, c in enumerate(imageContours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    area_max = 0
    rectangle = Rect()
    for i in range(len(imageContours)):
        area = boundRect[i][2] * boundRect[i][3]
        if area > area_max:
            area_max = area
            rectangle.x1 = int(boundRect[i][0])
            rectangle.y1 = int(boundRect[i][1])
            rectangle.x2 = int(boundRect[i][0] + boundRect[i][2])
            rectangle.y2 = int(boundRect[i][1] + boundRect[i][3])

    return rectangle


def mask(source, rect=False):
    if rect is False:
        rect = biggest_rect(source)

    image = np.zeros((source.shape[0], source.shape[1], 3), dtype=np.uint8)
    cv.rectangle(image, (rect.x1, rect.y1), (rect.x2, rect.y2), (255, 255, 255), -1)

    return image


def color_segmentation(source, k=2):
    Z = np.float32(source.reshape((-1, 3)))
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv.kmeans(Z, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((source.shape))

    return res2


class Rect:

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
