import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

def plotUMAP(data):
    rf = []
    reducer = umap.UMAP()
    data2 = reducer.fit_transform(data)
    score = summary_report2(data2)
    rf.append(score['Accuracy'][4])
    return rf

rf3 = plotUMAP(data2)
print(rf3)
