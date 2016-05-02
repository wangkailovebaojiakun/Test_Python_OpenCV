import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    print param[0],param[1]
    if event == cv2.EVENT_MOUSEMOVE :
        cv2.circle(img2,(x,y),100,(255,0,0),5)
img = np.zeros((512,512,3),np.uint8)
img2 = img.copy()

a = []
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle,[img2,a])

while (1):
    cv2.imshow('image',img2)
    img2 = img.copy()
    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
