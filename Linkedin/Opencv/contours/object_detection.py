# objeect detection
import cv2
img=cv2.imread('detect_blob.png')
cv2.imshow('Original colored',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Gray',gray)


thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('Thresh',thresh)

_,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2=img.copy()
index=-1
thickness=5
color=(255,0,255)
cv2.drawContours(img2,contours,index,color,thickness)
cv2.imshow('Contours',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
