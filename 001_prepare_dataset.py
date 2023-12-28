import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
import math

from utils import printinfo, isNaN, decade, find_label, split_data, model_plot, box_plot, kde_plot, analysis, correlation_plot, find_scores, summary_report

url1 = '/content/drive/MyDrive/COVID project datasets/combined_data.csv'
url2 = '/content/drive/MyDrive/COVID project datasets/Covid_Dataset.csv'
train_data = pd.read_csv(url1)
new_data = pd.read_csv(url2)
training_data = train_data[['a', 'g', 'smoker', 'cold', 'cough', 'diarrhoea', 'fever',
                            'loss_of_smell', 'mp', 'test_status', 'bd', 'ftg', 'st']]
training_newdata = training_data[training_data['test_status'].notnull()]

def preprocessing(training_data):
    import math
    from sklearn import preprocessing

    training_data['age_decade'] = training_data['a'].apply(lambda x: decade(x))
    gender = preprocessing.LabelEncoder()
    training_data['gender_label'] = gender.fit_transform(training_data['g'])
    training_data['smoker'] = training_data['smoker'].apply(lambda x: 1 if x=='True' or x == 'y' else 0)
    training_data['cold'] = training_data['cold'].apply(lambda x: 1 if not(isNaN(x)) else 0)
    training_data['cough'] = training_data['cough'].apply(lambda x: 1 if not(isNaN(x)) else 0)
    training_data['diarrhoea'] = training_data['diarrhoea'].apply(lambda x: 1 if not(isNaN(x)) else 0)
    training_data['fever'] = training_data['fever'].apply(lambda x: 1 if not(isNaN(x)) else 0)
    training_data['loss_of_smell'] = training_data['loss_of_smell'].apply(lambda x: 1 if not(isNaN(x)) else 0)
    training_data['mp'] = training_data['mp'].apply(lambda x: 1 if not(isNaN(x)) else 0)                         # muscle pain
    training_data['test_status'] = training_data['test_status'].apply(lambda x: 1 if x=='p' else 0)
    training_data['bd'] = training_data['bd'].apply(lambda x: 1 if not(isNaN(x)) else 0)                         # breathing difficuties
    training_data['ftg'] = training_data['ftg'].apply(lambda x: 1 if not(isNaN(x)) else 0)                       # fatigue
    training_data['st'] = training_data['st'].apply(lambda x: 1 if not(isNaN(x)) else 0)                         # sore throat
    del training_data['g']
    del training_data['a']
    return training_data

def preprocessing4(new_data):
  import math
  from sklearn import preprocessing
  data2 = pd.DataFrame()
  data2['test_status'] = new_data['COVID-19'] #[['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat', 'Running Nose', 'Fatigue ', 'COVID-19']]
  for i in new_data.columns:
    data2[i] = new_data[i].apply(lambda x: 1 if x=='Yes' else 0)
  data2['test_status'] = data2['test_status'].apply(lambda x: 1 if x=='Yes' else 0)
  del data2['COVID-19']
  del data2['Sanitization from Market']
  del data2['Wearing Masks']
  del data2['Gastrointestinal ']
  del data2['Family working in Public Exposed Places']
  del data2['Visited Public Exposed Places']
  del data2['Attended Large Gathering']
  return data2

total_data1 = preprocessing(training_newdata)
total_data2 = preprocessing4(new_data)