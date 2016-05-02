import cv2
import numpy as np
import pylab
img = np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(20,20),(400,400),(255,0,0),5)
cv2.imshow('cv_img',img)
pylab.figure('pylab')
pylab.imshow(img)
pylab.show()
cv2.waitKey()
