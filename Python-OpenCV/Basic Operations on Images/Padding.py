#coding:utf-8
#Making Borders for Images (Padding)
#图像制作边框（填充）
import cv2
import numpy as np
from matplotlib import  pyplot as plt
#cv2.copyMakeBorder() can create a border 
#around the image, something like a photo frame
#more applications for convolution operation(卷积运算), 
#zero padding(零填充) etc
#This function takes following arguments:
#borderType - Flag defining what kind of border to be added. 
#It can be following types:
#cv2.BORDER_CONSTANT - Adds a constant colored border(常量彩色边框). 
#The value should be given as next argument.
#cv2.BORDER_REFLECT - Border will be mirror reflection 
#of the border elements, 边框是边界元素的镜面反射，就像这样
#like this : fedcba|abcdefgh|hgfedcb
#cv2.BORDER_REPLICATE - Last element is replicated throughout, 
#最后一个元素被复制贯穿始终，
#like this: aaaaaa|abcdefgh|hhhhhhh
BLUE = [255,0,0]
img = cv2.imread('sex.jpg')
#replicate 复制
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
#reflect 反射 
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
#reflect101 
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
#wrap 包
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
#constant 常量
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)


plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
