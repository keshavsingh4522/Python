import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
pos = (20, 40)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.imread("Linkedin/Opencv/tomatoes.jpg")
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab_img)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
enhance_l = clahe.apply(l)
enhance_img = cv2.merge((enhance_l, a, b))
final_img = cv2.cvtColor(enhance_img, cv2.COLOR_LAB2BGR)
cv2.putText(img, 'Before', pos, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(final_img, 'After', pos, font, fontScale, color, thickness, cv2.LINE_AA)
compare_img = cv2.hconcat([img, final_img])
cv2.imshow('Enhanced Contrast', compare_img)
cv2.waitKey(0)