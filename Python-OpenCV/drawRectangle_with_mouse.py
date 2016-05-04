import cv2
import numpy as np
import pylab

refPt = []
cropping = False

def click_and_crop(event,x,y,flags,param):
    global refPt,cropping
    if event == cv2.EVENT_LBUTTONDOWN:
	refPt = [(x,y)]
	cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
	refPt.append((x,y))
	cropping = False
    #draw a rectangle around the region of interest
        cv2.rectangle(image,refPt[0],refPt[1],(0,255,0),2)
        cv2.imshow('image',image)


image = np.zeros((512,512,3),np.uint8)
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_and_crop)

while True:
    cv2.imshow('image',image)
    key = cv2.waitKey(1)& 0xFF
    if key == 27:
        image = clone.copy()
    elif key == 120:
        break

if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
    cv2.imshow('ROI',roi)
    cv2.waitKey()    
cv2.destroyAllWindows()



#cv2.rectangle(img,(20,20),(400,400),(255,0,0),5)
#cv2.imshow('cv_img',img)
#xy = pylab.ginput(2)

#print 'Please click 2 points'
#pylab.figure('pylab')
#pylab.imshow(img)

#pylab.show()
#cv2.waitKey()

