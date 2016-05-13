import cv2
import numpy as np

img =cv2.imread('sex.jpg')
ball = img[350:500,220:400]
cv2.imshow('ROI',ball)
cv2.imshow('Image',img)
img[0:150,0:180] = ball
cv2.imshow('after',img)
cv2.waitKey()

