#coding:utf-8
from numpy import *
from pylab import *

def normalize(points):
    """In homogeneous,normalize the points set,make the last row be 1"""
    for row in points:
	row/= points[-1]
    return points

def make_homog(points):
    """turn points set(dim*n array)to homogeneous represent"""
    return vstack((points, ones((1, points.shape[1]))))

def H_from_points(fp,tp):
    """use the DLT method, compute the Homography matrix, mapping fp to tp"""
    if fp.shape != tp.shape:
	raise RuntimeError('number of points do not match')
    #normalize the points
    #----the begin point of mapping---- 
    m = mean(fp[:2],axis=1)
    maxstd = max(std(fp[:2], axis = 1)) +1e-9
    C1 = diag([1/maxstd, 1/maxstd, 1])
    C1[0][2] = -m[0]/maxstd
    c1[1][2] = -m[1]/maxstd
    fp = dot(C1,fp)
    
    #----mapping points----
    m = mean(tp[:2], axis =1)
    maxstd = max(std(tp[:2], axis = 1))+1e-9
    C2 = diag([1/maxstd, 1/maxstd, 1])
    C2[0][2] = -m[0]/maxstd
    C2[1][2] = -m[1]/maxstd
    tp = dot(C2,tp)
    # 
