import cv2
#There are two kinds of Image Pyramids. 
#1) Gaussian Pyramid and 2) Laplacian Pyramids
#Higher level (Low resolution) in a Gaussian Pyramid 
#is formed by removing consecutive rows and columns in Lower level (higher resolution) image. 
#By doing so, a M x N image becomes M/2 x N/2 image. 
img = cv2.imread('../IMAGES/sex.jpg')
lower_reso = cv2.pyrDown(img)
cv2.imshow('img',img)
cv2.imshow('lower',lower_reso)
cv2.waitKey()
cv2.destroyAllWindows()
#you can go down the image pyramid with cv2.pyrUp() function.
higher_reso2 = cv2.pyrUp(lower_reso)
cv2.imshow('higher',higher_reso2)
cv2.waitKey()
