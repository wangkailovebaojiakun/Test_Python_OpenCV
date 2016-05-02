import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    print x,y
    if event == cv2.EVENT_MOUSEMOVE :
        if x<= 105:
	    x = 105
	if x>= width-105:
	    x = width-105
	if y<= 105:
	    y = 105
	if y>= hight-105:
	    y = hight-105    
        cv2.rectangle(img2,(x-100,y-100),(x+100,y+100),(0,255,0),5)	
        
img = cv2.imread('/home/wk/Pictures/sex.jpg')
img2 = img.copy()
width = img2.shape[0]
hight = img2.shape[1]

a = []
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle,[img2,a])

while (1):
    cv2.imshow('image',img2)
    img2 = img.copy()
    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
