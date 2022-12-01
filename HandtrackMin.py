import cv2
from cv2 import FONT_HERSHEY_COMPLEX
from matplotlib.cbook import pts_to_midstep
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands = mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0


while True:
    sucesss , img = cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results=hands.process(imgRGB)

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)), (0,50),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2 )
    cv2.imshow("cam 1", img)
    cv2.waitKey(1)

