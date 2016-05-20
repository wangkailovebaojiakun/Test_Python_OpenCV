import cv2
import numpy as np

img = cv2.imread('../IMAGES/j.png',0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('img',img)
cv2.imshow('closing',closing)
cv2.waitKey()
