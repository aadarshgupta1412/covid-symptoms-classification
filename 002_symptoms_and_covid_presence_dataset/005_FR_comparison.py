import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def feature_score(data, var):
    import umap.umap_ as umap
    model_names = ['Logistic Regression', 'K-Neighbors Classifier', 'Random Forest Classifier', 'SVM',
                 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']

    sc = StandardScaler()
    data1 = sc.fit_transform(data)
    pca = PCA(n_components = 7)
    data1 = pca.fit_transform(data1)

    reducer = umap.UMAP()
    data2 = reducer.fit_transform(data)

    #embedding = Isomap(n_components=11)
    #data3 = embedding.fit_transform(data[:len(data)])

    tabular_score = pd.DataFrame()

    score = summary_report2(data)
    nofr = score[var]
    tabular_score['Without FR'] = nofr
    score1 = summary_report2(data1)
    pca = score1[var]
    tabular_score['PCA'] = pca
    score2 = summary_report2(data2)
    umap = score2[var]
    tabular_score['UMAP'] = umap
    #score3 = summary_report2(data3)
    #isomap = score3[var]
    #tabular_score['ISOMAP'] = isomap

    return tabular_score
    '''plt.plot(model_names, nofr, linestyle='--', linewidth=2, color='orange', label='Without FR Techniques')
    plt.plot(model_names, pca, linestyle='--', linewidth=2, color='red', label='PCA')
    plt.plot(model_names, umap, linestyle='--', linewidth=2, color='blue', label='UMAP')
    plt.plot(model_names, isomap, linestyle='--', linewidth=2, color='green', label='ISOMAP')
    plt.xticks(rotation=90)
    plt.legend()
    return plt, tabular_score
    '''

tb = feature_score(data2, 'Accuracy')
print(tb)

w = 0.4

model_names = ['Logistic Regression', 'K-Neighbors Classifier', 'Random Forest Classifier', 'SVM',
                 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']

nofr = tb['Without FR']
pca = tb['PCA']
#umap = tb['UMAP']

bar1 = np.arange(len(model_names))
bar2 = [i+w for i in bar1]
#bar3 = [i+w for i in bar2]
'''bar4 = [i+w for i in bar3]
bar5 = [i+w for i in bar4]
bar6 = [i+w for i in bar5]
bar7 = [i+w for i in bar6]
'''
fig = plt.figure()
plt.xlabel('Classifier type', fontsize=10)
plt.ylabel('Accuracy', fontsize=10)
plt.title('Accuracy for Feature Reduction techniques vs Classifiers', fontsize=15)
plt.xticks(size=8)
plt.yticks(size=8)
plt.bar(bar1, nofr, w, label='No feature reduction')
plt.bar(bar2, pca, w, label='PCA')
#plt.bar(bar3, umap, w, label='UMAP')
plt.legend(fontsize=10)
plt.ylim([85,95])
image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'myimage2.svg'
plt.tight_layout()
plt.savefig(image_name, format=image_format, dpi=1500)
plt.show()

w = 0.2

model_names = ['Logistic Regression', 'K-Neighbors Classifier', 'Random Forest Classifier', 'SVM',
                 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']

nofr = tb['Without FR']
pca = tb['PCA']
umap = tb['UMAP']

bar1 = np.arange(len(model_names))
bar2 = [i+w for i in bar1]
bar3 = [i+w for i in bar2]
'''bar4 = [i+w for i in bar3]
bar5 = [i+w for i in bar4]
bar6 = [i+w for i in bar5]
bar7 = [i+w for i in bar6]
'''
fig = plt.figure(figsize = (20, 15))
plt.xlabel('CLassifier type', fontsize=20)
plt.ylabel('Accuracy', fontsize=20)
plt.title('Accuracy for Feature Reduction techniques vs Classifiers', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.bar(bar1, nofr, w, label='No feature reduction')
plt.bar(bar2, pca, w, label='PCA')
plt.bar(bar3, umap, w, label='UMAP')
plt.legend(fontsize=15)
plt.ylim([85,95])
plt.show()