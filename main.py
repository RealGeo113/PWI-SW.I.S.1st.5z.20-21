import project
import OCR
import filtry
import cv2 as cv
from PIL import Image
import numpy
import histogram

# source = input("Enter path to image: ")
source = "./3.jpg"

# scaled = project.scale_cv(source, 0.1)
# grayed = project.gray_pil(source)
# luminesence = project.luminesence(source, 200)
# negative = project.negative(source)
# threshold = project.threshold(source, 50, 135)
# opticalCharacterRecognition = OCR.OCR(source, "pol")
# edges = krawedzie.krawedzie(source)
filters = filtry.filtry(source, 6)
# hist = histogram.histogram(source)
# scaled.show()
# grayed.show()
# luminesence.show()
# negative.show()
# threshold.show()
# print(opticalCharacterRecognition)
# edges.show()
filters.show()
# hist.show()

# project.mask(source)

