
import cv2
import numpy as np
def window_move(event,x,y,flags,param):
    m_x = 0
    m_y = 0
    if event == cv2.EVENT_LBUTTONUP:
        m_x = x
        m_y = y
    if event == cv2.EVENT_LBUTTONDOWN:
	print m_x,m_y
    cv2.namedWindow('test')
    #if (flags==cv2.EVENT_FLAG_SHIFTKEY)&(event==cv2.EVENT_MOUSEMOVE):
    if flags==cv2.EVENT_FLAG_LBUTTON:
        print 'move:',m_x,m_y
        if x-50<0:
	    x = 50
	if y-50<0:
	    y = 50
        img_ROI = img2[x-50:x+50,y-50:y+50]
        cv2.imshow('test',img_ROI) 
img = cv2.imread('/home/wangkai/Pictures/0.jpg')
img2 = img.copy()
img_ROI = img2[100:200,100:200]	
width = img.shape[1]
hight = img.shape[0]

cv2.namedWindow('image')
cv2.setMouseCallback('image',window_move)

while (1):
    
    cv2.imshow('image',img_ROI)

    if cv2.waitKey(30) & 0xFF ==27:
	break
cv2.destroyAllWindows()
