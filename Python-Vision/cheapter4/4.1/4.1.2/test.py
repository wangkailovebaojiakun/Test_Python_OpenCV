import cam
from numpy import *
from pylab import *

K = array([[1000,0,500],[0,1000,300],[0,0,1]])
tmp = cam.rotation_matrix([0,0,1])[:3,:3]
Rt = hstack((tmp,array([[50],[40],[30]])))
c = cam.Camera(dot(K,Rt))

print K,Rt
print c.factor()
