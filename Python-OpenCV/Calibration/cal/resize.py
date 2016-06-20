import cv2
import glob
import numpy as np

images = glob.glob('*.jpg')
for fname in images:
    img = cv2.imread(fname)
    res = cv2.resize(img,None,fx = 0.1,fy=0.1,interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(fname,res)
