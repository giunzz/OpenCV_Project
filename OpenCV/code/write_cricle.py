import cv2
img = cv2.imread('hinh_anh_1.jpg')
center = (150, 250)
radius = 200
color = (0, 255, 255)
thickness = 2
lineType = cv2.LINE_8
shift = 0
cv2.circle(img, center, radius, color, thickness, lineType, shift)
cv2.imshow('Display Image' , img)
cv2.waitKey(0)
