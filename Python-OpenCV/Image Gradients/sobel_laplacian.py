import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../IMAGES/plate_1.jpg',0)
s_img = cv2.resize(img,None,fx = 0.2,fy = 0.2,interpolation = cv2.INTER_CUBIC)
#cv2.imshow('img small',s_img)
#cv2.imshow('img',img)
#cv2.waitKey()
#cv2.destroyAllWindows()
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_32F,0,1,ksize=5)

s_laplacian = cv2.Laplacian(s_img,cv2.CV_64F)
s_sobelx = cv2.Sobel(s_img,cv2.CV_32F,1,0,ksize=3)
s_sobely = cv2.Sobel(s_img,cv2.CV_32F,0,1,ksize=3)
plt.figure()	
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.figure()
plt.subplot(2,2,1),plt.imshow(s_img,cmap = 'gray')
plt.title('small Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(s_laplacian,cmap = 'gray')
plt.title('s Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(s_sobelx,cmap = 'gray')
plt.title('s Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(s_sobely,cmap = 'gray')
plt.title('s Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
