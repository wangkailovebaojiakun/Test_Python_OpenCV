import cv2
import numpy as np

img = cv2.imread('/home/wangkai/Pictures/0.jpg')
img_ROI = img2[100:200,100:200]	

cv2.namedWindow('image')
cv2.imshow('image',img_ROI)

if cv2.waitKey() & 0xFF ==27:
    cv2.destroyAllWindows()
