from PIL import Image
from pylab import *

pil_im = Image.open('../../IMAGES/sex.jpg')
out = pil_im.resize((32,32))
out = out.rotate(45)
imshow(out)
show()
