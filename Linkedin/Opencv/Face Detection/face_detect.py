# Face detection
import numpy as np
import cv2
img=cv2.imread('faces.jpeg')

rimg=cv2.resize(img,(img.shape[0]//3,img.shape[1]//5),interpolation=cv2.INTER_AREA)
gray=cv2.cvtColor(rimg,cv2.COLOR_BGR2GRAY)

path='haarcascade_frontalface_default.xml'

face_cascade=cv2.CascadeClassifier(path)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.25,minSize=(40,40))

for (x,y,w,h) in faces:
    cv2.rectangle(rimg,(x,y),(x+w,y+h),(0,255,0),1)
cv2.imshow('Img',rimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
