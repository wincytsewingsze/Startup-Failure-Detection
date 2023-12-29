from sklearn.svm import SVC
import matplotlib.pyplot as plt

class svm():
    def __init__(self):
        self.model = SVC(C=1.0,kernel='rbf')

    def trainModel(self,X,y):
        self.model.fit(X,y)

    def predict(self,input):
        return self.model.predict(input)