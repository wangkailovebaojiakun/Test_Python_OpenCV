import warp
from PIL import Image
from pylab import *
#affine example: im1 to im2
im1 = array(Image.open('/home/wangkai/Pictures/beatles69.jpg').convert('L'))
im2 = array(Image.open('/home/wangkai/Pictures/billboard_for_rent.jpg').convert('L'))

#choice some object points
tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])
im3 = warp.image_in_image(im1,im2,tp)
figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()
