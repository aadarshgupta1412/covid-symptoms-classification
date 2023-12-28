import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

data2, labels2 = find_label(total_data2)

# Data Analysis
analysis(data2)
correlation_plot(data2)

data2, X_train, X_val, Y_train, Y_val = split_data(data2, labels2)

# Model Plot
model_plot(data2, 'Accuracy')

model5 = RandomForestClassifier()
print("Model 5 : Random Forest Classifier", "\n")
model5.fit(X_train, Y_train)
prediction = model5.predict(X_val)
print("Acurracy of the model :", accuracy_score(Y_val, prediction), "\n")
print("Confusion matrix :","\n", confusion_matrix(Y_val, prediction), "\n")
print(classification_report(Y_val, prediction), "\n")

importance = model5.feature_importances_
import matplotlib.pyplot as plt
plt.title('Feature Importances')
plt.barh(['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Running Nose', 'Asthma', 'Chronic Lung Disease', 'Headache',
       'Heart Disease', 'Diabetes', 'Hyper Tension', 'Fatigue ',
       'Abroad travel', 'Contact with COVID Patient'], importance, color='b', align='center')
#plt.barh(['age_decade', 'ftg', 'fever', 'gender_label', 'loss_of_smell', 'cough'],
#        importance, color='b', align='center')
plt.tight_layout()
image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'feature_importance.svg'
plt.savefig(image_name, format=image_format, dpi=1200)
plt.show()

def find_scores(data, model):
  scores = cross_validate(model, data, labels2, cv=3, scoring=('accuracy', 'precision', 'recall', 'f1', 'roc_auc'), return_train_score=False)
  scores['test_accuracy'] = scores['test_accuracy'].mean()
  scores['fit_time'] = scores['fit_time'].mean()
  scores['test_precision'] = scores['test_precision'].mean()
  scores['test_recall'] = scores['test_recall'].mean()
  scores['test_f1'] = scores['test_f1'].mean()
  scores['test_roc_auc'] = scores['test_roc_auc'].mean()
  scores['score_time'] = scores['score_time'].mean()
  scores.pop('score_time')
  scores.pop('fit_time')
  df = pd.DataFrame.from_dict([scores])
  return df

def summary_report2(data):
  #data, X_train, X_val, Y_train, Y_val = split_data(data)
  #results = {}
  model_names = ['Logistic Regression', 'K-Nearest Neighbors', 'Random Forest Classifier', 'Gaussian Naive Bayes', 'SVM',
                 'Ada Boost Classifier', 'Gradient Boosting Classifier', 'Ensemble: Stacking Classifier']
                 #, 'Ensemble: VotingClassifier']
  score_param = ['Accuracy', 'F1 Score', 'Precision', 'Recall', 'AUC-ROC']

  scores = pd.DataFrame()
  model1 = LogisticRegression()
  scores = scores.append(find_scores(data, model1), ignore_index=True)
  #model2 = LinearDiscriminantAnalysis()
  #scores = scores.append(find_scores(data, model2), ignore_index=True)
  model3 = KNeighborsClassifier()
  scores = scores.append(find_scores(data, model3), ignore_index=True)
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
  estimators = [('LR', model1), ('KNN', model3), ('RF', model5),
                ('SVM', model7),  ('AB', model9), ('GB', model10)]
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

