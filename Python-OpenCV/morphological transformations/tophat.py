import cv2
import numpy as np

img = cv2.imread('../IMAGES/j.png',0)
kernel = np.ones((5,5),np.uint8)
#It is the difference between input image and Opening of the image.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('img',img)
cv2.imshow('tophat',tophat)
cv2.waitKey()
