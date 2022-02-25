import cv2
import numpy as np
import dlib
import time

url = 'https://192.168.0.102:8080/video'
cap = cv2.VideoCapture(url)
cap.set(3, 112)
cap.set(4, 80)
face_detector = dlib.get_frontal_face_detector()
while(True):
    camera, frame = cap.read()
    if frame is not None:
        gray = cv2.cvtColor(src = frame, code = cv2.COLOR_BGR2GRAY)
        a = time.time()
        cv2.resize(gray, (112, 80))
        faces = face_detector(gray)
        b = time.time() - a;
        print(f"time to process : {b}")
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom() 
            cv2.rectangle(img = gray, pt1 = (x1, y1), pt2 = (x2, y2), color = (0, 255, 0), thickness = 4)
        cv2.imshow("Frame", gray)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()

# vô hiệu quá khối lệnh prin ở dòng thứ 32
##print("test github!!")