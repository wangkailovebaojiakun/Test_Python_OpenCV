import cv2
import numpy as np
import os

path  = os.getcwd()
img_path = path+'/images/sex.jpg'
#reading img without parm 
im = cv2.imread(img_path)
cv2.imshow('img',im)
cv2.waitKey()

