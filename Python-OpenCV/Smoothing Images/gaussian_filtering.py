#coding:utf-8
#Image Blurring (Image Smoothing)图像模糊（图像平滑）
#Gaussian Filtering
#If you want, you can create a Gaussian kernel 
#with the function, cv2.getGaussianKernel().
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../IMAGES/sex.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#blur = cv2.blur(img,(5,5))
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
