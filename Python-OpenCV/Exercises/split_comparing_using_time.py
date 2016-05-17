import cv2
import numpy as np
import Image
import time
img = cv2.imread('./images/sex.jpg')
#cv2 splitting Image channels
e_cv_1 = time.time()
b,g,r = cv2.split(img)
e_cv_2 = time.time()
time_cv = (e_cv_2 - e_cv_1)
#numpy splitting Image channels
e_np_1 = time.time()
b_np = img[:,:,0]
g_np = img[:,:,1]
r_np = img[:,:,2]
e_np_2 = time.time()
time_np = (e_np_2 - e_np_1)

#Image splitting Image channels
img = Image.open('./images/sex.jpg')
e_PIL_1 = time.time()
b_I,g_I,r_I = img.split()
e_PIL_2 = time.time()
time_PIL = (e_PIL_2 - e_PIL_1)
print '----time cost----using time----'
print 'time of cv2:',time_cv
print 'time of numpy:',time_np
print 'time of Image:',time_PIL
print 'min time is:',min(time_cv,time_np,time_PIL)
