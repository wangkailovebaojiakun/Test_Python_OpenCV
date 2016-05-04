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
        cv2.rectangle(img3,(x-100,y-100),(x+100,y+100),(255,255,255),-1)	
        
img = cv2.imread('/home/wk/Pictures/pano.jpg')
img2 = img.copy()
img3 = np.zeros(img.shape,'uint8')
width = img2.shape[1]
hight = img2.shape[0]

a = []
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle,[img2,a])

while (1):
    frame = img3&img
    cv2.imshow('image',frame)
    img3 = np.zeros(img.shape,'uint8')

    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
