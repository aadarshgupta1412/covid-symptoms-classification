import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import preprocessing, model_selection
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.metrics import precision_recall_fscore_support, classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.cross_decomposition import PLSRegression
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, StackingClassifier, VotingClassifier
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap

import umap.umap_ as umap

def printinfo(training_data):
    temp = pd.DataFrame(index = training_data.columns)
    temp['data_type'] = training_data.dtypes
    temp['null_count'] = training_data.isnull().sum()
    return temp

def isNaN(num):
    return num != num

def decade(x):
  return math.ceil(x/10)

def find_label(data):
  labels = data['test_status']
  del data['test_status']
  return data, labels

def split_data(training_data, labels):
  X_train, X_val,Y_train,Y_val = train_test_split(training_data,labels,test_size=0.20,random_state=40)
  return training_data, X_train, X_val, Y_train, Y_val

def find_scores(data, model):
  scores = cross_validate(model, data, labels1, cv=3, scoring=('accuracy', 'precision', 'recall', 'f1', 'roc_auc'), return_train_score=False)
  scores['test_accuracy'] = scores['test_accuracy'].mean()
  scores['fit_time'] = scores['fit_time'].mean()
  scores['test_precision'] = scores['test_precision'].mean()
  scores['test_recall'] = scores['test_recall'].mean()
  scores['test_f1'] = scores['test_f1'].mean()
  scores['test_roc_auc'] = scores['test_roc_auc'].mean()
  scores['score_time'] = scores['score_time'].mean()
  scores.pop('score_time')
  df = pd.DataFrame.from_dict([scores])
  return df

def summary_report(data):
  #data, X_train, X_val, Y_train, Y_val = split_data(data)
  #results = {}
  model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                 'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
                 #, 'Ensemble: VotingClassifier']
  #score_param = ['Training-Time', 'Accuracy', 'F1 Score', 'Precision', 'Recall', 'AUC-ROC']
  score_param = ['Accuracy', 'F1 Score', 'Precision', 'Recall', 'AUC-ROC']

  scores = pd.DataFrame()
  model1 = LogisticRegression()
  scores = scores.append(find_scores(data, model1), ignore_index=True)
  model2 = LinearDiscriminantAnalysis()
  scores = scores.append(find_scores(data, model2), ignore_index=True)
  model3 = KNeighborsClassifier()
  scores = scores.append(find_scores(data, model3), ignore_index=True)
  model4 = DecisionTreeClassifier()
  scores = scores.append(find_scores(data, model4), ignore_index=True)
  model5 = RandomForestClassifier()
  scores = scores.append(find_scores(data, model5), ignore_index=True)
  model6 = GaussianNB()
  scores = scores.append(find_scores(data, model6), ignore_index=True)
  model7 = SVC()
  scores = scores.append(find_scores(data, model7), ignore_index=True)
  model8 = BaggingClassifier()
  scores = scores.append(find_scores(data, model8), ignore_index=True)
  model9 = AdaBoostClassifier()
  scores = scores.append(find_scores(data, model9), ignore_index=True)
  model10 = GradientBoostingClassifier()
  scores = scores.append(find_scores(data, model10), ignore_index=True)
  estimators = [('LR', model1), ('LDA', model2), ('KNN', model3), ('DT', model4), ('RF', model5),
                ('GNB', model6), ('SVM', model7), ('BG', model8),  ('AB', model9), ('GB', model10)]
  model11 = StackingClassifier(estimators = estimators)
  scores = scores.append(find_scores(data, model11), ignore_index=True)
  #model12 = VotingClassifier(estimators = estimators, voting='hard')
  #scores = scores.append(find_scores(data, model12), ignore_index=True)
  scores.index = model_names
  scores.columns = score_param
  #scores['Training-Time'] = scores['Training-Time'].round(decimals = 4)
  scores['Accuracy'] = scores['Accuracy']*100
  scores['Accuracy'] = scores['Accuracy'].round(decimals = 2)
  scores['F1 Score'] = scores['F1 Score']*100
  scores['F1 Score'] = scores['F1 Score'].round(decimals = 2)
  scores['Precision'] = scores['Precision']*100
  scores['Precision'] = scores['Precision'].round(decimals = 2)
  scores['Recall'] = scores['Recall']*100
  scores['Recall'] = scores['Recall'].round(decimals = 2)
  scores['AUC-ROC'] = scores['AUC-ROC']*100
  scores['AUC-ROC'] = scores['AUC-ROC'].round(decimals = 2)
  pd.set_option('display.float_format','{:.3f}'.format)
  return scores

# Give the data as input and parameter (Accuracy/F1 Score, etc.) to plot for each of the 11 models

def model_plot(data, var):
  model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                 'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
  score = summary_report(data)
  acc = score[var]
  plt.plot(model_names, acc)
  plt.xticks(rotation=90)
  plt.show()

def box_plot(data):
  N = len(data.columns)
  if N<=9:
    plt.figure(figsize = (20,10))
    for i in range(N):
      plt.subplot(3, 3, i+1)
      sns.boxplot(x=data[data.columns[i]])
    plt.show()
  else:
    plt.figure(figsize = (20,10))
    for i in range(9):
      plt.subplot(3, 3, i+1)
      sns.boxplot(x=data[data.columns[i]])
    plt.show()
    plt.figure(figsize = (20,10))
    for i in range(N-9):
      plt.subplot(3, 3, i+1)
      sns.boxplot(x=data[data.columns[9+i]])
    plt.show()

def kde_plot(data):
  N = len(data.columns)
  if N<=9:
    plt.figure(figsize = (20,10))
    for i in range(N):
      plt.subplot(3, 3, i+1)
      sns.kdeplot(x=data[data.columns[i]])
    plt.show()
  else:
    plt.figure(figsize = (20,10))
    for i in range(9):
      plt.subplot(3, 3, i+1)
      sns.kdeplot(x=data[data.columns[i]])
    plt.show()
    plt.figure(figsize = (20,10))
    for i in range(N-9):
      plt.subplot(3, 3, i+1)
      sns.kdeplot(x=data[data.columns[9+i]])
    plt.show()

def analysis(data):
  print('Skew measurement of each column:', '\n')
  print(data.skew(), "\n")
  print('Box Plots:', '\n')
  box_plot(data)
  print('KDE Plots:', '\n')
  kde_plot(data)

def correlation_plot(training_newdata):
    corr = abs(training_newdata.corr()) # correlation matrix
    lower_triangle = np.tril(corr, k = -1)  # select only the lower triangle of the correlation matrix
    mask = lower_triangle == 0  # to mask the upper triangle in the following heatmap

    plt.figure(figsize = (15,10))  # setting the figure size
    sns.heatmap(lower_triangle, center=0.5, cmap= 'Blues', xticklabels = corr.index,
                yticklabels = corr.columns,cbar = False, annot= True, linewidths= 1, mask = mask)   #Heatmap
    plt.show()