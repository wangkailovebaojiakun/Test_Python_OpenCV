#coding:utf-8
#Image Blurring (Image Smoothing)图像模糊（图像平滑）
#Median Filtering中值滤波
#cv2.medianBlur() computes the median of all the pixels under the kernel window 
#and the central pixel is replaced with this median value. 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../IMAGES/sex.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blur = cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()
