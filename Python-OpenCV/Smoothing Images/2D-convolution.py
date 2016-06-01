#coding:utf-8
#2D Convolution ( Image Filtering )二维卷积
# images also can be filtered with 
#various low-pass filters (LPF), 不同的低通滤波器
#high-pass filters (HPF)高通滤波器
#OpenCV provides a function, cv2.filter2D(), 
#to convolve a kernel with an image
#Filtering with the above kernel results in the following being performed: 
#for each pixel, a 5x5 window is centered on this pixel, 
#all pixels falling within this window are summed up, 
#and the result is then divided(分为,除) by 25. 
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../IMAGES/sex.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
dst  =cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
