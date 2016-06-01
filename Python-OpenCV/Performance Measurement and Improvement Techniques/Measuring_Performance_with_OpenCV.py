import cv2
import numpy as np 
import time
img1 = cv2.imread('../IMAGES/sex.jpg')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print 'median blur time  is',t,'s'
cv2.imshow('img',img1)
e3 = cv2.getTickCount()
t = (e3-e2)/cv2.getTickFrequency()
print 'show image time is',t,'s'
cv2.waitKey()

