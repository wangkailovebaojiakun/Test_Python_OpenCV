import cv2
from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('../IMAGES/B.jpg'))
im2 = filters.gaussian_filter(im,5)
#im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
#im2 = cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)
figure()
subplot(1,2,1),imshow(im)
subplot(1,2,2),imshow(im2)
show()

im3 = zeros(im.shape)
for i in range(3):
    im3[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im4 = uint8(im3)
subplot(1,2,1),imshow(im3)
subplot(1,2,2),imshow(im4)
show()

