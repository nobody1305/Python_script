import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
# import copy
# import seaborn
# import tensorflow

# Load data
cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv('machine_learning/magic04.data', names=cols)
df["class"] = (df["class"] == "g").astype(int)

# Create subplots
fig, axs = plt.subplots(2, 5, figsize=(20, 15))

# Plot histograms
for i, label in enumerate(cols[:-1]):
    row = i // 5  # Calculate the row index
    col = i % 5   # Calculate the column index
    ax = axs[row, col]  # Access the correct subplot
    ax.hist(df[df["class"]==1][label], color='blue', label='gamma', alpha=0.7, density=True)
    ax.hist(df[df["class"]==0][label], color='red', label='hadron', alpha=0.7, density=True)
    ax.set_title(label)
    ax.set_ylabel("Probability")
    ax.set_xlabel(label)
    ax.legend()

plt.tight_layout()
plt.show()

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])
def scale_dataset(dataframe, oversample=False):
  X = dataframe[dataframe.columns[:-1]].values
  y = dataframe[dataframe.columns[-1]].values

  scaler = StandardScaler()
  X = scaler.fit_transform(X)

  if oversample:
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X, y)

  data = np.hstack((X, np.reshape(y, (-1, 1))))

  return data, X, y
train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
test, X_test, y_test = scale_dataset(test, oversample=False)

# K-nearest
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
KNeighborsClassifier()
y_pred = knn_model.predict(X_test)
print(classification_report(y_test, y_pred))

# naive bayes
nb_model = GaussianNB()
nb_model = nb_model.fit(X_train, y_train)
y_pred = nb_model.predict(X_test)
print(classification_report(y_test, y_pred))

# logistic regression
lg_model = LogisticRegression()
lg_model = lg_model.fit(X_train, y_train)
y_pred = lg_model.predict(X_test)
print(classification_report(y_test, y_pred))

# svm method
svm_model = SVC()
svm_model = svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)
print(classification_report(y_test, y_pred))
