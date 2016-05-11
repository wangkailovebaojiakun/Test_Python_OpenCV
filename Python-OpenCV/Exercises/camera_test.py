import cv2  
import cv
cameraCapture = cv2.VideoCapture(0)  
#cameraCapture.set(CV_CAP_PROP_FRAME_WIDTH,352);
#cameraCapture.set(CV_CAP_PROP_FRAME_HEIGHT,288);
fps = 30 # an assumption  
size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))  
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)  
success, frame = cameraCapture.read()  

numFramesRemaining = 10 * fps - 1  
while success and numFramesRemaining > 0:  
    videoWriter.write(frame)  
    success, frame = cameraCapture.read()  
    numFramesRemaining -= 1 
