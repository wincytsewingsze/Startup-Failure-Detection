from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

class bayes():
    def __init__(self):
        self.model = SVC(C=1.0,kernel='rbf')

    def trainModel(self,X,y):
        gnb = GaussianNB()
        gnb.fit(X,y)
        mnb = MultinomialNB()
        mnb.fit(X,y)

    def predict(self,input):
        return self.model.predict(input)