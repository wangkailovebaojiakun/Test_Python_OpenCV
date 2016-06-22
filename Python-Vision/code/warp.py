from scipy import ndimage
from numpy import *
import homography

def image_in_image(im1,im2,tp):
    """use affine to put im1 on im2, make im1's angle close to tp"""
    """tp is homogeneous represent, and from the upper left corner by counterclockwise"""
    #twisted points
    m,n = im1.shape[:2]
    fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])
    #compute the affine transform, apply it to im1
    H = homography.Haffine_from_points(tp,fp)
    im1_t = ndimage.affine_transform(im1,H[:2,:2],(H[0,2],H[1,2]),im2.shape[:2])
    alpha = (im1_t > 0)
    return (1-alpha)*im2 + alpha*im1_t
	
