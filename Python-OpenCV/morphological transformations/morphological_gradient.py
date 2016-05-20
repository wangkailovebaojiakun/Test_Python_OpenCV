import cv2
import numpy as np

img = cv2.imread('../IMAGES/j.png',0)
kernel = np.ones((5,5),np.uint8)
#It is the difference between dilation and erosion of an image.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('img',img)
cv2.imshow('gradient',gradient)
cv2.waitKey()
