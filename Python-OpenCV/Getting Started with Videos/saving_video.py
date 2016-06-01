#coding:utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#����û��ϵͳ���û�б�������д������Ƶ��0kb
fourcc = cv2.cv.CV_FOURCC(*'XVID')
#fourcc = cv2.cv.CV_FOURCC(*'MJPG')
#���������cv2.VideoWirter�ĵڶ���������Ϊ-1
#��������ʱ��ύ���ص���һ���Ի��������ϵͳ���еı�����ѡ��һ����
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
