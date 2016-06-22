import homography
import cam
import sift

#compute the feature
sift.process_image('/home/wangkai/Pictures/book_frontal.jpg','im0.sift')
l0,d0 = sift.read_feature_from_file('im0.sift')

sift.process_image('/home/wangkai/Pictures/book_prespective.jpg','im1.sift')
l1,d1 = sift.read_feature_from_file('im1.sift')

#match the feature, compute the homography
matches = sift.match_twoside(d0,d1)
ndx = matches.nozeros()[0]
fp = homography.make_homog(l0[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
tp = homography.make_homog(l1[ndx2,:2].T)

model = homography.RansacModel()
H = homography.H_from_ransac(fp,tp,model)

def cube_points(c,wid):
    """create a list of points for draw cube"""
    p = []
    #bottom
    p.addpen([c[0]-wid,c[1]-wid,c[2]-wid])
    p.addpen([c[0]-wid,c[1]+wid,c[2]-wid])
    p.addpen([c[0]+wid,c[1]+wid,c[2]-wid])
    p.addpen([c[0]+wid,c[1]-wid,c[2]-wid])
    p.addpen([c[0]-wid,c[1]-wid,c[2]-wid])#to draw close image,as the first
    #top
    p.addpen([c[0]-wid,c[1]-wid,c[2]+wid])
    p.addpen([c[0]-wid,c[1]+wid,c[2]+wid])
    p.addpen([c[0]+wid,c[1]+wid,c[2]+wid])
    p.addpen([c[0]+wid,c[1]-wid,c[2]+wid])
    p.addpen([c[0]-wid,c[1]-wid,c[2]+wid])
    #vertical side
    p.addpen([c[0]-wid,c[1]-wid,c[2]+wid])
    p.addpen([c[0]-wid,c[1]+wid,c[2]+wid])
    p.addpen([c[0]-wid,c[1]+wid,c[2]-wid])
    p.addpen([c[0]+wid,c[1]+wid,c[2]-wid])
    p.addpen([c[0]+wid,c[1]+wid,c[2]+wid])
    p.addpen([c[0]+wid,c[1]-wid,c[2]+wid])
    p.addpen([c[0]+wid,c[1]-wid,c[2]-wid])
    return array(p).T

#compute the cam calibration matrix
K = my_calibration((747,1000))

#side is 0.2,z= 0 points
box = cube_points([0,0,0.1],0.1)
#projection cube on the first bottom
cam1 = cam.Camera( hstack((K,dot(K,array([[0],[0],[-1]])) )) )
#points up the bottom
box_trans = homography,mormalize(dot(H,box_cam1))
#compute the second matrix from the cam1 and H
cam2 = cam.Camera(dot(H,cam1.P))
A = dot(linalg.inv(K),cam2.P[:,:3])
A = array([A[:,0],A[:1],cross(A[:,0],A[:,1])]).T
cam2.P[:,:3] = dot(K,A)

#use the second matrix projection
box_cam2 = cam2.project(homography.make_homog(box))

#test:to projection on z =0 ,to get the same point
point = array([1,1,0,1]).T
print homography.normalize(dot(dot(H,cam1.P),point))
print cam2.project(point)

im0 = array(Image.open('/home/wangkai/Pictures/book_frontal.jpg'))
im1 = array(Image.open('/home/wangkai/Pictures/book_prespective.jpg'))

#bottom cube 2D projection
figure()
imshow(im0)
plot(box_cam1[0,:],box_cam1[1,:],linewidht=3)
#use H to trans the 2D projection
figure()
imshow(im1)
plot(box_trans[0,:], box_trans[1,:],linewidth=3)
#3D cube
figure()
imshow(im1)
plot(box_cam2[0,:], box_cam2[1,:],linewidth=3)
show()
