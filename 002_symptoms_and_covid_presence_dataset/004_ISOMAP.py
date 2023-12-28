import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def n_plotISOMAP(data):
    n_array = []
    rf = []
    #from scipy import sparse
    #data3 = sparse.csr_matrix(data)
    for i in range(2, 9):
        n_array.append(i)
        embedding = Isomap(n_components=i)
        data2 = embedding.fit_transform(data[:len(data)])
        score = summary_report2(data2)
        rf.append(score['Accuracy'][4])
    return n_array, rf

embedding = Isomap(n_components=6)
data3 = embedding.fit_transform(data2)

score = summary_report2(data3)
print(score)

n_array2, rf2 = n_plotISOMAP(random_data)
print(rf2)

plt.title('Accuracy vs n_components', size=15)
plt.bar(n_array2, rf2, label='Random Forest' ,color='purple')
plt.ylim([85, 100])
plt.legend()
plt.show()

