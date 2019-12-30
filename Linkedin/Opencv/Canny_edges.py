# Canny edge detection
import cv2
import numpy

img=cv2.imread('tomatoes.jpg')
HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ret,thresh=cv2.threshold(HSV[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh',thresh)

edges=cv2.Canny(img,100,70)
cv2.imshow('Edges',edges)

final=cv2.bitwise_or(thresh,edges)
cv2.imshow('Final',final)

cv2.waitKey(0)
cv2.destroyAllWindows()
