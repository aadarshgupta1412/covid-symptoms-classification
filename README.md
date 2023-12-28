# Text-Based Diagnosis of COVID-19 Using Data Mining Techniques: A Comparative Study

## Abstract

In the course of the recent pandemic, we have witnessed non-clinical approaches such as data mining and artificial intelligence techniques being exceedingly utilized to restrain and combat the increase of COVID-19 across the globe. The emergence of artificial intelligence in the medical field has helped in reducing the immense burden on medical systems by providing the best means for diagnosis and prognosis of COVID-19. This work attempts to analyze & evaluate superlative models on robust data resources on symptoms of COVID-19, consisting of age, gender, demographic information, pre-existing medical conditions, and symptoms experienced by patients. This study establishes a paradigmatic pipeline of supervised learning algorithms coupled with feature extraction techniques and surpasses the current state-of-the-art results by achieving an accuracy of 93.360. The optimal score was found by performing feature extraction on the data using principal component analysis (PCA) followed by binary classification using the AdaBoost classifier. In addition, the present study also establishes the contribution of various symptoms in the diagnosis of the malady.

## Installation

### Install required libraries

```
pip install -r requirements.txt
```

## Running the code

The code is split into 3 executable-able steps as depicted in the process pipeline for the 2 datasets under consideration:
![Process Pipeline](img/process_pipeline)

- [001_prepare_dataset.py](001_prepare_dataset.py): filters the key symptoms from raw data and encodes them to process the raw dataset.

- [001_coswara_dataset](001_coswara_dataset):
  - [001_coswara_data_setup.py](001_coswara_dataset/001_coswara_data_setup.py): provides a preliminary analysis and summary report of results for various classifiers without performing feature extraction on the processed coswara dataset.
  - [002_PCA.py](001_coswara_dataset/002_PCA.py)/[003_UMAP.py](001_coswara_dataset/003_UMAP.py)/[004_ISOMAP.py](001_coswara_dataset/004_ISOMAP.py): implements feature extraction using PCA/UMAP/ISOMAP followed by classifier on the coswara dataset.
  - [005_FR_comparison.py](001_coswara_dataset/005_FR_comparison.py): provides a summary report and plots for comparison of the 3 feature extraction techniques applied on the coswara dataset.

- [002_symptoms_and_covid_presence_dataset](002_symptoms_and_covid_presence_dataset):
  - [001_kaggle_data_setup.py](002_symptoms_and_covid_presence_dataset/001_kaggle_data_setup.py): provides a preliminary analysis and summary report of results for various classifiers without performing feature extraction on the processed symptoms and covid presence (kaggle) dataset.
  - [002_PCA.py](002_symptoms_and_covid_presence_dataset/002_PCA.py)/[003_UMAP.py](002_symptoms_and_covid_presence_dataset/003_UMAP.py)/[004_ISOMAP.py](002_symptoms_and_covid_presence_dataset/004_ISOMAP.py): implements feature extraction using PCA/UMAP/ISOMAP followed by classifier on the kaggle dataset.
  - [005_FR_comparison.py](002_symptoms_and_covid_presence_dataset/005_FR_comparison.py): provides a summary report and plots for comparison of the 3 feature extraction techniques applied on the kaggle dataset.
  
## Datasets

### Kaggle Cough-Classifier Dataset

https://www.kaggle.com/himanshu007121/coughclassifier-trial

The major problem with this dataset is, that it is highly unbalanced. Only 19 of the 170 examples are labeled as positive. <br/>
Therefore, in addition to the good test accuracy, the model shows a relatively high false-negative rate. <br/>
More data, especially positive examples, is needed to develop a reliable, cough audio-based Covid-19 test. <br/>

### Virufy Dataset

https://github.com/virufy/virufy_data/tree/main/clinical/segmented

This dataset is provided by the developers of the Virufy app. They offer a webservice (https://virufy.org/en/) which can detect a COVID-19 signature in recordings using an AI algorithm. The open dataset on github contains 121 examples of which 48 are labeled as positive.

### Balanced Dataset

The balanced dataset is created by combining the Kaggle and the Virufy dataset. Since they both contain more negative than positive examples, downsampling is used to create a perfectly balanced dataset.

### Other Datasets

Other datasets have not been investigated, yet.

- **Coswara**: https://github.com/iiscleap/Coswara-Data
- **COUGHVID**: https://zenodo.org/record/4048312

## The Model

The model used is a simple DNN with 6 Layers. The input is a 26 values feature vector calculated from the audio files using librosa.

<img src="img/model.png" width="300">

## Results

The balanced dataset is split into 8 folds and evaluated using cross validation.<br/>
The model converges after 20 epochs of training.

|             | Train Accuracy | Test Accuracy |
| ----------- | -------------: | ------------: |
| Fold 0      |       100.00 % |       94.12 % |
| Fold 1      |       100.00 % |       88.24 % |
| Fold 2      |       100.00 % |       94.12 % |
| Fold 3      |       100.00 % |       76.47 % |
| Fold 4      |       100.00 % |       88.24 % |
| Fold 5      |       100.00 % |       94.12 % |
| Fold 6      |       100.00 % |      100.00 % |
| Fold 7      |        96.61 % |       87.50 % |
| **Average** |    **99.58 %** |   **90.35 %** |

![Confusion Matrix](img/confusion_matrix_balanced.png)

## Credits

The Model is based on the Keras notebook by Himanshu which can be found here:
https://www.kaggle.com/himanshu007121/covid-19-cough-classification
