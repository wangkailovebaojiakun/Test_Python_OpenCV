
from scipy.ndimage import filters
from numpy import *
from PIL import Image
import pylab
import cv2
def compute_harris_response(im,sigma=3):
    """In a gray image,count the harris features for every pix"""
    imx = zeros(im.shape)
    filters.gaussian_filter(im,(sigma,sigma),(0,1),imx)
    imy = zeros(im.shape)
    filters.gaussian_filter(im,(sigma,sigma),(1,0),imy)
    cv2.imshow('imx',imx)
    cv2.imshow('imy',imy)
    cv2.waitKey()
    cv2.destroyAllWindows()
    #count Harris mix compment
    Wxx = filters.gaussian_filter(imx*imx,sigma)
    Wxy = filters.gaussian_filter(imx*imy,sigma)
    Wyy = filters.gaussian_filter(imy*imy,sigma)
    #count features value and 
    Wdet = Wxx*Wyy - Wxy**2
    Wtr = Wxx + Wyy
    return Wdet / Wtr 
    """ the fun() above would return an image of harris response value"""
    """ now we would choice some useful information"""
def get_harris_points(harrisim,min_dist=10,threshold=0.1):
    """ return corner point from an harris image"""
    #get the point higher than threshold
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim>corner_threshold)*1
    #get the coords positions
    coords = array(harrisim_t.nonzero()).T
    #get their Harris response value
    candidate_values = [harrisim[c[0],c[1]]for c in coords]
    #sort the candidate points by their Harris response value
    index = argsort(candidate_values)
    #put the points' position on the array
    allowed_locations = zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist,min_dist:-min_dist]=1
    #take the best harris points
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i,0],coords[i,1]]==1:
	    filtered_coords.append(coords[i])
	    allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),(coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0
    return filtered_coords

def plot_harris_points(image,filtered_coords):
    pylab.figure()
    pylab.gray()
    pylab.imshow(image)
    pylab.plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords],'*')
    pylab.axis('off')
    pylab.show()
im = array(Image.open('../IMAGES/B.jpg').convert('L'))
harrisim = compute_harris_response(im)
filtered_coords = get_harris_points(harrisim,6)
plot_harris_points(im,filtered_coords)

