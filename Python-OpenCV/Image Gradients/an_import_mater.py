#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../IMAGES/plate_2.jpg',0)
#Black-to-White transition(过渡) is taken as Positive slope(正斜率) 
#(it has a positive value) while White-to-Black transition 
#is taken as a Negative slope (It has negative value). 
#So when you convert data to np.uint8, all negative slopes 
#are made zero. In simple words, you miss that edge.
# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()

