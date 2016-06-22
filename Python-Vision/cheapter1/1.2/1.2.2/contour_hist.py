from PIL import Image
from pylab import *

#read image into an arry
im = array(Image.open('../../IMAGES/sex.jpg').convert('L'))
#create a new figure
figure()
#gray
gray()
#draw  contour
contour(im,origin = 'image')
axis('equal')
axis('off')
figure()
hist(im.flatten(),128)
show()
