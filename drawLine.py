import cv2
import numpy as np
import pylab

img = np.zeros((512,512),np.uint8)
cv2.line(img,(0,0),(511,511),255,5)
img = cv2.fromarray(img)
cv2.imshow(img)
cv2.waitKey()
