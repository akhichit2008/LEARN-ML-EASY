# -*- coding: utf-8 -*-
"""OlivettiFaces-Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1beGd48ZkltFsHpNMPs2SQtWXi-m9oLhQ

# Olivetti Faces Dataset Problem using *MLPClassifier*

> We use a Multi-Layer Perceptron Classifier on the AT & T Olivetti Faces Dataset to classify human facial expressions under any one of the 40 different categories.This is however a simplified implementation for beginners. Many improvements can be made to this such as using PCA (Principal Component Analysis) , tensorflow CNN (Convolutional Neural Network), etc.
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets , metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

ds = sklearn.datasets.fetch_olivetti_faces()
ds.images.shape , ds.target.shape
IMG_SIZE = 64

# Plot training samples
_,axes = plt.subplots(nrows=1,ncols=4,figsize=(10,4))
for axis,image,label in zip(axes,ds.images[40:],ds.target[40:]):
  axis.set_axis_off()
  axis.imshow(image,cmap="gray")
  axis.set_title("Training : {}".format(label))
n_samples = len(ds.images)
data = ds.images.reshape(n_samples,-1)

# Creating MLP Model
model = MLPClassifier(hidden_layer_sizes=(200))
X_train , X_test , Y_train , Y_test = train_test_split(data,ds.target,test_size=0.2,shuffle=True)
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)
_,axes = plt.subplots(nrows=1,ncols=4,figsize=(10,4))
#Plotting Predictions
for axis,image,label in zip(axes,X_test,y_pred):
  axis.set_axis_off()
  image = image.reshape(IMG_SIZE,IMG_SIZE)
  axis.imshow(image,cmap="gray")
  axis.set_title("Prediction : {}".format(label))
print(
    f"Classification report for classifier {model}:\n"
    f"{metrics.classification_report(Y_test, y_pred)}\n"
)