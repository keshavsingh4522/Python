# adaptive threading --->  https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-2-adaptive-thresholding
import cv2
img=cv2.imread('sudoku.png',0)
cv2.imshow('Original',img)

# simaple threading ---> problem ---> uneven binding
ret,frame=cv2.threshold(img,85,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',frame)

# adaptive threading ---> remove uneven binding
adap_thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('adaptive thresh',adap_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
