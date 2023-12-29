# import packages
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.decomposition import PCA

# Loading Dataset
df = pd.read_csv("train.csv")

# Some basic stats on the target variable
print('# startup failed = {}'.format(len(df[df['failure'] == 1])))

print('# startup succeed = {}'.format(len(df[df['failure'] == 0])))

print('% startup failed = {}%'.format(round(float(len(df[df['failure'] == 1])) / len(df) * 100), 3))

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

df = df.drop(['index', 'attr1', 'attr4', 'attr10'], axis=1)

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

clf = svm.SVC(kernel='linear')
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

pd.set_option('display.max_columns', None)
asm_test.head()

asm_test = asm_test.drop(['index', 'attr1', 'attr4', 'attr10'], axis=1)

prediction = pd.DataFrame(clf_model.predict(asm_test))
print(prediction)

prediction.to_csv("submission.csv")