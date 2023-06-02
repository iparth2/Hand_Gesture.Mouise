import cv2

import mediapipe as mop
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    cv2.imshow("virtual mouse" , frame)
    cv2.waitKey(1)


