# import packages
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import preprocessing

data = pd.read_csv("train.csv")
data.drop(['attr10'], axis = 1, inplace = True)
data_test = pd.read_csv("assignment-test.csv")
data_test.drop(['attr10'], axis = 1, inplace = True)


df = pd.DataFrame(data)

df.loc[df["attr1"]=="A", "attr1"] = 0
df.loc[df["attr1"]=="B", "attr1"] = 1
df.loc[df["attr1"]=="C", "attr1"] = 2
df.loc[df["attr1"]=="D", "attr1"] = 3
df.loc[df["attr1"]=="E", "attr1"] = 4
df.loc[df["attr1"]=="F", "attr1"] = 5
df.loc[df["attr1"]=="G", "attr1"] = 6

df.loc[df["attr4"]=="A", "attr4"] = 0
df.loc[df["attr4"]=="B", "attr4"] = 1
df.loc[df["attr4"]=="C", "attr4"] = 2
df.loc[df["attr4"]=="D", "attr4"] = 3
df.loc[df["attr4"]=="E", "attr4"] = 4
df.loc[df["attr4"]=="F", "attr4"] = 5
df.loc[df["attr4"]=="G", "attr4"] = 6
df.loc[df["attr4"]=="H", "attr4"] = 7
df.loc[df["attr4"]=="I", "attr4"] = 8
df.loc[df["attr4"]=="J", "attr4"] = 9
df.loc[df["attr4"]=="K", "attr4"] = 10
df.loc[df["attr4"]=="L", "attr4"] = 11

df.head()

columns_included = ['attr1', 'attr2', 'attr3', 'attr4', 'attr5', 'attr6', 'attr7', 'attr8', 'attr9', 'attr11', 'attr12', 'attr13', 'attr14', 'attr15', 'attr16', 'attr17', 'attr18','attr19','attr20']
df_dataArray = df[columns_included].copy()  
dataArray = preprocessing.scale(df_dataArray.values)
target = df["failure"].tolist()

target_names = ["0", "1"]

dataset = {
   "data": dataArray,
   "target": target,
   "feature_names": columns_included,
   "target_names": target_names
}

df_test = pd.DataFrame(data_test)

df_test.loc[df_test["attr1"]=="A", "attr1"] = 0
df_test.loc[df_test["attr1"]=="B", "attr1"] = 1
df_test.loc[df_test["attr1"]=="C", "attr1"] = 2
df_test.loc[df_test["attr1"]=="D", "attr1"] = 3
df_test.loc[df_test["attr1"]=="E", "attr1"] = 4
df_test.loc[df_test["attr1"]=="F", "attr1"] = 5
df_test.loc[df_test["attr1"]=="G", "attr1"] = 6

df_test.loc[df_test["attr4"]=="A", "attr4"] = 0
df_test.loc[df_test["attr4"]=="B", "attr4"] = 1
df_test.loc[df_test["attr4"]=="C", "attr4"] = 2
df_test.loc[df_test["attr4"]=="D", "attr4"] = 3
df_test.loc[df_test["attr4"]=="E", "attr4"] = 4
df_test.loc[df_test["attr4"]=="F", "attr4"] = 5
df_test.loc[df_test["attr4"]=="G", "attr4"] = 6
df_test.loc[df_test["attr4"]=="H", "attr4"] = 7
df_test.loc[df_test["attr4"]=="I", "attr4"] = 8
df_test.loc[df_test["attr4"]=="J", "attr4"] = 9
df_test.loc[df_test["attr4"]=="K", "attr4"] = 10
df_test.loc[df_test["attr4"]=="L", "attr4"] = 11

df_test.head()

rf = RandomForestClassifier()
rf.fit(dataset['data'], dataset['target'])
data_test_preprocessing = preprocessing.scale(df_test[columns_included].values)
predictedTestResult = rf.predict(data_test_preprocessing)

df_output = df_test[["index"]]
df_output.insert(1, "failure", predictedTestResult, True)
df_output.to_csv("DecisionTree.csv", index=False)


