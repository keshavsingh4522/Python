import numpy as np
import cv2
template=cv2.imread('template.jpg')
frame=cv2.imread('players.jpg')
cv2.imshow('Template',template)
cv2.imshow('Frame',frame)

result=cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)
cv2.imshow('result1',result)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
cv2.circle(result,max_loc,15,255,-1)
cv2.imshow('result2',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
