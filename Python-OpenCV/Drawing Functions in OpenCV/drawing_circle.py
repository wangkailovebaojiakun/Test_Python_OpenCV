import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)
#if the last parm is -1 it would be a full
#cv2.circle(img,(400,100),50,(0,0,255),-1)
#if the last parm is >0,it would be boundry
cv2.circle(img,(400,100),50,(0,0,255),2)
cv2.imshow('circle',img)
cv2.waitKey()

