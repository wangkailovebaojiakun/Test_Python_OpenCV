#coding:utf-8
#Image Blurring (Image Smoothing)图像模糊（图像平滑）
#Bilateral Filtering(双边滤波)
#双边滤波（Bilateral filter）是一种可以保边去噪的滤波器。之所以可以达到此去噪效果，是因为滤波器是由两个函数构成。
#一个函数是由几何空间距离决定滤波器系数。另一个由像素差值决定滤波器系数。
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../IMAGES/sex.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#blur = cv2.blur(img,(5,5))
blur = cv2.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
