#coding:utf-8
#Rotation (回转)
#OpenCV provides scaled rotation(缩放旋转) with 
#adjustable center of rotation so that 
#you can rotate at any location you prefer. 
import cv2
import numpy as np

img = cv2.imread('../IMAGES/sex.jpg',0)
rows,cols = img.shape
#To find this transformation matrix, OpenCV provides 
#a function, cv2.getRotationMatrix2D
#M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
M = cv2.getRotationMatrix2D((cols/4,rows/9),45,1)
print M
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('dst',dst)
cv2.waitKey()
