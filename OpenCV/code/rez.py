import cv2
img = cv2.imread('pic1.jpg') # đọc bức ảnh
# Resize
resized = cv2.resize(img, (200, 200))
print(img.shape) # in ra kích thước ảnh hiện tại
print(resized.shape) # in ra sau khi thay đổi