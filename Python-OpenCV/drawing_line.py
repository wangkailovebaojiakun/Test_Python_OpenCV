from numpy import *
import cv2

#create a black image
img = zeros((800,800,3),'uint8')
#Draw a diagonal blue line withe thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
if (img.data):
    cv2.imshow('img',img)
else:
    print 'img is wrong!'
cv2.waitKey()

