import cv2
img = cv2.imread('pic1.jpg') # đọc hình ảnh
# hình chuyển màu từ BGR sang GRAY
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('color', image) # hiện thị hình ảnh
cv2.waitKey(0) # nhấn phím bất kì để out

