# Area, Perimeter, Center, Curvature
import numpy as np
import cv2

img=cv2.imread('detect_blob.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
_,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img2=img.copy()
color=(123,255,61)
index=-1
tk=2
frame=np.zeros([img.shape[0],img.shape[1],3],'uint8')
i=1
for c in contours:
    cv2.drawContours(frame,[c],index,color,tk)
    area=cv2.contourArea(c)
    arclength=cv2.arcLength(c,True)
    print('{} Area: {},  perimeter: {}'.format(i,area,arclength))
    i+=1
    m=cv2.moments(c)
    cx=int(m['m10']/m['m00'])
    cy=int(m['m01']/m['m00'])
    cv2.circle(frame,(cx,cy),1,(0,0,255),-1)
    cv2.imshow('Original',frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
