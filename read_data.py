import os
import numpy as np
import cv2
from skimage.feature import hog
def read_data(dir,Categories):
    X = []
    y = []
    for cat in Categories:
        path = os.path.join(dir, cat)
        class_num = Categories.index(cat)
        for img in os.listdir(path):
            img = cv2.imread(os.path.join(path, img), cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (100, 100))
            fd, hog_image = hog(img, orientations=16, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                                visualize=True)
            X.append(fd)
            y.append(class_num)

    X=np.array(X)
    y=np.array(y)
    return X,y