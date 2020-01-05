# eye detection
import numpy as np
import cv2
img=cv2.imread('faces.jpeg')

rimg=cv2.resize(img,(img.shape[0]//3,img.shape[1]//5),interpolation=cv2.INTER_AREA)
gray=cv2.cvtColor(rimg,cv2.COLOR_BGR2GRAY)

path='haarcascade_eye.xml'

eye_cascade=cv2.CascadeClassifier(path)
eyes=eye_cascade.detectMultiScale(gray,scaleFactor=1.04,minNeighbors=20,minSize=(10,10))

for (x,y,w,h) in eyes:
    cx=(x+x+w)//2
    cy=(y+y+h)//2
    cv2.circle(rimg,(cx,cy),w//2,(255,0,0),2)
cv2.imshow('Img',rimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
