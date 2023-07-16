import cv2, time, sys
from handDetection import detect as detectHand

camera = cv2.VideoCapture(0) # object : camera cua may tinh
pTime = 0

while True:
    success, img = camera.read() # chup 1 tam hinh
    if not success:
        sys.exit('Could not capture') # chưa có thông tin hình ảnh vừa chụp
    img = cv2.flip(img, 1) # flip ảnh theo trục Oy ( ảnh ban đầu ngược hướng)
    cTime = time.time()
    fps = 1 / (cTime - pTime) # thời gian camera capture 1 bức ảnh
    pTime = cTime
    img = detectHand(img) 
    h, w, c = img.shape # lấy kích thước ảnh
    cv2.putText(img, f'FPS:{int(fps)}', (int(0.03 * w), int(0.14583 * h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2) 
    # vẽ chữ FPS:** lên ảnh img
    cv2.putText(img, f'Zun moi', (int(0.03 * w), int(0.9 * h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (147, 20, 255), 2) 
    # vẽ chữ Zun moi len ảnh img
    cv2.imshow("Test", img) # hiện ảnh ra màn hình
    k = cv2.waitKey(1)
    if k == ord('q'): # nhấn phím q để thoát chương trình
        sys.exit('Byeeeeeeeeeeeeeeeeee')