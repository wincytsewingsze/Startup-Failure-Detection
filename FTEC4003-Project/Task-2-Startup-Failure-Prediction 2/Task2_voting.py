import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import f1_score, accuracy_score

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

df = df.drop(['index', 'attr1', 'attr4'], axis=1)

# Randomly, split the data into test/training/validation sets
train, test, validate = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])

# Separate target and predictors
y_train = train['failure']
x_train = train.drop(['failure'], axis=1)
y_test = test['failure']
x_test = test.drop(['failure'], axis=1)
y_validate = validate['failure']
x_validate = validate.drop(['failure'], axis=1)

# Creating instances of the algorithms
logit_model = LogisticRegression(solver='lbfgs', max_iter=1000)
dt_model = DecisionTreeClassifier()
gb_model = GradientBoostingClassifier()

# Voting Classifier
voting = VotingClassifier(estimators=[
          ('lr', logit_model),
          ('dt', dt_model),
          ('gb', gb_model) ],
           voting='hard')

voting.fit(x_train, y_train)

# list of classifiers
list_of_classifiers = [logit_model, dt_model, gb_model, voting]
# Loop scores
for classifier in list_of_classifiers:
    classifier.fit(x_train,y_train)
    pred = classifier.predict(x_test)
    print("F1 Score:")
    print(classifier.__class__.__name__, f1_score(y_test, pred))
    print("Accuracy:")
    print(classifier.__class__.__name__, accuracy_score(y_test, pred))
    print("----------")

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

asm_test = asm_test.drop(['index', 'attr1', 'attr4'], axis=1)

prediction = pd.DataFrame(voting.predict(asm_test))
print(prediction.describe())

prediction.to_csv("submission.csv")