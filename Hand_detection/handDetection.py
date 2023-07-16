import cv2, numpy, sys
import mediapipe as mp

mpHands = mp.solutions.hands 
hands = mpHands.Hands(static_image_mode = False, 
                    max_num_hands = 2,
                    min_detection_confidence = 0.5, 
                    min_tracking_confidence = 0.5 ) # hands : hàm opject tạo ra detect(phát hiện) bàn tay
mpDraw = mp.solutions.drawing_utils # object : vẽ các đường liên kết 
# print(type(mpHands)) 
def detect(img: numpy.ndarray) -> numpy.ndarray:
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # imgRGB: hình chuyển màu từ BGR sang RGB 
    listHands = hands.process(imgRGB).multi_hand_landmarks # trả về các điểm trên bàn tay 
    if listHands:
        for currentHand in listHands:
            mpDraw.draw_landmarks(img, currentHand, mpHands.HAND_CONNECTIONS) # nối các điểm được nhận diện
            for ind, coors in enumerate(currentHand.landmark): # duyệt các điểm được xác định trên bàn tay
                h, w, c = img.shape # lấy độ dài các cạnh của hình
                x, y = int(coors.x * w), int(coors.y * h) # lấy tỉ lệ nhân với độ dài thực tế
                cv2.circle(img, (x, y), 3, (0, 255, 0) , cv2.FILLED) # vẽ hình tròn bán kính 3 tại tọa độ x,y
    return img