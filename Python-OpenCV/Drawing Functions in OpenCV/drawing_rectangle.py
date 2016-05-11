import numpy as np
import cv2

img = np.zeros(( 512,512,3),np.uint8)
cv2.rectangle(img,(400,10),(100,200),(0,255,0),3)
cv2.imshow('rectangle',img)
cv2.waitKey()

