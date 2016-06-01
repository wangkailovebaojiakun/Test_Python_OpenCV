#coding:utf-8
#Image Blending 图像融合
import cv2
import numpy as np
import os
#Both images should be of same depth and type, 
#or second image can just be a scalar value(标量值).
#read logo and image
path = os.getcwd()
parent_path = os.path.dirname(path)
logo_path = parent_path + '/IMAGES/logo.jpg'
logo = cv2.imread(logo_path)
im_path = parent_path + '/IMAGES/sex.jpg'
img = cv2.imread(im_path)
#add weighted
dst = cv2.addWeighted(img,0.7,logo,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey()
