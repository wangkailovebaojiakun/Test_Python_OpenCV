import cv2
import numpy as np,sys

img1 = cv2.imread('../IMAGES/p1.jpg')
img2 = cv2.imread('../IMAGES/p2.jpg')
#print A.shape,B.shape
#ha,wa = A.shape[:2]
#hb,wb = B.shape[:2]
A = cv2.resize(img1,(1024,2048),interpolation = cv2.INTER_CUBIC)
B = cv2.resize(img2,(1024,2048),interpolation = cv2.INTER_CUBIC)
# generate Gaussian pyramid for A
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    print i
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    print i
    GE = cv2.pyrUp(gpA[i])
    print gpA[i-1].shape,GE.shape
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

print len(la),len(lb)
# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
