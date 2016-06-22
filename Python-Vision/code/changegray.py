from PIL import Image
from numpy import *

im = array(Image.open(('/home/wangkai/Pictures/B.jpg').convert('L'))

im2 = 25 - im # reverse the im

im3 = (100.0/255)*im +100 #change the pix into range (100,200)

im4 = 255.0*(im/255.0)**2 #square the pix value 

print int(im.min()),int(im.max())

