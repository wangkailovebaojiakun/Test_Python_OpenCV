import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX
img = np.zeros((512,512,3),np.uint8)
cv2.putText(img,'TextOpenCV',(20,256),font,2,(255,255,0),8,2)
cv2.imshow('Text',img)
cv2.waitKey()
