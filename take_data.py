import os
import cv2
def take_data(name):
    cam=cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face_name=name
    count=0
    if os.path.exists("Data/"+face_name):
        pass
    else:
        os.makedirs("Data/"+face_name)
    while True:
        ret,img=cam.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count+=1
            img_path="Data/"+face_name+"/"+face_name+"."+str(count)
            while os.path.exists(img_path+".jpg"):
                img_path=img_path+".1"
            cv2.imwrite(img_path+".jpg",gray[y:y+h,x:x+w])
            cv2.imshow("Take picture ", img)
        print(count)
        k=cv2.waitKey(100) & 0xff
        if k ==27:
            break
        elif count>=50:
            break
    cam.release()
    cv2.destroyAllWindows()
