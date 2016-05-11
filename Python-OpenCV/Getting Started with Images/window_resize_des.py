import cv2
import os
from imtools import *

img_path = TEST_IMAGE_PATH
print TEST_IMAGE_PATH
im = cv2.imread(img_path)
#By default, the flag is cv2.WINDOW_AUTOSIZE
cv2.namedWindow('image')
cv2.imshow('image',im)
#But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window. 
# It will be helpful when image is too large in dimension 
#and adding track bar to windows.
cv2.namedWindow('image_',cv2.WINDOW_NORMAL)
cv2.imshow('image_',im)
cv2.waitKey()
#cv2.destroyWindow() where you pass the exact window name as the argument.
cv2.destroyWindow('image_')
cv2.waitKey()
#cv2.destroyAllWindows() simply destroys all the windows we created
cv2.destroyAllWindows()
