import cv2
from take_data import take_data
from test_data import test_data
from model import model

import numpy as np
from read_data import read_data
import os
import matplotlib.pyplot as plt
from pathlib import Path
import PySimpleGUI as sg
from PIL import Image
import io
from Take_data_menu import *
from skimage.feature import hog
import matplotlib.pyplot as plt
import joblib
if __name__=="__main__":
    #data path
    take_data_menu() #Take new data
    dir_data="Data/"
    Categories = []
    for cat in os.listdir(dir_data):
        Categories.append(cat)
#train model
    X,y=read_data(dir_data,Categories)
    svm=model(X,y)
#using model has been trained
    #svm = joblib.load('model.joblib')
#realtime
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            face=img[y:y+h,x:x+w]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            img_array = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            img_array = cv2.resize(img_array, (100, 100))
            fd, hog_image = hog(img_array, orientations=16, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)
            label = svm.predict(np.array([fd]))
            name=Categories[int(label[0])]

            cv2.putText(img, name, (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
            cv2.imshow("Recognition ", img)
        k = cv2.waitKey(100) & 0xff
        if k % 256 == 32:
            break
    cam.release()
    cv2.destroyAllWindows()




