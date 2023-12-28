import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def n_isomap(data):
    #model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                    #'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
    #plt.figure(figsize=(100, 100)
    n_array = []
    lr, lda, knn, dst, rf, gnb, svm, bc, abc, gbc, ensemble = [], [], [], [], [], [], [], [], [], [], []
    for i in range(2, 12):
        n_array.append(i)
        embedding = Isomap(n_components=i)
        data2 = embedding.fit_transform(data[:len(data)])
        #print('Result for PCA : n_components=', i)
        score = summary_report(data2)
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

def n_tableISOMAP(data):
    final_score = pd.DataFrame()
    for i in range(2, len(data.columns)):
        name = 'n_comp =' + str(i)
        embedding = Isomap(n_components=i)
        data2 = embedding.fit_transform(data[:len(data)])
        score = summary_report(data2)
        final_score[name] = score['Accuracy']
    return final_score

n_tableISOMAP(data1)

# best n_component = 11
#
embedding = Isomap(n_components=11)
data1i = embedding.fit_transform(data1[:len(data1)])

model_plot(data1i, 'Accuracy')
model_plot(data1i, 'F1 Score')