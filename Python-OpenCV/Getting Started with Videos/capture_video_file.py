#coding:utf-8
import cv2
import numpy as np
#if videocapture is wrong ,won't throw an error
#cap = cv2.VideoCapture('Star.Wars.Episode.II.Attack.of.the.Clones.2002.BluRay.iPad.720p.x264.AAC-BYRPAD.mp4')
#if can't open the video,won't throw an error
#cap = cv2.VideoCapture("D:\\Star.Wars.Episode.II.Attack.of.the.Clones.2002.BluRay.iPad.720p.x264.AAC-BYRPAD.mp4")
cap = cv2.VideoCapture("C:/Users/kai/Desktop/毕业论文/视频与图片/videohighwayI_raw.avi")
while(cap.isOpened()):
    flag,frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
