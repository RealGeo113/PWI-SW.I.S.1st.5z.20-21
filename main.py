import project
import OCR
import krawedzie
import cv2 as cv
from PIL import Image
import numpy

# source = input("Enter path to image: ")
source = "6.jpg"

scaled = project.scale(source, 2)
# grayed = project.gray(source)
# luminesence = project.luminesence(source, 200)
# negative = project.negative(source)
# threshold = project.threshold(source, 50, 135)
# opticalCharacterRecognition = OCR.OCR(source, "pol")
# edges = krawedzie.krawedzie(source)
scaled.show()
# grayed.show()
# luminesence.show()
# negative.show()
# threshold.show()
# print(opticalCharacterRecognition)
# edges.show()

project.mask(source)

