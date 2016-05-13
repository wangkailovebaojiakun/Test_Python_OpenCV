#coding:utf-8
import cv2
import numpy as np

img = cv2.imread('sex.jpg')
#access a pixel value by its row and column coordinates. 
#For BGR image, it returns an array of Blue, Green, Red values. 
pix = img[100,100]
print pix
#accessing only blue pixel
blue = img[100,100,0]
print blue
#modify the pixel values the same way.
img[100,100] = [255,255,255]
print img[100,100]
cv2.imshow('img',img)
cv2.waitKey()
#warning
#Numpy is a optimized library for fast array calculations. 
#So simply accessing each and every pixel values and modifying 
#it will be very slow and it is discouraged.
#numpy的是快速的阵列计算的优化库。
#所以，简单地访问和修改每一个像素值将是非常缓慢的，
#它是不被鼓励的
#Note
#For individual pixel access, Numpy array methods, 
#array.item() and array.itemset() is considered to be better. 
#But it always returns a scalar. So if you want to access all B,G,R values, 
#you need to call array.item() separately for all.
print img.item(10,10,2)
img.itemset((10,10,2),100)
print img.item(10,10,2)

