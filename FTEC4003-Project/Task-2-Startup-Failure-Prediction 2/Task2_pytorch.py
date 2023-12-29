import torch
import numpy as np
import pandas as pd
from torch import nn
from torch.nn import functional as F
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from torch.utils.data import Dataset, DataLoader

def correlation(dataset, threshold):
    col_corr = set()  
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: colname = corr_matrix.columns[i]                  
            col_corr.add(colname)
    return col_corr

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

df = df.drop(['index', 'attr1', 'attr4', 'attr7', 'attr16', 'attr20'], axis=1)

y = df['failure']
x = df.drop(['failure'], axis=1)

sc = StandardScaler()
x = sc.fit_transform(x)

class dataset(Dataset):
  def __init__(self,x,y):
    self.x = torch.tensor(x,dtype=torch.float32)
    self.y = torch.tensor(y,dtype=torch.float32)
    self.length = self.x.shape[0]
 
  def __getitem__(self,idx):
    return self.x[idx],self.y[idx]
  def __len__(self):
    return self.length
trainset = dataset(x,y)

#DataLoader
trainloader = DataLoader(trainset,batch_size=64,shuffle=False)

#defining the network
class Net(nn.Module):
  def __init__(self,input_shape):
    super(Net,self).__init__()
    self.fc1 = nn.Linear(input_shape,32)
    self.fc2 = nn.Linear(32,64)
    self.fc3 = nn.Linear(64,64)
    self.fc4 = nn.Linear(64,1)
  def forward(self,x):
    x = torch.relu(self.fc1(x))
    x = torch.relu(self.fc2(x))
    x = torch.relu(self.fc3(x))
    x = torch.sigmoid(self.fc4(x))
    return x

#hyper parameters
learning_rate = 0.01
epochs = 500
# Model , Optimizer, Loss
model = Net(input_shape=x.shape[1])
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
loss_fn = nn.BCELoss()

#forward loop
losses = []
accur = []
f1s = []
for i in range(epochs):
  for j,(x_train,y_train) in enumerate(trainloader):
    
    #calculate output
    output = model(x_train)
 
    #calculate loss
    loss = loss_fn(output,y_train.reshape(-1,1))
 
    #accuracy
    predicted = model(torch.tensor(x,dtype=torch.float32))
    acc = (predicted.reshape(-1).detach().numpy().round() == y).mean()
    f1 = f1_score(predicted.reshape(-1).detach().numpy().round(),y) 

    #backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

  if i%50 == 0:
    losses.append(loss)
    accur.append(acc)
    f1s.append(f1)
    print("epoch {}\tloss : {}\t accuracy : {} f1-score : {}".format(i,loss,acc,f1))

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

asm_test = asm_test.drop(['index', 'attr1', 'attr4', 'attr7', 'attr16', 'attr20'], axis=1)
asm_test = sc.fit_transform(asm_test)
submit = model(torch.tensor(asm_test,dtype=torch.float32))
prediction = pd.DataFrame(submit.reshape(-1).detach().numpy().round()).astype("int32")
print(prediction.describe())

prediction.to_csv("submission.csv")