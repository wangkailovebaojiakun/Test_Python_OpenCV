#coding:utf-8
import cv2
import numpy as np

img = cv2.inmread('noise-1.png',0)
blur = cv2.GaussianBlur(img,(5,5),0)
#find normalized_histogram, and its cumulative distribution function
#直方图计算函数
#原型为cv2.calcHist
#(images, channels, mask, histSize, ranges[, hist[, accumulate ]]) 
#返回hist
#[blur]第一个参数必须用方括号括起来 
#使用的通道 [0]
#没有使用mask None
#HistSize表示这个直方图分成多少份（即多少个直方柱） [256]
#直方图柱的范围,表示直方图中各个像素的值 [0,256]
hist = cv2.calcHist([blur],[0],None,[256],[0,256])
#ravel()  平坦化数组(x = np.array([[1, 2, 3], [4, 5, 6]]))
#np.ravel(x) = [1 2 3 4 5 6] 
hist_norm = hist.ravel()/hist.max()
#Return the cumulative sum of the elements along a given axis.
#返回沿给定轴线的元素的累计总和。
Q = hist_norm.cumsum()
#arange函数用于创建等差数组
#numpy.arange([start, ]stop, [step, ]dtype=None)
bins = np.arrange(256)
#infinity 无穷
fn_min  = np.inf
thresh = -1

for i in xrange(1,256):
    p1,p2 = np.hsqlit(hist_norm,[i])# probabilities概率
    q1,q2 = Q[i],Q[255]-Q[i]# cum sum of classes类的累计总和
    b1,b2 = np.hsplit(bins,[i]) # weights
    # finding means and variances方差
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print thresh,ret
