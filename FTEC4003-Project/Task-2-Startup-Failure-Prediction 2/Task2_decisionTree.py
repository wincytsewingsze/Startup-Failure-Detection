# import packages
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

# Loading Dataset
df = pd.read_csv("train.csv")

# Prepend string prior to encoding
df['attr1'] = '1_' + df['attr1'].astype(str)
df['attr4'] = '4_' + df['attr4'].astype(str)

# Create 'attr1' dummies and join
one_hot_attr1 = pd.get_dummies(df['attr1'])
df = df.join(one_hot_attr1)

# Create 'attr4' dummies and join
one_hot_attr4 = pd.get_dummies(df['attr4'])
df = df.join(one_hot_attr4)

pd.set_option('display.max_columns', None)

df = df.drop(['index', 'attr1', 'attr4', 'attr17'], axis=1)

# Randomly, split the data into test/training/validation sets
train, test, validate = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
print(train.shape, test.shape, validate.shape)

# Separate target and predictors
y_train = train['failure']
x_train = train.drop(['failure'], axis=1)
y_test = test['failure']
x_test = test.drop(['failure'], axis=1)
y_validate = validate['failure']
x_validate = validate.drop(['failure'], axis=1)

print(y_test.mean())
print(y_train.mean())

# Variable importance
rf = RandomForestClassifier()
rf.fit(x_train, y_train)
print ("Features sorted by their score:")
print (sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), x_train), reverse=True))

clf = tree.DecisionTreeClassifier()
clf_model = clf.fit(x_train, y_train)

asm_test = pd.read_csv('assignment-test.csv')

# Prepend string prior to encoding
asm_test['attr1'] = '1_' + asm_test['attr1'].astype(str)
asm_test['attr4'] = '4_' + asm_test['attr4'].astype(str)

# Create 'attr1' dummies and join
one_hot_attr1 = pd.get_dummies(asm_test['attr1'])
asm_test = asm_test.join(one_hot_attr1)

# Create 'attr4' dummies and join
one_hot_attr4 = pd.get_dummies(asm_test['attr4'])
asm_test = asm_test.join(one_hot_attr4)

asm_test = asm_test.drop(['index', 'attr1', 'attr4', 'attr17'], axis=1)

prediction = pd.DataFrame(clf_model.predict(asm_test))
print(prediction.describe())

prediction.to_csv("submission.csv")


