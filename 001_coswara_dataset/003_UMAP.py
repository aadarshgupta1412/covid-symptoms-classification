import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

reducer = umap.UMAP()
data1u = reducer.fit_transform(data1)

model_plot(data1u, 'Accuracy')

model_plot(data1u, 'F1 Score')

