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
import tensorflow as tf
import os
import PyPDF2
# import copy
# import seaborn

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

# neural network
def plot_history(history, filename=None, title=None):
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
  ax1.plot(history.history['loss'], label='loss')
  ax1.plot(history.history['val_loss'], label='val_loss')
  ax1.set_xlabel('Epoch')
  ax1.set_ylabel('Binary crossentropy')
  ax1.grid(True)

  ax2.plot(history.history['accuracy'], label='accuracy')
  ax2.plot(history.history['val_accuracy'], label='val_accuracy')
  ax2.set_xlabel('Epoch')
  ax2.set_ylabel('Accuracy')
  ax2.grid(True)

  if title:  # Add title if provided
    plt.suptitle(title)

  if filename:
    plt.savefig(filename)
    plt.close()
  else:
    plt.show()

def train_model(X_train, y_train, num_nodes, dropout_prob, lr, batch_size, epochs):
  nn_model = tf.keras.Sequential([
      tf.keras.layers.Dense(num_nodes, activation='relu', input_shape=(10,)),
      tf.keras.layers.Dropout(dropout_prob),
      tf.keras.layers.Dense(num_nodes, activation='relu'),
      tf.keras.layers.Dropout(dropout_prob),
      tf.keras.layers.Dense(1, activation='sigmoid')
  ])

  nn_model.compile(optimizer=tf.keras.optimizers.Adam(lr), loss='binary_crossentropy',
                  metrics=['accuracy'])
  history = nn_model.fit(
    X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, verbose=0
  )

  return nn_model, history

def merge_pdfs(input_filenames, output_filename, title=None):  # Added title parameter
    merger = PyPDF2.PdfMerger()
    
    for filename in input_filenames:
        merger.append(filename)
    
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)
    
    if title:  # Add title to the merged PDF file
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_reader = PyPDF2.PdfFileReader(output_filename)

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            page.mergePage(PyPDF2.PdfFileReader(title).getPage(0))
            pdf_writer.addPage(page)

        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

pdf_filenames = []
counter = 1
directory = "machine_learning/training_plot"

least_val_loss = float('inf')
least_loss_model = None
epochs=100
for num_nodes in [16, 32]:
  for dropout_prob in[0]:
    for lr in [0.01]:
      for batch_size in [32]:
        print(f"{num_nodes} nodes, dropout {dropout_prob}, lr {lr}, batch size {batch_size}")
        model, history = train_model(X_train, y_train, num_nodes, dropout_prob, lr, batch_size, epochs)
        filename = os.path.join(directory, f"filename{counter}.pdf")
        plot_history(history, filename, title=f"{num_nodes} nodes, dropout {dropout_prob}, lr {lr}, batch size {batch_size}")
        pdf_filenames.append(filename)
        val_loss = model.evaluate(X_valid, y_valid)[0]
        if val_loss < least_val_loss:
          least_val_loss = val_loss
          least_loss_model = model
        counter += 1
        merge_pdfs(pdf_filenames, os.path.join(directory, 'picture.pdf'))

for filename in pdf_filenames:
    os.remove(filename)  
    
y_pred = least_loss_model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int).reshape(-1,)
print(classification_report(y_test, y_pred))
