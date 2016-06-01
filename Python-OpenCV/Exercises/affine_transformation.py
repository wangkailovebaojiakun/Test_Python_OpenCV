#coding:utf-8
#Affine Transformation(仿射变换)
#Affine Transformation是一种二维坐标到二维坐标之间的线性变换，
#保持二维图形的“平直性”（译注：straightness，即变换后直线还是直线不会打弯，
#圆弧还是圆弧）和“平行性”（译注：parallelness，其实是指保二维图形间的
#相对位置关系不变，平行线还是平行线，相交直线的交角不变。）。
#仿射变换可以通过一系列的原子变换的复合来实现，包括：
#平移（Translation）、缩放（Scale）、翻转（Flip）、旋转（Rotation）
#和剪切（Shear）。
#此类变换可以用一个3×3的矩阵来表示，其最后一行为(0, 0, 1)。
#In affine transformation, all parallel(平行) lines 
#in the original image will still be parallel in the output image. 
#To find the transformation matrix, we need three points from input image and 
#their corresponding locations in output image. 
#Then cv2.getAffineTransform will create a 2x3 matrix 
#which is to be passed to cv2.warpAffine.
import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread('../IMAGES/affine_1.jpg')
img2 = cv2.imread('../IMAGES/affine_1.jpg')
rows,cols,ch = img1.shape
#max_boundry = max(rows,cols)

res = cv2.resize(img1,None,0.2,0.2,cv2.INTER_CUBIC)

#if (max_boundry>300):
cv2.imshow('res',res)
#cv2.imshow('img2',img2)
cv2.waitKey()

#pts1 = np.float32([[50,50],[200,50],[50,200]])
#pts2 = np.float32([[10,100],[200,50],[100,250]])

#M = cv2.getAffineTransform(pts1,pts2)

#dst = cv2.warpAffine(img,M,(cols,rows))

#plt.subplot(121),plt.imshow(img),plt.title('Input')
#plt.subplot(122),plt.imshow(dst),plt.title('Output')
#plt.show()
