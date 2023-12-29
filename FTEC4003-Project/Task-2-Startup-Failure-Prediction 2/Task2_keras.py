import numpy as np
import pandas as pd
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split

# Loading Dataset
data = pd.read_csv("train.csv")
X = data[["attr1", "attr2", "attr3", "attr4", "attr5", "attr6", "attr7", "attr8", "attr9", "attr10", "attr11", "attr12", "attr13", "attr14", "attr15", "attr16", "attr17", "attr18", "attr19", "attr20"]]
y = data["failure"]

#identify all categorical variables
cat_columns = X.select_dtypes(['object']).columns
#convert all categorical variables to numeric
X[cat_columns] = X[cat_columns].apply(lambda x: pd.factorize(x)[0])

counts = np.bincount(y[:])
print(
    "Number of positive samples in training data: {} ({:.2f}% of total)".format(
        counts[1], 100 * float(counts[1]) / len(y)
    )
)

weight_for_0 = 1.0 / counts[0]
weight_for_1 = 1.0 / counts[1]

# X = normalize(X)
mean = np.mean(X, axis=0)
X -= mean
std = np.std(X, axis=0)
X /= std

model = keras.Sequential(
    [
        keras.layers.Dense(256, activation="relu", input_shape=(20,)),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(256, activation="relu"),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(64, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ]
)
model.summary()

metrics = [
    keras.metrics.FalseNegatives(name="fn"),
    keras.metrics.FalsePositives(name="fp"),
    keras.metrics.TrueNegatives(name="tn"),
    keras.metrics.TruePositives(name="tp"),
    keras.metrics.Precision(name="precision"),
    keras.metrics.Recall(name="recall"),
]

model.compile(
    optimizer=keras.optimizers.Adam(1e-2), loss="binary_crossentropy", metrics=metrics
)

callbacks = [keras.callbacks.ModelCheckpoint("fraud_model_at_epoch_{epoch}.h5")]
class_weight = {0: weight_for_0, 1: weight_for_1}

model.fit(
    X,
    y,
    batch_size=1024,
    epochs=300,
    verbose=1,
    validation_split=0.2,
    class_weight=class_weight,
)

test = pd.read_csv("assignment-test.csv")
test = test[["attr1", "attr2", "attr3", "attr4", "attr5", "attr6", "attr7", "attr8", "attr9", "attr10", "attr11", "attr12", "attr13", "attr14", "attr15", "attr16", "attr17", "attr18", "attr19", "attr20"]]
#identify all categorical variables
cat_columns = test.select_dtypes(['object']).columns
#convert all categorical variables to numeric
test[cat_columns] = test[cat_columns].apply(lambda x: pd.factorize(x)[0])

mean = np.mean(test, axis=0)
test -= mean
std = np.std(test, axis=0)
test /= std

print("Generate a prediction")
prediction = (model.predict(test) > 0.5).astype("int32")
print("prediction shape:", prediction.shape)

submit = pd.DataFrame(prediction, columns=["Class"], dtype=int)
print(submit.describe())
plt.scatter(submit["Class"], submit.index)
plt.ylabel('value')
plt.xlabel('no')
plt.show()
submit.to_csv("submission.csv")