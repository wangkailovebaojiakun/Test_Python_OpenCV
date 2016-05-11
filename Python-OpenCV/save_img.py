import cv2
import numpy as np
from imtools import *

im_path = TEST_IMAGE_PATH
print im_path
img = cv2.imread(im_path,0)
cv2.imshow('image',img)
#If you are using a 64-bit machine, 
#you will have to modify k = cv2.waitKey(0) line 
#as follows : k = cv2.waitKey(0) & 0xFF
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
#if path is wrong won't throw an error
    cv2.imwrite('./images/sexgray.png',img)
    cv2.destroyAllWindows()


