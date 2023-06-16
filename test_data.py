import os
import cv2
import numpy as np
from take_test_data import *
def test_data(img):
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    for (x, y, w, h) in faces:
        return img[y:y+h,x:x+w]
# img=test_data(cv2.imread("dong2.jpg"))
# cv2.imwrite("test7.jpg",img)
