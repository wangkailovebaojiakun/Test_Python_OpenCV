#coding:utf-8
#Scaling(缩放) is just resizing of the image.
#Different interpolation(插值) methods are used
#cv2.INTER_AREA for shrinking(萎缩)
#cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming(缩放).
#By default, interpolation method used is cv2.INTER_LINEAR 
#for all resizing purposes.
import cv2
import time
import numpy as np
from pylab import *
from matplotlib import pyplot as plt

img1 = cv2.imread('../IMAGES/affine_1.jpg')
img2 = cv2.imread('../IMAGES/affine_2.jpg')

#cv2.imshow('img',img)
print 'img1.shape',img1.shape
#dst = cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]])
e1 = cv2.getTickCount()
#
res1 = cv2.resize(img1,None,fx=0.1,fy=0.1,interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(img2,None,fx=0.1,fy=0.1,interpolation = cv2.INTER_CUBIC)
res_1 = cv2.cvtColor(res1,cv2.COLOR_BGR2RGB)
res_2 = cv2.cvtColor(res2,cv2.COLOR_BGR2RGB)
#
e2 = cv2.getTickCount()
fre = cv2.getTickFrequency()
time_1 = (e2-e1)/fre

#cv2.imshow('res1',res1)
#cv2.imshow('res2',res2)
#cv2.waitKey()
rows,cols,ch = res1.shape
print 'res1.shape',rows,cols,ch
print 'time is',time_1,'s'
plt.subplot(121),plt.imshow(res_1),plt.title('img1')
plt.subplot(122),plt.imshow(res_2),plt.title('img2')
#print 'Please click 1th points pair:'
print 'Please click 3 points at img2:'
x1 = ginput(3)
print 'you clicked:',floor(x1)
print 'Please click 3 points at img2:'
#print 'Please click 1th points pair:'
x2 = ginput(3)
print 'you clicked:',floor(x2)
plt.show()
pts1 = np.float32(x1)
pts2 = np.float32(x2)
print pts1
print pts2
M1 = cv2.getAffineTransform(pts1,pts2)
M2 = cv2.getAffineTransform(pts2,pts1)
print M1

dst1 = cv2.warpAffine(res1,M1,(cols,rows))
dst2 = cv2.warpAffine(res2,M2,(cols,rows))
output_1 = cv2.cvtColor(dst1,cv2.COLOR_BGR2RGB)
output_2 = cv2.cvtColor(dst2,cv2.COLOR_BGR2RGB)
cv2.circle(res_1,tuple(pts1[0]),1,(0,0,255),-1)
cv2.circle(res_1,tuple(pts1[1]),1,(0,0,255),-1)
cv2.circle(res_1,tuple(pts1[2]),1,(0,0,255),-1)
cv2.circle(res_2,tuple(pts2[0]),1,(0,0,255),-1)
cv2.circle(res_2,tuple(pts2[1]),1,(0,0,255),-1)
cv2.circle(res_2,tuple(pts2[2]),1,(0,0,255),-1)

plt.subplot(141),plt.imshow(res_1),plt.title('Input1')
plt.subplot(142),plt.imshow(res_2),plt.title('Input2')
plt.subplot(143),plt.imshow(output_1),plt.title('output1')
plt.subplot(144),plt.imshow(output_2),plt.title('output2')

plt.show()
