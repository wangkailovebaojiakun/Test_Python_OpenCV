#coding:utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#这里没有系统如果没有编码器，写出的视频是0kb
fourcc = cv2.cv.CV_FOURCC(*'XVID')
#fourcc = cv2.cv.CV_FOURCC(*'MJPG')
#这里如果把cv2.VideoWirter的第二个参数设为-1
#程序运行时则会交互地弹出一个对话框让你从系统已有的编码中选择一个。
out = cv2.VideoWriter('output.avi',-1,19.0,(640,480))
while(cap.isOpened()):
    flag,frame = cap.read()
    if flag == True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
