# import cv2
# img = cv2.imread('pic1.jpg') # đọc hình ảnh
# cv2.imshow('Show testing', img) # hiển thị hình ảnh
# k = cv2.waitKey(0) #sẽ hiển thị cửa sổ sau t ms
# # t = 0 hiển thị đến khi người dùng nhấn phím bất kì
# if k == ord('s'):
#         # nếu nhấn phím s sẽ lưu hình ảnh
#         cv2.imwrite('pic2.png', img)

# import cv2
# img = cv2.imread('pic1.jpg') # đọc hình ảnh
# (h,w,d) = img.shape # lấy kích thước
# print("chieu cao = ",h)
# print("chieu rong = ",w)
# print("chieu sau = ",d)

import cv2
img = cv2.imread('pic1.jpg')
(B,G,R) = img[20,50] 
print("R = ",R)
print("G = ",G)
print("B = ",B)

