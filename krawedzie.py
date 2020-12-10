import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import project

def krawedzie(source):

    img = cv.imread(source,0)
    edges = cv.Canny(img,100,200)
    edges = project.cv_to_pil(edges)
    return edges
