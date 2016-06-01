from PIL import Image
from pylab import *

pil_im = Image.open('../../IMAGES/sex.jpg')
box = (50,50,80,90)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)

imshow(pil_im)
#imshow(region)
show()
