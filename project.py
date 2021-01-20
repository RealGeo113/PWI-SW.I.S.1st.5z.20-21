from PIL import Image
import cv2 as cv
import numpy as np
import random as rng

def scale(source, ratio):
    image = Image.open(source)
    width = image.size[0] * ratio
    height = image.size[1] * ratio
    resizedimage = image.resize((int(width), int(height)), Image.ANTIALIAS)

    return resizedimage


def gray(source):
    image = Image.open(source);
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColor = image.getpixel((i, j))
            newpixel = round((pixelColor[0]+pixelColor[1]+pixelColor[2])/3)
            image.putpixel((i, j), (newpixel, newpixel, newpixel))

    return image


def gray_cv(source):
    image = cv.imread(source, 0)

    return image


def luminesence(source, ratio):
    image = Image.open(source)
    newpixel = [1,2,3]
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColor = image.getpixel((i, j))
            for k in range(0,3):
                newpixel[k] = round(float(pixelColor[k])*float(ratio)/100)

            image.putpixel((i, j), (newpixel[0], newpixel[1], newpixel[2]))

    return image


def negative(source):
    image = Image.open(source)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelcolor = image.getpixel((i, j))
            red = 255 - pixelcolor[0]
            green = 255 - pixelcolor[1]
            blue = 255 - pixelcolor[2]
            image.putpixel((i, j), (red, green, blue))

    return image


def threshold(source, edge_min, edge_max):
    image = Image.open(source)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelcolor = image.getpixel((i, j))
            avgpixel = sum(pixelcolor)/3
            if avgpixel < edge_min:
                pixel = 0
            elif avgpixel > edge_max:
                pixel = 0
            else:
                pixel = 255
            image.putpixel((i, j), (pixel, pixel, pixel))

    return image


def threshold_cv(source):
    blur = cv.GaussianBlur(cv.cvtColor(source, cv.COLOR_BGR2GRAY), (7, 7), 0)
    image = cv.threshold(blur, 80, 120, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    return image


def gaussian_cv(source):
    source_gray = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
    image = cv.adaptiveThreshold(source_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 15)

    return image


def cv_to_pil(source):
    source = cv.cvtColor(source, cv.COLOR_BGR2RGB)
    image = Image.fromarray(source)

    return image


def mask(source):
    rng.seed(12345)

    def thresh_callback(val):
        threshold = val

        canny_output = cv.Canny(src_gray, threshold, threshold * 2)

        contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        contours_poly = [None] * len(contours)
        boundRect = [None] * len(contours)
        centers = [None] * len(contours)
        radius = [None] * len(contours)
        for i, c in enumerate(contours):
            contours_poly[i] = cv.approxPolyDP(c, 3, True)
            boundRect[i] = cv.boundingRect(contours_poly[i])
            centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        area_max = 0;
        for i in range(len(contours)):
            color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
            cv.drawContours(drawing, contours_poly, i, color)
            cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
                         (int(boundRect[i][0] + boundRect[i][2]), int(boundRect[i][1] + boundRect[i][3])), color, 2)
            # cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
            area = boundRect[i][2] * boundRect[i][3]
            if area > area_max:
                area_max = area
                x1 = int(boundRect[i][0])
                y1 = int(boundRect[i][1])
                x2 = int(boundRect[i][0] + boundRect[i][2])
                y2 = int(boundRect[i][1] + boundRect[i][3])

        whiteboard = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        cv.rectangle(whiteboard, (x1, y1), (x2, y2), (255, 255, 255), -1)
        cv.imshow('Contours', drawing)
        cv.imshow("Whiteboard", whiteboard)

        image = src
        masked_image = cv.subtract(whiteboard, image)
        result = cv.subtract(whiteboard, masked_image)
        result_cropped = result[y1:y2, x1:x2]
        cv.imshow("Result", result_cropped)

    src = cv.imread(source)
    if src is None:
        print('Could not open or find the image:', source)
        exit(0)
    # Convert image to gray and blur it
    width, height, channel = src.shape

    src = cv.resize(src, (int(height/4),int(width/4)))
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    src_gray = cv.blur(src_gray, (3, 3))
    source_window = 'Source'
    cv.namedWindow(source_window)
    cv.imshow(source_window, src)
    max_thresh = 255
    thresh = 170  # initial threshold
    cv.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)
    thresh_callback(thresh)
    cv.waitKey()
    return mask

