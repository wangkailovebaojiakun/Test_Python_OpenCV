import homography
import camera
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

