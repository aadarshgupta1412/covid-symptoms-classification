import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

data1, labels1 = find_label(total_data1)

# Data Analysis
analysis(data1)
correlation_plot(data1)

# Model Plot
model_plot(data1, 'Accuracy')

def summary_report1(data):
  #data, X_train, X_val, Y_train, Y_val = split_data(data)
  #results = {}
  model_names = ['Logistic Regression', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
                 #, 'Ensemble: VotingClassifier']
  score_param = ['Accuracy', 'F1 Score', 'Precision', 'Recall', 'AUC-ROC']

  scores = pd.DataFrame()
  model1 = LogisticRegression()
  scores = scores.append(find_scores(data, model1), ignore_index=True)
  #model2 = LinearDiscriminantAnalysis()
  #scores = scores.append(find_scores(data, model2), ignore_index=True)
  #model3 = KNeighborsClassifier()
  #scores = scores.append(find_scores(data, model3), ignore_index=True)
  #model4 = DecisionTreeClassifier()
  #scores = scores.append(find_scores(data, model4), ignore_index=True)
  model5 = RandomForestClassifier()
  scores = scores.append(find_scores(data, model5), ignore_index=True)
  model6 = GaussianNB()
  scores = scores.append(find_scores(data, model6), ignore_index=True)
  model7 = SVC()
  scores = scores.append(find_scores(data, model7), ignore_index=True)
  #model8 = BaggingClassifier()
  #scores = scores.append(find_scores(data, model8), ignore_index=True)
  model9 = AdaBoostClassifier()
  scores = scores.append(find_scores(data, model9), ignore_index=True)
  model10 = GradientBoostingClassifier()
  scores = scores.append(find_scores(data, model10), ignore_index=True)
  estimators = [('LR', model1), ('RF', model5),
                ('GNB', model6), ('SVM', model7),  ('AB', model9), ('GB', model10)]
  model11 = StackingClassifier(estimators = estimators)
  scores = scores.append(find_scores(data, model11), ignore_index=True)
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

summary_report1(data1)

# Give the data as input and parameter (Accuracy/F1 Score, etc.) to obtain bar plot for each of the 11 models

def model_bar(data, var):
  model_names = ['Logistic Regression', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
  score = summary_report1(data)
  acc = score[var]
  plt.bar(model_names, acc)
  plt.xticks(rotation=90)
  plt.ylim([50, 80])
  plt.show()

model_bar(data1, 'Accuracy')

