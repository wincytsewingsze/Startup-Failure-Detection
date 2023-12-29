import pandas as pd

train_fn = '/Users/wincytse/Downloads/FTEC4003/FTEC4003-Project/Task-1-Debt-Default-Prediction/train.csv'
test_fn = '/Users/wincytse/Downloads/FTEC4003/FTEC4003-Project/Task-1-Debt-Default-Prediction/assignment-test.csv'
results_path = '/Users/wincytse/Downloads/FTEC4003/FTEC4003-Project/Task-1-Debt-Default-Prediction/'
feature_cols = ['EA1','EA2','EA3','EA4','EA5','EA6']

class dataHandling():
    def read_train():
        df = pd.read_csv(train_fn)
        attributes = df[feature_cols].to_numpy()
        actualClass = df['Class'].to_numpy()
        return attributes,actualClass

    def read_test():
        df = pd.read_csv(test_fn)
        attributes_test = df[feature_cols].to_numpy()
        return attributes_test,df

    def results_to_csv(results,test_df,name):
        results_df = test_df.copy()
        results_df['Class']=results
        results_df = results_df.drop(columns=feature_cols)
        results_df.to_csv(results_path+name)