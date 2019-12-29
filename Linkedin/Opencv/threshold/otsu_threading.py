# otsu threading ---> https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-3-otsu-thresholding/
'We use the Traditional cv2.threshold function and use cv2.THRESH_OTSU as an extra flag.'
import cv2
img=cv2.imread('sudoku.png',0)
cv2.imshow('Original',img)

# simaple threading ---> problem ---> uneven binding
ret,frame=cv2.threshold(img,85,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',frame)

# otsu
ret,frame=cv2.threshold(img,85,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu',frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
