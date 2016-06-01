from PIL import Image
import numpy as np
import cv2
from pylab import *
print 'PIL read an image as RGB mode.'
pil_im =Image.open('../IMAGES/sex.jpg')
pil_im_l = pil_im.convert('L')
print 'The size of PIL image objects:'
print pil_im.size,pil_im_l.size
print 'Turn PIL object to array'
array1 = np.array(pil_im)
array2 = np.array(pil_im_l)
print 'The shape of it and its convert L:'
print array1.shape,array2.shape
print 'Pylab show the image as RGB mode'
print 'If we need gray mode,gray() should be used.'
figure()
subplot(1,2,1),imshow(pil_im)
subplot(1,2,2),imshow(pil_im_l,'gray')
show()

print 'opencv show an image as BGR mode'
cv2.imshow('a1',array1)
cv2.imshow('a2',array2)
cv2.waitKey()
cv2.destroyAllWindows()
