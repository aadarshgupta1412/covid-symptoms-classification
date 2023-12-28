import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def n_plotPCA(data):
    sc = StandardScaler()
    data2 = sc.fit_transform(data)
    #model_names = ['Logistic Regression', 'LDA', 'K-Neighbors Classifier', 'Decision Tree Classifier', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                    #'Bagging Classifier', 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
    #plt.figure(figsize=(100, 100)
    n_array = []
    acc = pd.DataFrame()
    for i in range(2, 12):
        n_array.append(i)
        name = 'n='+str(i)
        pca = PCA(n_components = i)
        data3 = pca.fit_transform(data2)
        explained_variance = pca.explained_variance_ratio_
        #print('Result for PCA : n_components=', i)
        score = summary_report2(data3)
        acc[name] = score['Accuracy']

    return n_array, acc

n_array, acc = n_plotPCA(data2)
print(acc)

rf = pd.DataFrame(acc.iloc[[2,]]).to_numpy()[0]
ada = pd.DataFrame(acc.iloc[[4,]]).to_numpy()[0]

plt.title('Accuracy vs number of Principal Components (PCA)')
plt.bar(n_array, rf, label='Random Forest' ,color='purple')
plt.ylim([85, 100])
plt.legend()
image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'myimage.svg'
plt.tight_layout()
plt.savefig(image_name, format=image_format, dpi=1500)
plt.show()

plt.title('AdaBoost: number of Principal Components (PCA)', size = 15)
plt.bar(n_array, ada, color='purple')
plt.ylim([90, 95])
plt.ylabel('Accuracy', size=12)
plt.xlabel('n_component', size=12)
plt.xticks(size=10)
plt.yticks(size=10)
#plt.legend()
image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'fig5.svg'
plt.tight_layout()
plt.savefig(image_name, format=image_format, dpi=1500)
plt.show()



