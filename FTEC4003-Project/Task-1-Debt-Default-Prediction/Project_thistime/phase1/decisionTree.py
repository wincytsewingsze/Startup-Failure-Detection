from sklearn import tree
import graphviz


feature_cols = ['EA1','EA2','EA3','EA4','EA5','EA6']

class decisionTree():
    def __init__(self):
        self.model = tree.DecisionTreeClassifier(criterion='gini',splitter='best')

    def trainModel(self,X,y):
        self.model.fit(X,y)

    def predict(self,input):
        return self.model.predict(input)

    def plot_tree(self):
        data=tree.export_graphviz(self.model,feature_names=feature_cols,filled=True)
        graph = graphviz.Source(data)
        return graph
    