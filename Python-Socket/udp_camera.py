import cv2
import numpy

videoCap = cv2.VideoCapture(0)
isOpened = videoCap.isOpened()
cv2.namedWindow('cam')
count = 0

gotImage = 0
if not isOpened:
    print "Camera is not opened."

else:
    print "Camera is opened."
    gotImage,frame = videoCap.read()

while (isOpened):
#    if(gotImage):
#        print 'gotImage:',gotImage
#    count+=1
   
    print frame.size
    print frame.shape
    frame = cv2.resize(frame,(32,32),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('cam',frame)
    delay  = cv2.waitKey(10)
    gotImage,frame = videoCap.read()

#    else:
#	break
#   stopkey = cv2.waitKey(30)
#   if stopkey == 27:
#        isOpened = 0
#	break
cv2.destroyAllWindows()
