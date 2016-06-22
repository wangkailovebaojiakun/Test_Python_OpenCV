from PIL import Image
from pylab import *

im = array(Image.open('/home/wangkai/Pictures/[192.168.1.166]-[49]-[306774].jpg'))
imshow(im)
print 'Please click 3 points:'
x = ginput(3)
print 'you clicked:',x
show()

