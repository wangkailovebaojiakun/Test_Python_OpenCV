from PIL import Image
from pylab import *

pil_im = Image.open('../../IMAGES/B.jpg')
test = pil_im.thumbnail((128,128))
print test
imshow(pil_im)
show()
