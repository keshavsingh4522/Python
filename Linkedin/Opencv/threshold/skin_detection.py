# skin detection ---> 
import cv2
import numpy as np
img=cv2.imread('faces.jpeg',1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)

h=hsv[:,:,0]
s=hsv[:,:,1]
v=hsv[:,:,2]
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow('HSV_SPLIT',hsv_split)

# detect
ret,min_set=cv2.threshold(s,40,255,cv2.THRESH_BINARY)
ret,max_set=cv2.threshold(h,15,255,cv2.THRESH_BINARY)
final=cv2.bitwise_and(min_set,max_set)
cv2.imshow('Final',final)

cv2.waitKey(0)
cv2.destroyAllWindows()
