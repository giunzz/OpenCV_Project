import cv2
img = cv2.imread("pic1.jpg") # đọc bức ảnh
# cắt ảnh từ vị trí (50,60) phía trái trên đến (180,300) phía phải dưới.
crop = img[50:180, 60:300] 
cv2.imshow('original', img) # hình ảnh ban đầu
cv2.imshow('cropped', crop) # hình ảnh sau khi tắt
cv2.waitKey(0) # nhấn phím bất kì để out
