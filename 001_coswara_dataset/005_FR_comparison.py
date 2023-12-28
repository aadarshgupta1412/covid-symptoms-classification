import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def feature_plot(data, var):
    import umap.umap_ as umap

    sc = StandardScaler()
    data1 = sc.fit_transform(data)
    pca = PCA(n_components = 2)
    data1 = pca.fit_transform(data1)

    reducer = umap.UMAP()
    data2 = reducer.fit_transform(data)

    embedding = Isomap(n_components=11)
    data3 = embedding.fit_transform(data[:len(data)])

    tabular_score = pd.DataFrame()

    score = summary_report(data)
    nofr = score[var]
    tabular_score['Without FR'] = nofr
    score1 = summary_report(data1)
    pca = score1[var]
    tabular_score['PCA'] = pca
    score2 = summary_report(data2)
    umap = score2[var]
    tabular_score['UMAP'] = umap
    score3 = summary_report(data3)
    isomap = score3[var]
    tabular_score['ISOMAP'] = isomap
    model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                 'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
    plt.plot(model_names, nofr, linestyle='--', linewidth=2, color='orange', label='Without FR Techniques')
    plt.plot(model_names, pca, linestyle='--', linewidth=2, color='red', label='PCA')
    plt.plot(model_names, umap, linestyle='--', linewidth=2, color='blue', label='UMAP')
    plt.plot(model_names, isomap, linestyle='--', linewidth=2, color='green', label='ISOMAP')
    plt.xticks(rotation=90)
    plt.legend()
    return plt, tabular_score

plt1, tabular_score1 = feature_plot(data1, 'Accuracy')
plt2, tabular_score2 = feature_plot(data1, 'Training-Time')
plt3, tabular_score3 = feature_plot(data1, 'F1 Score')
