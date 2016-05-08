import cv2
import numpy as np
import os

path  = os.getcwd()
#this is a right path
img_path = path+'/images/sex.jpg'
#this is a wrong path
img_F_path = path +'sex.jpg'
#if the image path is warong it won't throw an error
#but print img will give you NONE

#reading img without parm 
im = cv2.imread(img_path)
cv2.imshow('img',im)
#won't throw an  error
im_F = cv2.imread(img_F_path)
#give None
print im_F
#won't throw an error
cv2.imshow('img',im)
cv2.waitKey()

