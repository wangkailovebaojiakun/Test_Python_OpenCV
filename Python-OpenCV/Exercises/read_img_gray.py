import cv2
import numpy as np
import os

path  = os.getcwd()
img_path = path+'/images/sex.jpg'
#reading img with parm 0 means convert to gray 
im = cv2.imread(img_path,0)
cv2.imshow('img',im)
cv2.waitKey()

