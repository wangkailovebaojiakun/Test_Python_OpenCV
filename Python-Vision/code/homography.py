
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
    #build the DLT matrix,for each responsing points, it would be 2 row of values in the matrix
    nbr_correspondes = fp.shape[1]
    A = zeros((2*nbr_corresponds,9))
    for i in range(nbr_correspondences):
    	A[2*i] = [ -fp[0][i], -fp[1][i],-1,0,0,0, fp[0][i]*fp[0][i], fp[0][i]* fp[1][i], tp[0][i] ]
        A[2*i+1] = [ 0,0,0, -fp[0][i], -fp[1][i], -1, tp[1][i]*fp[0][i], tp[1][i]*fp[1][i], tp[1][i]]
    U, S, V = linalg.svd(A)
    # inverse normalize
    H = dot(linalg.inv(C2),dot(H,C1))
    # normalize and return
    return H/H[2,2] 
 
def Haffine_from_points(fp,tp):
    """compute H,haffine,make tp is from fp by haffine"""
    if fp.shape!=tp.shape:
	raise RuntimeError('Number of points do not match')
    """normalize the points"""
    """---begin of mapping---"""
    m = mean(fp[:2],axis=1)
    maxstd = max(std(fp[:2],axis=1))+1e-9
    C1 = diag([1/maxstd, 1/maxstd,1])
    C1[0][2] = -m[0]/maxstd
    C1[1][2] = -m[1]/maxstd
    fp_cond = dot(C1,fp)
    #---mapping response points---
    m = mean(tp[:2],axis=1)
    C2 = C1.copy()#two points sets, must same scale
    C2[0][2] = -m[0]/maxstd
    C2[1][2] = -m[1]/maxstd
    tp_cond = dot(C2,tp)

    #beacuse the mean is 0 after normalize,so the t is zeor
    A = concatenate((fp_cond[:2],tp_cond[:2]),axis = 0)
    U,S,V = linalg.svd(A.T)
    #as Hartley and Zisserman's "Multiple View Geometry in Computer, Scond Edition"
    #build the maxtrix B and C
    tmp = V[:2].T
    B = tmp[:2]
    C = tmp[2:4]

    tmp2 = concatenate((dot(C,linalg.pinv(B)),zeros((2,1))),axis=1)
    H = vstack((tmp2,[0,0,1]))

    #inverse normalize
    H = dot(linalg.inv(C2),dot(H,C1))

    return H/H[2,2]
	
class RansacModel(object):
    """a class to test the homography matrix"""
    def __init__(self, debug = False):
	self.debug = debug

    def fit(self, data):
	"""compute the 4 choiced homography matrix"""
	data = data.T
    	#the begin of mapping
    	fp = data[:3,:4]
    	#object points to map
    	tp = data[3:,:4]
    	#compute the homography matrix and return
    	return H_from_points(fp,tp)
    
    def get_error(self, data, H):
	"""compute the homography matrix for all the points, and to each return the error"""
	data = data.T
	#begin to mapping
	fp = data[:3]
	#object points
	tp = data[3:]
	#trans fp
	fp_transformed = dot(H, fp)
	#normalized
	for i in range(3):
	    fp_transformed[i] /= fp_transformed[2]
	
	#return each error
	return sqrt( sum((tp - fp_transformed)**2,axis = 0))

def H_from_ransac(fp, tp, model, maxiter = 1000, match_theshold =10):
    """use RANSAC to compute the H"""
    #input :Homogeneous represent points fp, tp(3*n array)
    import ransac
    #correspond points
    data = vstack((fp,tp))
    #compute H,return
    H,ransac_data = ransac.ransac(data.T, model, 4, maxiter, match_threshold, 10, return_all=True)
    return H,ransac_data['inliers']

def convert_points(j):
    ndx = matches[j].nonzero()[0]
    fp = homography.make_homog(l[j+1][ndx,:2].T)
    ndx2 = [int(matches[j][i]) for i in ndx]
    tp = homography.make_homog(l[j][ndx2,:2].T)
    return fp,tp

