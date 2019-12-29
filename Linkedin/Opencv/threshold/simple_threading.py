# simple threading
import numpy as np
import cv2
bw=cv2.imread('0.jpeg',0)
cv2.imshow('Original',bw)

'method1'
height,width=bw.shape[0:2]
binary=np.zeros([height,width,3],'uint8')
thresh=85
for row in range(0,height):
    for col in range(0,width):
        if bw[row][col]>thresh:
            binary[row][col]=255
cv2.imshow('binary',binary)

'method2'
ret,thresh=cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
