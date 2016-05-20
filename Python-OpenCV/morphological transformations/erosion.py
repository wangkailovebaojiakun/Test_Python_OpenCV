import cv2
import numpy as np

img = cv2.imread('../IMAGES/j.png')
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('img',img)
cv2.imshow('erosion',erosion)
cv2.waitKey()
