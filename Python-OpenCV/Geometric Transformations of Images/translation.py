#coding:utf-8
#Translation(平移) is the shifting(移动) of object’s location. 
#If you know the shift in (x,y) direction,
#you can create the transformation matrix
#You can take make it into a Numpy array of type 
#np.float32 and pass it into cv2.warpAffine() function.
import cv2
import numpy as np
img = cv2.imread('../IMAGES/sex.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

