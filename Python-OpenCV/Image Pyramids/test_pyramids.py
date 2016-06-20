import cv2
p1 = cv2.imread('../IMAGES/p1.jpg')
A = p1
G = A.copy()
gpA = [G]
for i in xrange(5):
    G = cv2.pyrDown(G)
    print G.size
    gpA.append(G)

cv2.imshow('0',gpA[0])
cv2.imshow('1',gpA[1])
cv2.imshow('2',gpA[2])
cv2.imshow('3',gpA[3])
cv2.imshow('4',gpA[4])
cv2.imshow('5',gpA[5])
cv2.waitKey()
cv2.destroyAllWindows()
