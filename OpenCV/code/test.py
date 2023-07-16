import cv2, time, sys
from handDetection import detect as detectHand

camera = cv2.VideoCapture(0) # tao ra object la camera cua may tinh
pTime = 0

while True:
    success, img = camera.read() # chup 1 tam hinh, success tra ve true neu chup thanh cong, nguoc lai false; img la object chua thong tin hinh anh vua chup
    if not success:
        sys.exit('Could not capture')
    img = cv2.flip(img, 1) # flip anh theo truc Oy boi vi anh ban dau bi nguoc huong
    cTime = time.time()
    fps = 1 / (cTime - pTime) # ta co fps = 1 / T, T la thoi gian chup hinh cua 2 buc anh gan nhat => fps la so luong khung anh trong 1s
    pTime = cTime
    img = detectHand(img) 
    cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2) # ve chu FPS:** len anh img
    cv2.imshow("Test", img) # hien anh ra man hinh
    k = cv2.waitKey(1)
    if k == ord('q'): # nhan phim q de thoat chuong trinh
        sys.exit('Byeeeeeeeeeeeeeeeeee') 