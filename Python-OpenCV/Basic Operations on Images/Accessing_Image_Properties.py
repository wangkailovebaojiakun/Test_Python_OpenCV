import cv2
import numpy as np

img = cv2.imread('sex.jpg')
print img.shape
#otal number of pixels is accessed by img.size:
print img.size
print img.dtype
