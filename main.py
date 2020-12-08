import project
import cv2

source = input("Enter path to image: ")

scaled = project.scale(source, 2)
grayed = project.gray(source)
luminesence = project.lumi(source, 200)
negative = project.negative(source)
binarization = project.binarization(source, 100)

scaled.show()
grayed.show()
luminesence.show()
negative.show()
binarization.show()
