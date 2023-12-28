import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def complete_PCA_analysis(data, var):
  sc = StandardScaler()
  data2 = sc.fit_transform(data)
  model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                  'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
  for i in range(2, data2.shape[1]):
      pca = PCA(n_components = i)
      data3 = pca.fit_transform(data2)
      explained_variance = pca.explained_variance_ratio_
      #print('Result for PCA : n_components=', i)
      score = summary_report(data3)
      plt.plot(model_names,score[var], label=i)
  plt.xticks(rotation=90)
  plt.legend()
  plt.show()

complete_PCA_analysis(data1, 'Accuracy')
complete_PCA_analysis(data1, 'F1 Score')

def PCA_analysis_modified(data, var):
  sc = StandardScaler()
  data2 = sc.fit_transform(data)
  model_names = ['Logistic Regression', 'LDA', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                  'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
  for i in range(2, 8):
      pca = PCA(n_components = i)
      data3 = pca.fit_transform(data2)
      explained_variance = pca.explained_variance_ratio_
      #print('Result for PCA : n_components=', i)
      score = summary_report(data3)
      score = score.drop(['K-Neighbors Classifier', 'Decision Tree Classifier', 'Bagging Classifier'])

      plt.plot(model_names,score[var], label=i)
  plt.xticks(rotation=90)
  plt.legend()
  plt.show()

PCA_analysis_modified(data1, 'Accuracy')
PCA_analysis_modified(data1, 'F1 Score')

def n_plotPCA(data):
    sc = StandardScaler()
    data2 = sc.fit_transform(data)
    #model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                    #'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
    #plt.figure(figsize=(100, 100)
    n_array = []
    lr, lda, knn, dst, rf, gnb, svm, bc, abc, gbc, ensemble = [], [], [], [], [], [], [], [], [], [], []
    for i in range(2, len(data.columns)):
        n_array.append(i)
        pca = PCA(n_components = i)
        data3 = pca.fit_transform(data2)
        explained_variance = pca.explained_variance_ratio_
        #print('Result for PCA : n_components=', i)
        score = summary_report(data3)
        lr.append(score['Accuracy'][0])
        lda.append(score['Accuracy'][1])
        knn.append(score['Accuracy'][2])
        dst.append(score['Accuracy'][3])
        rf.append(score['Accuracy'][4])
        gnb.append(score['Accuracy'][5])
        svm.append(score['Accuracy'][6])
        bc.append(score['Accuracy'][7])
        abc.append(score['Accuracy'][8])
        gbc.append(score['Accuracy'][9])
        ensemble.append(score['Accuracy'][10])
    return n_array, lr, lda, knn, dst, rf, gnb, svm, bc, abc, gbc, ensemble

def n_tablePCA(data):
    sc = StandardScaler()
    data2 = sc.fit_transform(data)
    final_score = pd.DataFrame()
    for i in range(2, len(data.columns)):
        name = 'n_comp=' + str(i)
        pca = PCA(n_components = i)
        data3 = pca.fit_transform(data2)
        explained_variance = pca.explained_variance_ratio_
        score = summary_report(data3)
        final_score[name] = score['Accuracy']
    return final_score

n_tablePCA(data1)

# best n_component = 2
#
sc = StandardScaler()
data1p = sc.fit_transform(data1)
pca = PCA(n_components = 2)
data1p = pca.fit_transform(data1p)

model_plot(data1p, 'Accuracy')
model_plot(data1p, 'F1 Score')
