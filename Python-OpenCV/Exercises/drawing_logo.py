#coding:utf-8
import cv2
import numpy as np
#mk a black background image
img = np.zeros((900,900,3),np.uint8)
#put text 'OpenCV' on it
font =  cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(210,750),font,4,(255,255,255),10,1)
#draw 3 circle
cv2.circle(img,(450,150),100,(0,0,255),50)
cv2.circle(img,(300,450),100,(0,255,0),50)
cv2.circle(img,(600,450),100,(255,0,0),50)
#draw Polygon(多边形)
pts = np.array([[450,150],[300,450],[600,450]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,0,0),20)
#show image
cv2.imshow('logo',img)
saveKey = cv2.waitKey()& 0xFF
if(saveKey == ord('s')):
    cv2.imwrite('logo.jpg',img)
cv2.destroyAllWindows()
