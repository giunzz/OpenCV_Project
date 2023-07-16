import cv2
img = cv2.imread('hinh_anh_1.jpg')
front = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
frontScale = 1
color = (255, 0, 0)
thickness = 2
lineType = cv2.LINE_AA
cv2.putText(img , 'hello' , org , front , frontScale , color, thickness, lineType, False) 
cv2.imshow('Display Image' , img)
cv2.waitKey(0)
