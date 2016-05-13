import cv2
import numpy as np
import time

img = cv2.imread('sex.jpg')
cv_start = time.clock()
b,g,r = cv2.split(img)
cv_end = time.clock()
cv_time = cv_end - cv_start
print 'cv time is %f s' %(cv_time)
#cv2.split() is a costly operation (in terms of time), 
#so only use it if necessary. 
#Numpy indexing is much more efficient and should be used if possible.
np_start = time.clock()
b_index = img[:,:,0]
g_index = img[:,:,1]
r_index = img[:,:,2]
np_end = time.clock()
np_time = np_end - np_start
print 'np time is %f s' %(np_time)

if (np_time < cv_time):
    print 'numpy index is faster'
    print 'diff is %f s' %(cv_time - np_time)

#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)
#cv2.imshow('b_index',b_index)
#cv2.imshow('g_index',g_index)
#cv2.imshow('r_index',r_index)
cv2.waitKey()
