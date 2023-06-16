import os
import cv2
def take_test_data():
    cam=cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    while True:
        ret, img = cam.read()
        k = cv2.waitKey(10)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow("Take picture ", img)
            k = cv2.waitKey(100) & 0xff
            if k % 256 == 32:
                return img[y:y+h,x:x+w]
