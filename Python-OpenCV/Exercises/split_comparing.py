import cv2
import numpy as np
import Image

img = cv2.imread('./images/sex.jpg')
fre = cv2.getTickFrequency()
#cv2 splitting Image channels
e_cv_1 = cv2.getTickCount()
b,g,r = cv2.split(img)
e_cv_2 = cv2.getTickCount()
time_cv = (e_cv_2 - e_cv_1)/fre
#numpy splitting Image channels
e_np_1 = cv2.getTickCount()
b_np = img[:,:,0]
g_np = img[:,:,1]
r_np = img[:,:,2]
e_np_2 = cv2.getTickCount()
time_np = (e_np_2 - e_np_1)/fre

#Image splitting Image channels
img = Image.open('./images/sex.jpg')
e_PIL_1 = cv2.getTickCount()
b_I,g_I,r_I = img.split()
e_PIL_2 = cv2.getTickCount()
time_PIL = (e_PIL_2 - e_PIL_1)/fre
print '----time cost----using cv2.tickCount----'
print 'time of cv2:',time_cv
print 'time of numpy:',time_np
print 'time of Image:',time_PIL
print 'min time is:',min(time_cv,time_np,time_PIL)
