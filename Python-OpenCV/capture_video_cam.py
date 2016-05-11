import numpy as np
import cv2

cap = cv2.VideoCapture(1)
#You can also access some of the features of 
#this video using cap.get(propId) method 
#where propId is a number from 0 to 18. 
# Each number denotes a property of the video 
#(if it is applicable to that video) 
#For example, I can check the frame width and height 
#by cap.get(3) and cap.get(4). It gives me 640x480 by default.
width = cap.get(3)
height = cap.get(4)
print width,height
#But I want to modify it to 320x240. 
#Just use ret = cap.set(3,320) 
#and ret = cap.set(4,240).
cap.set(3,320)
cap.set(4,240)
while(True):
    #Capture frame-by-frame
    ret,frame = cap.read()
    #Our operations on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	break
cap.release()
cv2.destroyAllWindows()

#There is a big problem 
#select timeout
