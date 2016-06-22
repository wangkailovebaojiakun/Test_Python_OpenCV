import cam
from numpy import *
from pylab import *
#load the points
points = loadtxt('house.p3d').T
points = vstack((points,ones(points.shape[1])))

# set the camera pram
P = hstack((eye(3),array([[0],[0],[-10]])))
c = cam.Camera(P)
x = c.project(points)
#draw projection
figure()
plot(x[0],x[1],'k.')
show()
