import cv2
import numpy as np

img = cv2.imread('../IMAGES/6.jpg',0)
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('img',img)
cv2.imshow('closing',closing)
cv2.imwrite('6.png',closing)
cv2.waitKey()
