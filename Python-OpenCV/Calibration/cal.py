import cv2
import numpy as np
import glob
#termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.01)
#cv2.TERM_CRITERIA_EPS 
#prepar object points,like(0,0,0),(1,0,0),(2,0,0).....(6,5,0)
objp = np.zeros((6*7,3),np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
#Arrays to store object points and image points from all the images
objpoints = []#3d point in read world space(in Zhang's method Z is 0)
imgpoints = []#2d points in image plane
images = glob.glob('*.jpg')
for fname in images:
    img = cv2.imread(fname)
    print bool(img.data),'name'+fname
    #cv2.imshow('test',img)
    #cv2.waitKey(30)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    #Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray,(7,6),None)
    #If found,add object points,image points(after refining them)
    if ret == True:
        objpoints.append(objp)

        print bool(img.data)
	corners2 =cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        print corners2
	imgpoints.append(corners)
	#draw and display the corners
	cv2.drawChessboardCorners(img,(7,6),corners,ret)
        #print bool(img.data)
        cv2.imshow('img',img)
	#cv2.waitKey(500)
#Calibration

if len(objpoints)==len(imgpoints):
    print 'length is same'
    print objpoints[0].dtype,imgpoints[0].dtype
else:
    print len(objpoints),len(imgpoints)
    
impa = np.array(imgpoints,'float32')
obpa = np.array(objpoints,'float32')

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obpa,impa, gray.shape[::-1],None,None)
#undistortion
img = cv2.imread('left12.jpg')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
#1.using cv2.undistort
dst = cv2.undistort(img,mtx,dist,None,newcameramtx)
cv2.imshow('undistort',dst)
cv2.imshow('input',img)
#2.using remapping
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow('remapping',dst)
#crop the image
x,y,w,h = roi
dst = dst[y:y+h,x:x+w]
cv2.imshow('remapping crop',dst)
cv2.imwrite('calibresult.png',dst)
cv2.waitKey()
cv2.destroyAllWindows()    

