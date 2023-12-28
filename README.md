# Text-Based Diagnosis of COVID-19 Using Data Mining Techniques: A Comparative Study
[PDF](https://ieeexplore.ieee.org/document/10040129/)/[Presentation](INDICON2022_Presentation.pdf)

## Abstract

In the course of the recent pandemic, we have witnessed non-clinical approaches such as data mining and artificial intelligence techniques being exceedingly utilized to restrain and combat the increase of COVID-19 across the globe. The emergence of artificial intelligence in the medical field has helped in reducing the immense burden on medical systems by providing the best means for diagnosis and prognosis of COVID-19. This work attempts to analyze & evaluate superlative models on robust data resources on symptoms of COVID-19, consisting of age, gender, demographic information, pre-existing medical conditions, and symptoms experienced by patients. This study establishes a paradigmatic pipeline of supervised learning algorithms coupled with feature extraction techniques and surpasses the current state-of-the-art results by achieving an accuracy of 93.360. The optimal score was found by performing feature extraction on the data using principal component analysis (PCA) followed by binary classification using the AdaBoost classifier. In addition, the present study also establishes the contribution of various symptoms in the diagnosis of the malady.

## Installation

### Install required libraries

```
pip install -r requirements.txt
```

## Running the code

The code is split into 3 executable-able steps as depicted in the process pipeline for the 2 datasets under consideration:

![alt text](https://fwtbbmf399.execute-api.us-east-1.amazonaws.com/Prod/svg?source=https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md&name=sample.svg)

<details> 
<summary>SVG code</summary>

```
@sample.svg
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="121px" height="81px" viewBox="-0.5 -0.5 121 81" style="background-color: rgb(255, 255, 255);">
    <defs/>
    <g>
        <ellipse cx="60" cy="40" rx="60" ry="40" fill="#ffffff" stroke="#000000" pointer-events="all"/>
    </g>
</svg>
@sample.svg
```

</details>

![Process Pipeline](img/process_pipeline.svg)

- [001_prepare_dataset.py](001_prepare_dataset.py): filters the key symptoms from raw data and encodes them to process the raw dataset.

- [001_coswara_dataset](001_coswara_dataset):
  - [001_coswara_data_setup.py](001_coswara_dataset/001_coswara_data_setup.py): provides a preliminary analysis and summary report of results for various classifiers without performing feature extraction on the processed coswara dataset.
  - [002_PCA.py](001_coswara_dataset/002_PCA.py)/[003_UMAP.py](001_coswara_dataset/003_UMAP.py)/[004_ISOMAP.py](001_coswara_dataset/004_ISOMAP.py): implements feature extraction using PCA/UMAP/ISOMAP followed by classifier on the coswara dataset.
  - [005_FR_comparison.py](001_coswara_dataset/005_FR_comparison.py): provides a summary report and plots for comparison of the 3 feature extraction techniques applied on the coswara dataset.

- [002_symptoms_and_covid_presence_dataset](002_symptoms_and_covid_presence_dataset):
  - [001_kaggle_data_setup.py](002_symptoms_and_covid_presence_dataset/001_kaggle_data_setup.py): provides a preliminary analysis and summary report of results for various classifiers without performing feature extraction on the processed symptoms and covid presence (kaggle) dataset.
  - [002_PCA.py](002_symptoms_and_covid_presence_dataset/002_PCA.py)/[003_UMAP.py](002_symptoms_and_covid_presence_dataset/003_UMAP.py)/[004_ISOMAP.py](002_symptoms_and_covid_presence_dataset/004_ISOMAP.py): implements feature extraction using PCA/UMAP/ISOMAP followed by classifier on the kaggle dataset.
  - [005_FR_comparison.py](002_symptoms_and_covid_presence_dataset/005_FR_comparison.py): provides a summary report and plots for comparison of the 3 feature extraction techniques applied on the kaggle dataset.

- [covid-symptoms-classification.ipynb](full_demonstration/covid-symptoms-classification.ipynb): demonstrates a complete run of the steps on both datasets to derive inference.
## Datasets


### Coswara Dataset

https://github.com/iiscleap/Coswara-Data/

The Coswara project aims to create a COVID-19 diagnostic tool based on speech, cough, and breath sounds. Acoustic and text data was collected from public participants and the text data utilized comprised age, present health status, geographic location, gender, and health issues that already exist.

### Symptoms and COVID Presence Dataset

https://github.com/virufy/virufy_data/tree/main/clinical/segmented

The dataset was created as a synthetic substitute based on a WHO report to study viral patterns in COVID-19 patients from the sub-continental region. The dataset, predominantly comprised of Indian subjects, incorporates the symptoms responses in binary form for 5434 subjects.

## Results


