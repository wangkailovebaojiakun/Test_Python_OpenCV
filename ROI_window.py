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
        img_ROI = img2[x-100:x+100,y-100:y+100]	
        cv2.imshow('image',img_ROI)
img = cv2.imread('/home/wangkai/Pictures/0.jpg')
img2 = img.copy()
img3 = np.zeros(img.shape,'uint8')
width = img2.shape[1]
hight = img2.shape[0]

a = []
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while (1):
    
    img3 = np.zeros(img.shape,'uint8')

    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
