from numpy import *
from PIL import Image

im = array(Image.open('/home/wangkai/Pictures/sex.jpg'))
print im.shape,im.dtype

im = array(Image.open('/home/wangkai/Pictures/sex.jpg').convert('L'),'f')
print im.shape,im.dtype


