import HandTrackingModule as htm
import time
import cv2
wCam , hCam = 720 , 1280
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime= 0

detector = htm.handDetector(maxHands=1)

while True:
    sucess, img=cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

   





    cTime =time.time()
    fps = 1 / (cTime - pTime)
    pTime= cTime
    cv2.putText(img, str(int(fps)),(20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3 )
    
    
    
    
    
    
    cv2.imshow("Ishan", img)
    cv2.waitKey(1)