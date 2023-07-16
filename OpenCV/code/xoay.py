import cv2
img = cv2.imread('pic1.jpg') # đọc hình ảnh
(h,w,d) = img.shape # lấy kích thước
tam = (w//2,h//2) # tâm quay của hình
M = cv2.getRotationMatrix2D(tam, 45, 1.0) # Tọa độ của tâm xoay
rotated = cv2.cv2.warpAffine(img,M,(w,h))
cv2.imshow('anh_sau_khi_xoay',rotated)
cv2.waitKey(0)