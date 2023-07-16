import cv2
img = cv2.imread('hinh_anh_1.jpg')
pt1 = (50, 50)
pt2 = (400, 400)
color = (0, 255, 0)
thickness = 2
lineType = cv2.LINE_8
shilf = 0
cv2.line(img, pt1, pt2, color, thickness, lineType, shilf)
cv2.imshow('Display Image' , img)
cv2.waitKey(0)
