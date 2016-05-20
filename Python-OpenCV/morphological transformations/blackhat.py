import cv2
import numpy as np

img = cv2.imread('../IMAGES/j.png',0)
kernel = np.ones((5,5),np.uint8)
#It is the difference between the closing 
#of the input image and input image.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('img',img)
cv2.imshow('blackhat',blackhat)
cv2.waitKey()
