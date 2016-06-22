from PIL import Image
from pylab import *

#read image to array
im = array(Image.open('../../IMAGES/sex.jpg'))
#show image
imshow(im)
#some points
x = [10,10,30,40]
y = [20,50,20,50]
#mark the points with red stars
plot(x,y,'r*')
#draw the line of the 2 before points
plot(x[:],y[:],'ks:')
#add title
title('Plotting:sex')
axis('off')
show()
