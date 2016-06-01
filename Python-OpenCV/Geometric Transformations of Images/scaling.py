#coding:utf-8
#Scaling(缩放) is just resizing of the image.
#Different interpolation(插值) methods are used
#cv2.INTER_AREA for shrinking(萎缩)
#cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming(缩放).
#By default, interpolation method used is cv2.INTER_LINEAR 
#for all resizing purposes.
import cv2
import numpy as np
import time
img = cv2.imread('../IMAGES/sex.jpg')
cv2.imshow('img',img)
print 'img.shape',img.shape
#dst = cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]])
e1 = cv2.getTickCount()
res = cv2.resize(img,None,fx=0.2,fy=0.2,interpolation = cv2.INTER_CUBIC)
e2 = cv2.getTickCount()
print 'res.shape',res.shape
cv2.imshow('res',res)

#or
e3 = cv2.getTickCount()
height,width = img.shape[:2]
res_2 = cv2.resize(img,(int(0.2*width),int(0.2*height)),interpolation = cv2.INTER_CUBIC)
e4 = cv2.getTickCount()
fre = cv2.getTickFrequency()
time_1 = (e2-e1)/fre
time_2 = (e4-e3)/fre
print 'method 1 time is',time_1,'s'
print 'method 2 time is',time_2,'s'

cv2.waitKey()
