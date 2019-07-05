import cv2 as cv
import numpy as np
import os

img = cv.imread('1.jpg')
my_roi = img[500:600, 200:300]
img[300:400, 300:400] = my_roi
cv.imshow('bgr.png', img)
cv.waitKey()
cv.destroyAllWindows()