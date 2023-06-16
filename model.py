from sklearn.svm import SVC
import cv2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
import joblib
def model(features,labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.4, random_state=42)
    param_grid = {'C': [1, 10, 100, 1000], 'gamma': [0.1, 0.01, 0.001, 0.0001]}
    svm = SVC(kernel='poly')
    grid = GridSearchCV(svm, param_grid, cv=5)
    grid.fit(X_train, y_train)
    y_pred=grid.predict(X_test)
    print(accuracy_score(y_test,y_pred))
    joblib.dump(grid, 'model4.joblib')
    return grid