import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,0,255),2)
cv2.imshow('polygon',img)
cv2.waitKey()
