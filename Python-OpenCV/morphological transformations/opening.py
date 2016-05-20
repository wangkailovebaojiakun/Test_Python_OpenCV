import cv2
import numpy as np

img = cv2.imread('../IMAGES/j.png',0)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('img',img)
cv2.imshow('opening',opening)
cv2.waitKey()

