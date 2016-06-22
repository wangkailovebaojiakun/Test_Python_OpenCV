
from scipy import linalg
from numpy import *

class Camera(object):
    """pinhole camera class"""
    def __init__(self,P):
        """init the P = K[R|t] cam model"""
        self.P = P
    	self.K = None #calibration matrix
    	self.R = None #R
    	self.t = None #t
    	self.c = None #center
    def project(self,X):
        """ X(4*n) projection point,and norm"""
        x = dot(self.P,X)
        for i in range(3):
            x[i] /= x[2]
        return x
    def rotation_matrix(a):
        """ create a matrix around vector a"""
	R = eye(4)
	R[:3,:3] = linalg.expm([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
	return R

    def factor(self):
	""" decompose the cam matrix to K R t and P = K[P|t]"""
        #before decompose the 3*3 part
	K,R = linalg.rq(self.P[:,:3])
	#make the diagonal elements of K to positive
	T = diag(sign(diag(K)))
	if linalg.det(T)<0:
	    T[1,1] *=-1
	self.K = dot(K,T)
	slef.R = dot(T,R) # the reverse of T is its'self
	self.t = dot(linalg.inv(self.K),self.P[:,3])
	return self.K,self.R,self.t
    
    def center(self):
	"""count the center of the camera"""
	if self.c is not None:
	    return self.c
	else:
	    #compute the c by using factor decomposing
	    self.factor()
	    self.c = -dot(self.R.T,self.t)
	    return self.c

    def my_calibration(sz):
	row,col =sz
	fx = 2555

