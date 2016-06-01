#coding:utf-8
#Bitwise Operations 位运算
#This includes bitwise AND, OR, NOT and XOR operations. 
#这包括按位AND，OR，NOT和XOR运算
#OpenCV logo is a not a rectangular shape. (不是一个矩形形状)
#So you can do it with bitwise operations as below:
import cv2
import os
import numpy as np

#read two image
path = os.getcwd()
parent_path = os.path.dirname(path)
logo_path = parent_path + '/IMAGES/logo.jpg'
img_path = parent_path + '/IMAGES/sex.jpg'
print logo_path
print img_path
img1 = cv2.imread(logo_path)
img2 = cv2.imread(img_path)
#if (img1.data):
#    cv2.imshow('img1',img1)
#if (img2.data):
#    cv2.imshow('img2',img2)
#
#resize img1 to a small shape
logo = cv2.resize(img1,(240,240),interpolation = cv2.INTER_LINEAR)
cv2.imshow('img1',logo)
#put the logo on top-left corner,create a ROI
rows,cols,channels = logo.shape
#print logo.shape
roi = img2[0:rows,0:cols]
#Now create a mask of logo and create its inverse(逆)
img2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
rect,mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
#Now black-out the area of logo in ROI
#img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img_bg = roi
#Take only region of logo from logo image
logo_fg = cv2.bitwise_and(logo,logo,mask = mask)
#Put logo in ROI and modify the main image
#Create a slide show of images in a folder 
#with smooth transition between images 
#using cv2.addWeighted function
dst = cv2.addWeighted(img_bg,1,logo_fg,0.2,0)
cv2.imshow('dst',dst)
img2[0:rows,0:cols] = dst
cv2.imshow('res',img2)
cv2.waitKey()
