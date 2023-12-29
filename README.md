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

![process_pipeline](https://github.com/aadarshgupta1412/covid-symptoms-classification/assets/62350692/232a1c39-783f-43d9-b278-74307e57bdf3)


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

![feature_importance](https://github.com/aadarshgupta1412/covid-symptoms-classification/assets/62350692/e6dc1a0c-6e69-4b05-a7a9-7418a57d76df)

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (https://matplotlib.org/) -->
<svg height="288pt" version="1.1" viewBox="0 0 432 288" width="432pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 288 
L 432 288 
L 432 0 
L 0 0 
z
" style="fill:#ffffff;"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 153.8 260.2 
L 418.023087 260.2 
L 418.023087 26.8 
L 153.8 26.8 
z
" style="fill:#ffffff;"/>
   </g>
   <g id="patch_3">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 249.590909 
L 380.627931 249.590909 
L 380.627931 237.290514 
L 153.8 237.290514 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_4">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 234.215415 
L 270.295292 234.215415 
L 270.295292 221.91502 
L 153.8 221.91502 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_5">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 218.839921 
L 341.827749 218.839921 
L 341.827749 206.539526 
L 153.8 206.539526 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_6">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 203.464427 
L 405.441036 203.464427 
L 405.441036 191.164032 
L 153.8 191.164032 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_7">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 188.088933 
L 191.511842 188.088933 
L 191.511842 175.788538 
L 153.8 175.788538 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_8">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 172.713439 
L 189.488683 172.713439 
L 189.488683 160.413043 
L 153.8 160.413043 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_9">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 157.337945 
L 195.7408 157.337945 
L 195.7408 145.037549 
L 153.8 145.037549 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_10">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 141.962451 
L 190.59835 141.962451 
L 190.59835 129.662055 
L 153.8 129.662055 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_11">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 126.586957 
L 200.283901 126.586957 
L 200.283901 114.286561 
L 153.8 114.286561 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_12">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 111.211462 
L 186.289537 111.211462 
L 186.289537 98.911067 
L 153.8 98.911067 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_13">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 95.835968 
L 193.25402 95.835968 
L 193.25402 83.535573 
L 153.8 83.535573 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_14">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 80.460474 
L 191.878749 80.460474 
L 191.878749 68.160079 
L 153.8 68.160079 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_15">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 65.08498 
L 368.634468 65.08498 
L 368.634468 52.784585 
L 153.8 52.784585 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="patch_16">
    <path clip-path="url(#pf5091c3e1a)" d="M 153.8 49.709486 
L 306.955744 49.709486 
L 306.955744 37.409091 
L 153.8 37.409091 
z
" style="fill:#0000ff;"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <defs>
       <path d="M 0 0 
L 0 3.5 
" id="m112681208e" style="stroke:#000000;stroke-width:0.8;"/>
      </defs>
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 0.000 -->
      <defs>
       <path d="M 31.78125 66.40625 
Q 24.171875 66.40625 20.328125 58.90625 
Q 16.5 51.421875 16.5 36.375 
Q 16.5 21.390625 20.328125 13.890625 
Q 24.171875 6.390625 31.78125 6.390625 
Q 39.453125 6.390625 43.28125 13.890625 
Q 47.125 21.390625 47.125 36.375 
Q 47.125 51.421875 43.28125 58.90625 
Q 39.453125 66.40625 31.78125 66.40625 
z
M 31.78125 74.21875 
Q 44.046875 74.21875 50.515625 64.515625 
Q 56.984375 54.828125 56.984375 36.375 
Q 56.984375 17.96875 50.515625 8.265625 
Q 44.046875 -1.421875 31.78125 -1.421875 
Q 19.53125 -1.421875 13.0625 8.265625 
Q 6.59375 17.96875 6.59375 36.375 
Q 6.59375 54.828125 13.0625 64.515625 
Q 19.53125 74.21875 31.78125 74.21875 
z
" id="DejaVuSans-48"/>
       <path d="M 10.6875 12.40625 
L 21 12.40625 
L 21 0 
L 10.6875 0 
z
" id="DejaVuSans-46"/>
      </defs>
      <g transform="translate(139.485938 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-48"/>
       <use x="159.033203" xlink:href="#DejaVuSans-48"/>
       <use x="222.65625" xlink:href="#DejaVuSans-48"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_2">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="190.290702" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 0.025 -->
      <defs>
       <path d="M 19.1875 8.296875 
L 53.609375 8.296875 
L 53.609375 0 
L 7.328125 0 
L 7.328125 8.296875 
Q 12.9375 14.109375 22.625 23.890625 
Q 32.328125 33.6875 34.8125 36.53125 
Q 39.546875 41.84375 41.421875 45.53125 
Q 43.3125 49.21875 43.3125 52.78125 
Q 43.3125 58.59375 39.234375 62.25 
Q 35.15625 65.921875 28.609375 65.921875 
Q 23.96875 65.921875 18.8125 64.3125 
Q 13.671875 62.703125 7.8125 59.421875 
L 7.8125 69.390625 
Q 13.765625 71.78125 18.9375 73 
Q 24.125 74.21875 28.421875 74.21875 
Q 39.75 74.21875 46.484375 68.546875 
Q 53.21875 62.890625 53.21875 53.421875 
Q 53.21875 48.921875 51.53125 44.890625 
Q 49.859375 40.875 45.40625 35.40625 
Q 44.1875 33.984375 37.640625 27.21875 
Q 31.109375 20.453125 19.1875 8.296875 
z
" id="DejaVuSans-50"/>
       <path d="M 10.796875 72.90625 
L 49.515625 72.90625 
L 49.515625 64.59375 
L 19.828125 64.59375 
L 19.828125 46.734375 
Q 21.96875 47.46875 24.109375 47.828125 
Q 26.265625 48.1875 28.421875 48.1875 
Q 40.625 48.1875 47.75 41.5 
Q 54.890625 34.8125 54.890625 23.390625 
Q 54.890625 11.625 47.5625 5.09375 
Q 40.234375 -1.421875 26.90625 -1.421875 
Q 22.3125 -1.421875 17.546875 -0.640625 
Q 12.796875 0.140625 7.71875 1.703125 
L 7.71875 11.625 
Q 12.109375 9.234375 16.796875 8.0625 
Q 21.484375 6.890625 26.703125 6.890625 
Q 35.15625 6.890625 40.078125 11.328125 
Q 45.015625 15.765625 45.015625 23.390625 
Q 45.015625 31 40.078125 35.4375 
Q 35.15625 39.890625 26.703125 39.890625 
Q 22.75 39.890625 18.8125 39.015625 
Q 14.890625 38.140625 10.796875 36.28125 
z
" id="DejaVuSans-53"/>
      </defs>
      <g transform="translate(175.97664 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-48"/>
       <use x="159.033203" xlink:href="#DejaVuSans-50"/>
       <use x="222.65625" xlink:href="#DejaVuSans-53"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_3">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="226.781405" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 0.050 -->
      <g transform="translate(212.467342 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-48"/>
       <use x="159.033203" xlink:href="#DejaVuSans-53"/>
       <use x="222.65625" xlink:href="#DejaVuSans-48"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_4">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="263.272107" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 0.075 -->
      <defs>
       <path d="M 8.203125 72.90625 
L 55.078125 72.90625 
L 55.078125 68.703125 
L 28.609375 0 
L 18.3125 0 
L 43.21875 64.59375 
L 8.203125 64.59375 
z
" id="DejaVuSans-55"/>
      </defs>
      <g transform="translate(248.958045 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-48"/>
       <use x="159.033203" xlink:href="#DejaVuSans-55"/>
       <use x="222.65625" xlink:href="#DejaVuSans-53"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_5">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="299.76281" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 0.100 -->
      <defs>
       <path d="M 12.40625 8.296875 
L 28.515625 8.296875 
L 28.515625 63.921875 
L 10.984375 60.40625 
L 10.984375 69.390625 
L 28.421875 72.90625 
L 38.28125 72.90625 
L 38.28125 8.296875 
L 54.390625 8.296875 
L 54.390625 0 
L 12.40625 0 
z
" id="DejaVuSans-49"/>
      </defs>
      <g transform="translate(285.448747 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-49"/>
       <use x="159.033203" xlink:href="#DejaVuSans-48"/>
       <use x="222.65625" xlink:href="#DejaVuSans-48"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_6">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="336.253512" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 0.125 -->
      <g transform="translate(321.93945 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-49"/>
       <use x="159.033203" xlink:href="#DejaVuSans-50"/>
       <use x="222.65625" xlink:href="#DejaVuSans-53"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_7">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="372.744215" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 0.150 -->
      <g transform="translate(358.430152 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-49"/>
       <use x="159.033203" xlink:href="#DejaVuSans-53"/>
       <use x="222.65625" xlink:href="#DejaVuSans-48"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_8">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="409.234917" xlink:href="#m112681208e" y="260.2"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 0.175 -->
      <g transform="translate(394.920855 274.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-48"/>
       <use x="63.623047" xlink:href="#DejaVuSans-46"/>
       <use x="95.410156" xlink:href="#DejaVuSans-49"/>
       <use x="159.033203" xlink:href="#DejaVuSans-55"/>
       <use x="222.65625" xlink:href="#DejaVuSans-53"/>
      </g>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_9">
      <defs>
       <path d="M 0 0 
L -3.5 0 
" id="m819bcadd00" style="stroke:#000000;stroke-width:0.8;"/>
      </defs>
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="243.440711"/>
      </g>
     </g>
     <g id="text_9">
      <!-- Breathing Problem -->
      <defs>
       <path d="M 19.671875 34.8125 
L 19.671875 8.109375 
L 35.5 8.109375 
Q 43.453125 8.109375 47.28125 11.40625 
Q 51.125 14.703125 51.125 21.484375 
Q 51.125 28.328125 47.28125 31.5625 
Q 43.453125 34.8125 35.5 34.8125 
z
M 19.671875 64.796875 
L 19.671875 42.828125 
L 34.28125 42.828125 
Q 41.5 42.828125 45.03125 45.53125 
Q 48.578125 48.25 48.578125 53.8125 
Q 48.578125 59.328125 45.03125 62.0625 
Q 41.5 64.796875 34.28125 64.796875 
z
M 9.8125 72.90625 
L 35.015625 72.90625 
Q 46.296875 72.90625 52.390625 68.21875 
Q 58.5 63.53125 58.5 54.890625 
Q 58.5 48.1875 55.375 44.234375 
Q 52.25 40.28125 46.1875 39.3125 
Q 53.46875 37.75 57.5 32.78125 
Q 61.53125 27.828125 61.53125 20.40625 
Q 61.53125 10.640625 54.890625 5.3125 
Q 48.25 0 35.984375 0 
L 9.8125 0 
z
" id="DejaVuSans-66"/>
       <path d="M 41.109375 46.296875 
Q 39.59375 47.171875 37.8125 47.578125 
Q 36.03125 48 33.890625 48 
Q 26.265625 48 22.1875 43.046875 
Q 18.109375 38.09375 18.109375 28.8125 
L 18.109375 0 
L 9.078125 0 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.1875 
Q 20.953125 51.171875 25.484375 53.578125 
Q 30.03125 56 36.53125 56 
Q 37.453125 56 38.578125 55.875 
Q 39.703125 55.765625 41.0625 55.515625 
z
" id="DejaVuSans-114"/>
       <path d="M 56.203125 29.59375 
L 56.203125 25.203125 
L 14.890625 25.203125 
Q 15.484375 15.921875 20.484375 11.0625 
Q 25.484375 6.203125 34.421875 6.203125 
Q 39.59375 6.203125 44.453125 7.46875 
Q 49.3125 8.734375 54.109375 11.28125 
L 54.109375 2.78125 
Q 49.265625 0.734375 44.1875 -0.34375 
Q 39.109375 -1.421875 33.890625 -1.421875 
Q 20.796875 -1.421875 13.15625 6.1875 
Q 5.515625 13.8125 5.515625 26.8125 
Q 5.515625 40.234375 12.765625 48.109375 
Q 20.015625 56 32.328125 56 
Q 43.359375 56 49.78125 48.890625 
Q 56.203125 41.796875 56.203125 29.59375 
z
M 47.21875 32.234375 
Q 47.125 39.59375 43.09375 43.984375 
Q 39.0625 48.390625 32.421875 48.390625 
Q 24.90625 48.390625 20.390625 44.140625 
Q 15.875 39.890625 15.1875 32.171875 
z
" id="DejaVuSans-101"/>
       <path d="M 34.28125 27.484375 
Q 23.390625 27.484375 19.1875 25 
Q 14.984375 22.515625 14.984375 16.5 
Q 14.984375 11.71875 18.140625 8.90625 
Q 21.296875 6.109375 26.703125 6.109375 
Q 34.1875 6.109375 38.703125 11.40625 
Q 43.21875 16.703125 43.21875 25.484375 
L 43.21875 27.484375 
z
M 52.203125 31.203125 
L 52.203125 0 
L 43.21875 0 
L 43.21875 8.296875 
Q 40.140625 3.328125 35.546875 0.953125 
Q 30.953125 -1.421875 24.3125 -1.421875 
Q 15.921875 -1.421875 10.953125 3.296875 
Q 6 8.015625 6 15.921875 
Q 6 25.140625 12.171875 29.828125 
Q 18.359375 34.515625 30.609375 34.515625 
L 43.21875 34.515625 
L 43.21875 35.40625 
Q 43.21875 41.609375 39.140625 45 
Q 35.0625 48.390625 27.6875 48.390625 
Q 23 48.390625 18.546875 47.265625 
Q 14.109375 46.140625 10.015625 43.890625 
L 10.015625 52.203125 
Q 14.9375 54.109375 19.578125 55.046875 
Q 24.21875 56 28.609375 56 
Q 40.484375 56 46.34375 49.84375 
Q 52.203125 43.703125 52.203125 31.203125 
z
" id="DejaVuSans-97"/>
       <path d="M 18.3125 70.21875 
L 18.3125 54.6875 
L 36.8125 54.6875 
L 36.8125 47.703125 
L 18.3125 47.703125 
L 18.3125 18.015625 
Q 18.3125 11.328125 20.140625 9.421875 
Q 21.96875 7.515625 27.59375 7.515625 
L 36.8125 7.515625 
L 36.8125 0 
L 27.59375 0 
Q 17.1875 0 13.234375 3.875 
Q 9.28125 7.765625 9.28125 18.015625 
L 9.28125 47.703125 
L 2.6875 47.703125 
L 2.6875 54.6875 
L 9.28125 54.6875 
L 9.28125 70.21875 
z
" id="DejaVuSans-116"/>
       <path d="M 54.890625 33.015625 
L 54.890625 0 
L 45.90625 0 
L 45.90625 32.71875 
Q 45.90625 40.484375 42.875 44.328125 
Q 39.84375 48.1875 33.796875 48.1875 
Q 26.515625 48.1875 22.3125 43.546875 
Q 18.109375 38.921875 18.109375 30.90625 
L 18.109375 0 
L 9.078125 0 
L 9.078125 75.984375 
L 18.109375 75.984375 
L 18.109375 46.1875 
Q 21.34375 51.125 25.703125 53.5625 
Q 30.078125 56 35.796875 56 
Q 45.21875 56 50.046875 50.171875 
Q 54.890625 44.34375 54.890625 33.015625 
z
" id="DejaVuSans-104"/>
       <path d="M 9.421875 54.6875 
L 18.40625 54.6875 
L 18.40625 0 
L 9.421875 0 
z
M 9.421875 75.984375 
L 18.40625 75.984375 
L 18.40625 64.59375 
L 9.421875 64.59375 
z
" id="DejaVuSans-105"/>
       <path d="M 54.890625 33.015625 
L 54.890625 0 
L 45.90625 0 
L 45.90625 32.71875 
Q 45.90625 40.484375 42.875 44.328125 
Q 39.84375 48.1875 33.796875 48.1875 
Q 26.515625 48.1875 22.3125 43.546875 
Q 18.109375 38.921875 18.109375 30.90625 
L 18.109375 0 
L 9.078125 0 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.1875 
Q 21.34375 51.125 25.703125 53.5625 
Q 30.078125 56 35.796875 56 
Q 45.21875 56 50.046875 50.171875 
Q 54.890625 44.34375 54.890625 33.015625 
z
" id="DejaVuSans-110"/>
       <path d="M 45.40625 27.984375 
Q 45.40625 37.75 41.375 43.109375 
Q 37.359375 48.484375 30.078125 48.484375 
Q 22.859375 48.484375 18.828125 43.109375 
Q 14.796875 37.75 14.796875 27.984375 
Q 14.796875 18.265625 18.828125 12.890625 
Q 22.859375 7.515625 30.078125 7.515625 
Q 37.359375 7.515625 41.375 12.890625 
Q 45.40625 18.265625 45.40625 27.984375 
z
M 54.390625 6.78125 
Q 54.390625 -7.171875 48.1875 -13.984375 
Q 42 -20.796875 29.203125 -20.796875 
Q 24.46875 -20.796875 20.265625 -20.09375 
Q 16.0625 -19.390625 12.109375 -17.921875 
L 12.109375 -9.1875 
Q 16.0625 -11.328125 19.921875 -12.34375 
Q 23.78125 -13.375 27.78125 -13.375 
Q 36.625 -13.375 41.015625 -8.765625 
Q 45.40625 -4.15625 45.40625 5.171875 
L 45.40625 9.625 
Q 42.625 4.78125 38.28125 2.390625 
Q 33.9375 0 27.875 0 
Q 17.828125 0 11.671875 7.65625 
Q 5.515625 15.328125 5.515625 27.984375 
Q 5.515625 40.671875 11.671875 48.328125 
Q 17.828125 56 27.875 56 
Q 33.9375 56 38.28125 53.609375 
Q 42.625 51.21875 45.40625 46.390625 
L 45.40625 54.6875 
L 54.390625 54.6875 
z
" id="DejaVuSans-103"/>
       <path id="DejaVuSans-32"/>
       <path d="M 19.671875 64.796875 
L 19.671875 37.40625 
L 32.078125 37.40625 
Q 38.96875 37.40625 42.71875 40.96875 
Q 46.484375 44.53125 46.484375 51.125 
Q 46.484375 57.671875 42.71875 61.234375 
Q 38.96875 64.796875 32.078125 64.796875 
z
M 9.8125 72.90625 
L 32.078125 72.90625 
Q 44.34375 72.90625 50.609375 67.359375 
Q 56.890625 61.8125 56.890625 51.125 
Q 56.890625 40.328125 50.609375 34.8125 
Q 44.34375 29.296875 32.078125 29.296875 
L 19.671875 29.296875 
L 19.671875 0 
L 9.8125 0 
z
" id="DejaVuSans-80"/>
       <path d="M 30.609375 48.390625 
Q 23.390625 48.390625 19.1875 42.75 
Q 14.984375 37.109375 14.984375 27.296875 
Q 14.984375 17.484375 19.15625 11.84375 
Q 23.34375 6.203125 30.609375 6.203125 
Q 37.796875 6.203125 41.984375 11.859375 
Q 46.1875 17.53125 46.1875 27.296875 
Q 46.1875 37.015625 41.984375 42.703125 
Q 37.796875 48.390625 30.609375 48.390625 
z
M 30.609375 56 
Q 42.328125 56 49.015625 48.375 
Q 55.71875 40.765625 55.71875 27.296875 
Q 55.71875 13.875 49.015625 6.21875 
Q 42.328125 -1.421875 30.609375 -1.421875 
Q 18.84375 -1.421875 12.171875 6.21875 
Q 5.515625 13.875 5.515625 27.296875 
Q 5.515625 40.765625 12.171875 48.375 
Q 18.84375 56 30.609375 56 
z
" id="DejaVuSans-111"/>
       <path d="M 48.6875 27.296875 
Q 48.6875 37.203125 44.609375 42.84375 
Q 40.53125 48.484375 33.40625 48.484375 
Q 26.265625 48.484375 22.1875 42.84375 
Q 18.109375 37.203125 18.109375 27.296875 
Q 18.109375 17.390625 22.1875 11.75 
Q 26.265625 6.109375 33.40625 6.109375 
Q 40.53125 6.109375 44.609375 11.75 
Q 48.6875 17.390625 48.6875 27.296875 
z
M 18.109375 46.390625 
Q 20.953125 51.265625 25.265625 53.625 
Q 29.59375 56 35.59375 56 
Q 45.5625 56 51.78125 48.09375 
Q 58.015625 40.1875 58.015625 27.296875 
Q 58.015625 14.40625 51.78125 6.484375 
Q 45.5625 -1.421875 35.59375 -1.421875 
Q 29.59375 -1.421875 25.265625 0.953125 
Q 20.953125 3.328125 18.109375 8.203125 
L 18.109375 0 
L 9.078125 0 
L 9.078125 75.984375 
L 18.109375 75.984375 
z
" id="DejaVuSans-98"/>
       <path d="M 9.421875 75.984375 
L 18.40625 75.984375 
L 18.40625 0 
L 9.421875 0 
z
" id="DejaVuSans-108"/>
       <path d="M 52 44.1875 
Q 55.375 50.25 60.0625 53.125 
Q 64.75 56 71.09375 56 
Q 79.640625 56 84.28125 50.015625 
Q 88.921875 44.046875 88.921875 33.015625 
L 88.921875 0 
L 79.890625 0 
L 79.890625 32.71875 
Q 79.890625 40.578125 77.09375 44.375 
Q 74.3125 48.1875 68.609375 48.1875 
Q 61.625 48.1875 57.5625 43.546875 
Q 53.515625 38.921875 53.515625 30.90625 
L 53.515625 0 
L 44.484375 0 
L 44.484375 32.71875 
Q 44.484375 40.625 41.703125 44.40625 
Q 38.921875 48.1875 33.109375 48.1875 
Q 26.21875 48.1875 22.15625 43.53125 
Q 18.109375 38.875 18.109375 30.90625 
L 18.109375 0 
L 9.078125 0 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.1875 
Q 21.1875 51.21875 25.484375 53.609375 
Q 29.78125 56 35.6875 56 
Q 41.65625 56 45.828125 52.96875 
Q 50 49.953125 52 44.1875 
z
" id="DejaVuSans-109"/>
      </defs>
      <g transform="translate(53.992188 247.23993)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-66"/>
       <use x="68.603516" xlink:href="#DejaVuSans-114"/>
       <use x="107.466797" xlink:href="#DejaVuSans-101"/>
       <use x="168.990234" xlink:href="#DejaVuSans-97"/>
       <use x="230.269531" xlink:href="#DejaVuSans-116"/>
       <use x="269.478516" xlink:href="#DejaVuSans-104"/>
       <use x="332.857422" xlink:href="#DejaVuSans-105"/>
       <use x="360.640625" xlink:href="#DejaVuSans-110"/>
       <use x="424.019531" xlink:href="#DejaVuSans-103"/>
       <use x="487.496094" xlink:href="#DejaVuSans-32"/>
       <use x="519.283203" xlink:href="#DejaVuSans-80"/>
       <use x="577.835938" xlink:href="#DejaVuSans-114"/>
       <use x="616.699219" xlink:href="#DejaVuSans-111"/>
       <use x="677.880859" xlink:href="#DejaVuSans-98"/>
       <use x="741.357422" xlink:href="#DejaVuSans-108"/>
       <use x="769.140625" xlink:href="#DejaVuSans-101"/>
       <use x="830.664062" xlink:href="#DejaVuSans-109"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_10">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="228.065217"/>
      </g>
     </g>
     <g id="text_10">
      <!-- Fever -->
      <defs>
       <path d="M 9.8125 72.90625 
L 51.703125 72.90625 
L 51.703125 64.59375 
L 19.671875 64.59375 
L 19.671875 43.109375 
L 48.578125 43.109375 
L 48.578125 34.8125 
L 19.671875 34.8125 
L 19.671875 0 
L 9.8125 0 
z
" id="DejaVuSans-70"/>
       <path d="M 2.984375 54.6875 
L 12.5 54.6875 
L 29.59375 8.796875 
L 46.6875 54.6875 
L 56.203125 54.6875 
L 35.6875 0 
L 23.484375 0 
z
" id="DejaVuSans-118"/>
      </defs>
      <g transform="translate(119.2625 231.864436)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-70"/>
       <use x="52.019531" xlink:href="#DejaVuSans-101"/>
       <use x="113.542969" xlink:href="#DejaVuSans-118"/>
       <use x="172.722656" xlink:href="#DejaVuSans-101"/>
       <use x="234.246094" xlink:href="#DejaVuSans-114"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_11">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="212.689723"/>
      </g>
     </g>
     <g id="text_11">
      <!-- Dry Cough -->
      <defs>
       <path d="M 19.671875 64.796875 
L 19.671875 8.109375 
L 31.59375 8.109375 
Q 46.6875 8.109375 53.6875 14.9375 
Q 60.6875 21.78125 60.6875 36.53125 
Q 60.6875 51.171875 53.6875 57.984375 
Q 46.6875 64.796875 31.59375 64.796875 
z
M 9.8125 72.90625 
L 30.078125 72.90625 
Q 51.265625 72.90625 61.171875 64.09375 
Q 71.09375 55.28125 71.09375 36.53125 
Q 71.09375 17.671875 61.125 8.828125 
Q 51.171875 0 30.078125 0 
L 9.8125 0 
z
" id="DejaVuSans-68"/>
       <path d="M 32.171875 -5.078125 
Q 28.375 -14.84375 24.75 -17.8125 
Q 21.140625 -20.796875 15.09375 -20.796875 
L 7.90625 -20.796875 
L 7.90625 -13.28125 
L 13.1875 -13.28125 
Q 16.890625 -13.28125 18.9375 -11.515625 
Q 21 -9.765625 23.484375 -3.21875 
L 25.09375 0.875 
L 2.984375 54.6875 
L 12.5 54.6875 
L 29.59375 11.921875 
L 46.6875 54.6875 
L 56.203125 54.6875 
z
" id="DejaVuSans-121"/>
       <path d="M 64.40625 67.28125 
L 64.40625 56.890625 
Q 59.421875 61.53125 53.78125 63.8125 
Q 48.140625 66.109375 41.796875 66.109375 
Q 29.296875 66.109375 22.65625 58.46875 
Q 16.015625 50.828125 16.015625 36.375 
Q 16.015625 21.96875 22.65625 14.328125 
Q 29.296875 6.6875 41.796875 6.6875 
Q 48.140625 6.6875 53.78125 8.984375 
Q 59.421875 11.28125 64.40625 15.921875 
L 64.40625 5.609375 
Q 59.234375 2.09375 53.4375 0.328125 
Q 47.65625 -1.421875 41.21875 -1.421875 
Q 24.65625 -1.421875 15.125 8.703125 
Q 5.609375 18.84375 5.609375 36.375 
Q 5.609375 53.953125 15.125 64.078125 
Q 24.65625 74.21875 41.21875 74.21875 
Q 47.75 74.21875 53.53125 72.484375 
Q 59.328125 70.75 64.40625 67.28125 
z
" id="DejaVuSans-67"/>
       <path d="M 8.5 21.578125 
L 8.5 54.6875 
L 17.484375 54.6875 
L 17.484375 21.921875 
Q 17.484375 14.15625 20.5 10.265625 
Q 23.53125 6.390625 29.59375 6.390625 
Q 36.859375 6.390625 41.078125 11.03125 
Q 45.3125 15.671875 45.3125 23.6875 
L 45.3125 54.6875 
L 54.296875 54.6875 
L 54.296875 0 
L 45.3125 0 
L 45.3125 8.40625 
Q 42.046875 3.421875 37.71875 1 
Q 33.40625 -1.421875 27.6875 -1.421875 
Q 18.265625 -1.421875 13.375 4.4375 
Q 8.5 10.296875 8.5 21.578125 
z
M 31.109375 56 
z
" id="DejaVuSans-117"/>
      </defs>
      <g transform="translate(93.767188 216.488942)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-68"/>
       <use x="77.001953" xlink:href="#DejaVuSans-114"/>
       <use x="118.115234" xlink:href="#DejaVuSans-121"/>
       <use x="177.294922" xlink:href="#DejaVuSans-32"/>
       <use x="209.082031" xlink:href="#DejaVuSans-67"/>
       <use x="278.90625" xlink:href="#DejaVuSans-111"/>
       <use x="340.087891" xlink:href="#DejaVuSans-117"/>
       <use x="403.466797" xlink:href="#DejaVuSans-103"/>
       <use x="466.943359" xlink:href="#DejaVuSans-104"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_12">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="197.314229"/>
      </g>
     </g>
     <g id="text_12">
      <!-- Sore throat -->
      <defs>
       <path d="M 53.515625 70.515625 
L 53.515625 60.890625 
Q 47.90625 63.578125 42.921875 64.890625 
Q 37.9375 66.21875 33.296875 66.21875 
Q 25.25 66.21875 20.875 63.09375 
Q 16.5 59.96875 16.5 54.203125 
Q 16.5 49.359375 19.40625 46.890625 
Q 22.3125 44.4375 30.421875 42.921875 
L 36.375 41.703125 
Q 47.40625 39.59375 52.65625 34.296875 
Q 57.90625 29 57.90625 20.125 
Q 57.90625 9.515625 50.796875 4.046875 
Q 43.703125 -1.421875 29.984375 -1.421875 
Q 24.8125 -1.421875 18.96875 -0.25 
Q 13.140625 0.921875 6.890625 3.21875 
L 6.890625 13.375 
Q 12.890625 10.015625 18.65625 8.296875 
Q 24.421875 6.59375 29.984375 6.59375 
Q 38.421875 6.59375 43.015625 9.90625 
Q 47.609375 13.234375 47.609375 19.390625 
Q 47.609375 24.75 44.3125 27.78125 
Q 41.015625 30.8125 33.5 32.328125 
L 27.484375 33.5 
Q 16.453125 35.6875 11.515625 40.375 
Q 6.59375 45.0625 6.59375 53.421875 
Q 6.59375 63.09375 13.40625 68.65625 
Q 20.21875 74.21875 32.171875 74.21875 
Q 37.3125 74.21875 42.625 73.28125 
Q 47.953125 72.359375 53.515625 70.515625 
z
" id="DejaVuSans-83"/>
      </defs>
      <g transform="translate(90.804688 201.113448)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-83"/>
       <use x="63.476562" xlink:href="#DejaVuSans-111"/>
       <use x="124.658203" xlink:href="#DejaVuSans-114"/>
       <use x="163.521484" xlink:href="#DejaVuSans-101"/>
       <use x="225.044922" xlink:href="#DejaVuSans-32"/>
       <use x="256.832031" xlink:href="#DejaVuSans-116"/>
       <use x="296.041016" xlink:href="#DejaVuSans-104"/>
       <use x="359.419922" xlink:href="#DejaVuSans-114"/>
       <use x="398.283203" xlink:href="#DejaVuSans-111"/>
       <use x="459.464844" xlink:href="#DejaVuSans-97"/>
       <use x="520.744141" xlink:href="#DejaVuSans-116"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_13">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="181.938735"/>
      </g>
     </g>
     <g id="text_13">
      <!-- Running Nose -->
      <defs>
       <path d="M 44.390625 34.1875 
Q 47.5625 33.109375 50.5625 29.59375 
Q 53.5625 26.078125 56.59375 19.921875 
L 66.609375 0 
L 56 0 
L 46.6875 18.703125 
Q 43.0625 26.03125 39.671875 28.421875 
Q 36.28125 30.8125 30.421875 30.8125 
L 19.671875 30.8125 
L 19.671875 0 
L 9.8125 0 
L 9.8125 72.90625 
L 32.078125 72.90625 
Q 44.578125 72.90625 50.734375 67.671875 
Q 56.890625 62.453125 56.890625 51.90625 
Q 56.890625 45.015625 53.6875 40.46875 
Q 50.484375 35.9375 44.390625 34.1875 
z
M 19.671875 64.796875 
L 19.671875 38.921875 
L 32.078125 38.921875 
Q 39.203125 38.921875 42.84375 42.21875 
Q 46.484375 45.515625 46.484375 51.90625 
Q 46.484375 58.296875 42.84375 61.546875 
Q 39.203125 64.796875 32.078125 64.796875 
z
" id="DejaVuSans-82"/>
       <path d="M 9.8125 72.90625 
L 23.09375 72.90625 
L 55.421875 11.921875 
L 55.421875 72.90625 
L 64.984375 72.90625 
L 64.984375 0 
L 51.703125 0 
L 19.390625 60.984375 
L 19.390625 0 
L 9.8125 0 
z
" id="DejaVuSans-78"/>
       <path d="M 44.28125 53.078125 
L 44.28125 44.578125 
Q 40.484375 46.53125 36.375 47.5 
Q 32.28125 48.484375 27.875 48.484375 
Q 21.1875 48.484375 17.84375 46.4375 
Q 14.5 44.390625 14.5 40.28125 
Q 14.5 37.15625 16.890625 35.375 
Q 19.28125 33.59375 26.515625 31.984375 
L 29.59375 31.296875 
Q 39.15625 29.25 43.1875 25.515625 
Q 47.21875 21.78125 47.21875 15.09375 
Q 47.21875 7.46875 41.1875 3.015625 
Q 35.15625 -1.421875 24.609375 -1.421875 
Q 20.21875 -1.421875 15.453125 -0.5625 
Q 10.6875 0.296875 5.421875 2 
L 5.421875 11.28125 
Q 10.40625 8.6875 15.234375 7.390625 
Q 20.0625 6.109375 24.8125 6.109375 
Q 31.15625 6.109375 34.5625 8.28125 
Q 37.984375 10.453125 37.984375 14.40625 
Q 37.984375 18.0625 35.515625 20.015625 
Q 33.0625 21.96875 24.703125 23.78125 
L 21.578125 24.515625 
Q 13.234375 26.265625 9.515625 29.90625 
Q 5.8125 33.546875 5.8125 39.890625 
Q 5.8125 47.609375 11.28125 51.796875 
Q 16.75 56 26.8125 56 
Q 31.78125 56 36.171875 55.265625 
Q 40.578125 54.546875 44.28125 53.078125 
z
" id="DejaVuSans-115"/>
      </defs>
      <g transform="translate(77.684375 185.737954)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-82"/>
       <use x="64.982422" xlink:href="#DejaVuSans-117"/>
       <use x="128.361328" xlink:href="#DejaVuSans-110"/>
       <use x="191.740234" xlink:href="#DejaVuSans-110"/>
       <use x="255.119141" xlink:href="#DejaVuSans-105"/>
       <use x="282.902344" xlink:href="#DejaVuSans-110"/>
       <use x="346.28125" xlink:href="#DejaVuSans-103"/>
       <use x="409.757812" xlink:href="#DejaVuSans-32"/>
       <use x="441.544922" xlink:href="#DejaVuSans-78"/>
       <use x="516.349609" xlink:href="#DejaVuSans-111"/>
       <use x="577.53125" xlink:href="#DejaVuSans-115"/>
       <use x="629.630859" xlink:href="#DejaVuSans-101"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_14">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="166.563241"/>
      </g>
     </g>
     <g id="text_14">
      <!-- Asthma -->
      <defs>
       <path d="M 34.1875 63.1875 
L 20.796875 26.90625 
L 47.609375 26.90625 
z
M 28.609375 72.90625 
L 39.796875 72.90625 
L 67.578125 0 
L 57.328125 0 
L 50.6875 18.703125 
L 17.828125 18.703125 
L 11.1875 0 
L 0.78125 0 
z
" id="DejaVuSans-65"/>
      </defs>
      <g transform="translate(108.623438 170.36246)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-65"/>
       <use x="68.408203" xlink:href="#DejaVuSans-115"/>
       <use x="120.507812" xlink:href="#DejaVuSans-116"/>
       <use x="159.716797" xlink:href="#DejaVuSans-104"/>
       <use x="223.095703" xlink:href="#DejaVuSans-109"/>
       <use x="320.507812" xlink:href="#DejaVuSans-97"/>
      </g>
     </g>
    </g>
    <g id="ytick_7">
     <g id="line2d_15">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="151.187747"/>
      </g>
     </g>
     <g id="text_15">
      <!-- Chronic Lung Disease -->
      <defs>
       <path d="M 48.78125 52.59375 
L 48.78125 44.1875 
Q 44.96875 46.296875 41.140625 47.34375 
Q 37.3125 48.390625 33.40625 48.390625 
Q 24.65625 48.390625 19.8125 42.84375 
Q 14.984375 37.3125 14.984375 27.296875 
Q 14.984375 17.28125 19.8125 11.734375 
Q 24.65625 6.203125 33.40625 6.203125 
Q 37.3125 6.203125 41.140625 7.25 
Q 44.96875 8.296875 48.78125 10.40625 
L 48.78125 2.09375 
Q 45.015625 0.34375 40.984375 -0.53125 
Q 36.96875 -1.421875 32.421875 -1.421875 
Q 20.0625 -1.421875 12.78125 6.34375 
Q 5.515625 14.109375 5.515625 27.296875 
Q 5.515625 40.671875 12.859375 48.328125 
Q 20.21875 56 33.015625 56 
Q 37.15625 56 41.109375 55.140625 
Q 45.0625 54.296875 48.78125 52.59375 
z
" id="DejaVuSans-99"/>
       <path d="M 9.8125 72.90625 
L 19.671875 72.90625 
L 19.671875 8.296875 
L 55.171875 8.296875 
L 55.171875 0 
L 9.8125 0 
z
" id="DejaVuSans-76"/>
      </defs>
      <g transform="translate(38.753125 154.986966)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-67"/>
       <use x="69.824219" xlink:href="#DejaVuSans-104"/>
       <use x="133.203125" xlink:href="#DejaVuSans-114"/>
       <use x="172.066406" xlink:href="#DejaVuSans-111"/>
       <use x="233.248047" xlink:href="#DejaVuSans-110"/>
       <use x="296.626953" xlink:href="#DejaVuSans-105"/>
       <use x="324.410156" xlink:href="#DejaVuSans-99"/>
       <use x="379.390625" xlink:href="#DejaVuSans-32"/>
       <use x="411.177734" xlink:href="#DejaVuSans-76"/>
       <use x="465.140625" xlink:href="#DejaVuSans-117"/>
       <use x="528.519531" xlink:href="#DejaVuSans-110"/>
       <use x="591.898438" xlink:href="#DejaVuSans-103"/>
       <use x="655.375" xlink:href="#DejaVuSans-32"/>
       <use x="687.162109" xlink:href="#DejaVuSans-68"/>
       <use x="764.164062" xlink:href="#DejaVuSans-105"/>
       <use x="791.947266" xlink:href="#DejaVuSans-115"/>
       <use x="844.046875" xlink:href="#DejaVuSans-101"/>
       <use x="905.570312" xlink:href="#DejaVuSans-97"/>
       <use x="966.849609" xlink:href="#DejaVuSans-115"/>
       <use x="1018.949219" xlink:href="#DejaVuSans-101"/>
      </g>
     </g>
    </g>
    <g id="ytick_8">
     <g id="line2d_16">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="135.812253"/>
      </g>
     </g>
     <g id="text_16">
      <!-- Headache -->
      <defs>
       <path d="M 9.8125 72.90625 
L 19.671875 72.90625 
L 19.671875 43.015625 
L 55.515625 43.015625 
L 55.515625 72.90625 
L 65.375 72.90625 
L 65.375 0 
L 55.515625 0 
L 55.515625 34.71875 
L 19.671875 34.71875 
L 19.671875 0 
L 9.8125 0 
z
" id="DejaVuSans-72"/>
       <path d="M 45.40625 46.390625 
L 45.40625 75.984375 
L 54.390625 75.984375 
L 54.390625 0 
L 45.40625 0 
L 45.40625 8.203125 
Q 42.578125 3.328125 38.25 0.953125 
Q 33.9375 -1.421875 27.875 -1.421875 
Q 17.96875 -1.421875 11.734375 6.484375 
Q 5.515625 14.40625 5.515625 27.296875 
Q 5.515625 40.1875 11.734375 48.09375 
Q 17.96875 56 27.875 56 
Q 33.9375 56 38.25 53.625 
Q 42.578125 51.265625 45.40625 46.390625 
z
M 14.796875 27.296875 
Q 14.796875 17.390625 18.875 11.75 
Q 22.953125 6.109375 30.078125 6.109375 
Q 37.203125 6.109375 41.296875 11.75 
Q 45.40625 17.390625 45.40625 27.296875 
Q 45.40625 37.203125 41.296875 42.84375 
Q 37.203125 48.484375 30.078125 48.484375 
Q 22.953125 48.484375 18.875 42.84375 
Q 14.796875 37.203125 14.796875 27.296875 
z
" id="DejaVuSans-100"/>
      </defs>
      <g transform="translate(96.532813 139.611472)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-72"/>
       <use x="75.195312" xlink:href="#DejaVuSans-101"/>
       <use x="136.71875" xlink:href="#DejaVuSans-97"/>
       <use x="197.998047" xlink:href="#DejaVuSans-100"/>
       <use x="261.474609" xlink:href="#DejaVuSans-97"/>
       <use x="322.753906" xlink:href="#DejaVuSans-99"/>
       <use x="377.734375" xlink:href="#DejaVuSans-104"/>
       <use x="441.113281" xlink:href="#DejaVuSans-101"/>
      </g>
     </g>
    </g>
    <g id="ytick_9">
     <g id="line2d_17">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="120.436759"/>
      </g>
     </g>
     <g id="text_17">
      <!-- Heart Disease -->
      <g transform="translate(76.457813 124.235978)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-72"/>
       <use x="75.195312" xlink:href="#DejaVuSans-101"/>
       <use x="136.71875" xlink:href="#DejaVuSans-97"/>
       <use x="197.998047" xlink:href="#DejaVuSans-114"/>
       <use x="239.111328" xlink:href="#DejaVuSans-116"/>
       <use x="278.320312" xlink:href="#DejaVuSans-32"/>
       <use x="310.107422" xlink:href="#DejaVuSans-68"/>
       <use x="387.109375" xlink:href="#DejaVuSans-105"/>
       <use x="414.892578" xlink:href="#DejaVuSans-115"/>
       <use x="466.992188" xlink:href="#DejaVuSans-101"/>
       <use x="528.515625" xlink:href="#DejaVuSans-97"/>
       <use x="589.794922" xlink:href="#DejaVuSans-115"/>
       <use x="641.894531" xlink:href="#DejaVuSans-101"/>
      </g>
     </g>
    </g>
    <g id="ytick_10">
     <g id="line2d_18">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="105.061265"/>
      </g>
     </g>
     <g id="text_18">
      <!-- Diabetes -->
      <g transform="translate(102.409375 108.860484)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-68"/>
       <use x="77.001953" xlink:href="#DejaVuSans-105"/>
       <use x="104.785156" xlink:href="#DejaVuSans-97"/>
       <use x="166.064453" xlink:href="#DejaVuSans-98"/>
       <use x="229.541016" xlink:href="#DejaVuSans-101"/>
       <use x="291.064453" xlink:href="#DejaVuSans-116"/>
       <use x="330.273438" xlink:href="#DejaVuSans-101"/>
       <use x="391.796875" xlink:href="#DejaVuSans-115"/>
      </g>
     </g>
    </g>
    <g id="ytick_11">
     <g id="line2d_19">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="89.685771"/>
      </g>
     </g>
     <g id="text_19">
      <!-- Hyper Tension -->
      <defs>
       <path d="M 18.109375 8.203125 
L 18.109375 -20.796875 
L 9.078125 -20.796875 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.390625 
Q 20.953125 51.265625 25.265625 53.625 
Q 29.59375 56 35.59375 56 
Q 45.5625 56 51.78125 48.09375 
Q 58.015625 40.1875 58.015625 27.296875 
Q 58.015625 14.40625 51.78125 6.484375 
Q 45.5625 -1.421875 35.59375 -1.421875 
Q 29.59375 -1.421875 25.265625 0.953125 
Q 20.953125 3.328125 18.109375 8.203125 
z
M 48.6875 27.296875 
Q 48.6875 37.203125 44.609375 42.84375 
Q 40.53125 48.484375 33.40625 48.484375 
Q 26.265625 48.484375 22.1875 42.84375 
Q 18.109375 37.203125 18.109375 27.296875 
Q 18.109375 17.390625 22.1875 11.75 
Q 26.265625 6.109375 33.40625 6.109375 
Q 40.53125 6.109375 44.609375 11.75 
Q 48.6875 17.390625 48.6875 27.296875 
z
" id="DejaVuSans-112"/>
       <path d="M -0.296875 72.90625 
L 61.375 72.90625 
L 61.375 64.59375 
L 35.5 64.59375 
L 35.5 0 
L 25.59375 0 
L 25.59375 64.59375 
L -0.296875 64.59375 
z
" id="DejaVuSans-84"/>
      </defs>
      <g transform="translate(76.228125 93.48499)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-72"/>
       <use x="75.195312" xlink:href="#DejaVuSans-121"/>
       <use x="134.375" xlink:href="#DejaVuSans-112"/>
       <use x="197.851562" xlink:href="#DejaVuSans-101"/>
       <use x="259.375" xlink:href="#DejaVuSans-114"/>
       <use x="300.488281" xlink:href="#DejaVuSans-32"/>
       <use x="332.275391" xlink:href="#DejaVuSans-84"/>
       <use x="376.359375" xlink:href="#DejaVuSans-101"/>
       <use x="437.882812" xlink:href="#DejaVuSans-110"/>
       <use x="501.261719" xlink:href="#DejaVuSans-115"/>
       <use x="553.361328" xlink:href="#DejaVuSans-105"/>
       <use x="581.144531" xlink:href="#DejaVuSans-111"/>
       <use x="642.326172" xlink:href="#DejaVuSans-110"/>
      </g>
     </g>
    </g>
    <g id="ytick_12">
     <g id="line2d_20">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="74.310277"/>
      </g>
     </g>
     <g id="text_20">
      <!-- Fatigue  -->
      <g transform="translate(107.117188 78.109495)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-70"/>
       <use x="48.394531" xlink:href="#DejaVuSans-97"/>
       <use x="109.673828" xlink:href="#DejaVuSans-116"/>
       <use x="148.882812" xlink:href="#DejaVuSans-105"/>
       <use x="176.666016" xlink:href="#DejaVuSans-103"/>
       <use x="240.142578" xlink:href="#DejaVuSans-117"/>
       <use x="303.521484" xlink:href="#DejaVuSans-101"/>
       <use x="365.044922" xlink:href="#DejaVuSans-32"/>
      </g>
     </g>
    </g>
    <g id="ytick_13">
     <g id="line2d_21">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="58.934783"/>
      </g>
     </g>
     <g id="text_21">
      <!-- Abroad travel -->
      <g transform="translate(78.942188 62.734001)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-65"/>
       <use x="68.408203" xlink:href="#DejaVuSans-98"/>
       <use x="131.884766" xlink:href="#DejaVuSans-114"/>
       <use x="170.748047" xlink:href="#DejaVuSans-111"/>
       <use x="231.929688" xlink:href="#DejaVuSans-97"/>
       <use x="293.208984" xlink:href="#DejaVuSans-100"/>
       <use x="356.685547" xlink:href="#DejaVuSans-32"/>
       <use x="388.472656" xlink:href="#DejaVuSans-116"/>
       <use x="427.681641" xlink:href="#DejaVuSans-114"/>
       <use x="468.794922" xlink:href="#DejaVuSans-97"/>
       <use x="530.074219" xlink:href="#DejaVuSans-118"/>
       <use x="589.253906" xlink:href="#DejaVuSans-101"/>
       <use x="650.777344" xlink:href="#DejaVuSans-108"/>
      </g>
     </g>
    </g>
    <g id="ytick_14">
     <g id="line2d_22">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="153.8" xlink:href="#m819bcadd00" y="43.559289"/>
      </g>
     </g>
     <g id="text_22">
      <!-- Contact with COVID Patient -->
      <defs>
       <path d="M 4.203125 54.6875 
L 13.1875 54.6875 
L 24.421875 12.015625 
L 35.59375 54.6875 
L 46.1875 54.6875 
L 57.421875 12.015625 
L 68.609375 54.6875 
L 77.59375 54.6875 
L 63.28125 0 
L 52.6875 0 
L 40.921875 44.828125 
L 29.109375 0 
L 18.5 0 
z
" id="DejaVuSans-119"/>
       <path d="M 39.40625 66.21875 
Q 28.65625 66.21875 22.328125 58.203125 
Q 16.015625 50.203125 16.015625 36.375 
Q 16.015625 22.609375 22.328125 14.59375 
Q 28.65625 6.59375 39.40625 6.59375 
Q 50.140625 6.59375 56.421875 14.59375 
Q 62.703125 22.609375 62.703125 36.375 
Q 62.703125 50.203125 56.421875 58.203125 
Q 50.140625 66.21875 39.40625 66.21875 
z
M 39.40625 74.21875 
Q 54.734375 74.21875 63.90625 63.9375 
Q 73.09375 53.65625 73.09375 36.375 
Q 73.09375 19.140625 63.90625 8.859375 
Q 54.734375 -1.421875 39.40625 -1.421875 
Q 24.03125 -1.421875 14.8125 8.828125 
Q 5.609375 19.09375 5.609375 36.375 
Q 5.609375 53.65625 14.8125 63.9375 
Q 24.03125 74.21875 39.40625 74.21875 
z
" id="DejaVuSans-79"/>
       <path d="M 28.609375 0 
L 0.78125 72.90625 
L 11.078125 72.90625 
L 34.1875 11.53125 
L 57.328125 72.90625 
L 67.578125 72.90625 
L 39.796875 0 
z
" id="DejaVuSans-86"/>
       <path d="M 9.8125 72.90625 
L 19.671875 72.90625 
L 19.671875 0 
L 9.8125 0 
z
" id="DejaVuSans-73"/>
      </defs>
      <g transform="translate(10.157813 47.358507)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-67"/>
       <use x="69.824219" xlink:href="#DejaVuSans-111"/>
       <use x="131.005859" xlink:href="#DejaVuSans-110"/>
       <use x="194.384766" xlink:href="#DejaVuSans-116"/>
       <use x="233.59375" xlink:href="#DejaVuSans-97"/>
       <use x="294.873047" xlink:href="#DejaVuSans-99"/>
       <use x="349.853516" xlink:href="#DejaVuSans-116"/>
       <use x="389.0625" xlink:href="#DejaVuSans-32"/>
       <use x="420.849609" xlink:href="#DejaVuSans-119"/>
       <use x="502.636719" xlink:href="#DejaVuSans-105"/>
       <use x="530.419922" xlink:href="#DejaVuSans-116"/>
       <use x="569.628906" xlink:href="#DejaVuSans-104"/>
       <use x="633.007812" xlink:href="#DejaVuSans-32"/>
       <use x="664.794922" xlink:href="#DejaVuSans-67"/>
       <use x="734.619141" xlink:href="#DejaVuSans-79"/>
       <use x="811.580078" xlink:href="#DejaVuSans-86"/>
       <use x="879.988281" xlink:href="#DejaVuSans-73"/>
       <use x="909.480469" xlink:href="#DejaVuSans-68"/>
       <use x="986.482422" xlink:href="#DejaVuSans-32"/>
       <use x="1018.269531" xlink:href="#DejaVuSans-80"/>
       <use x="1074.072266" xlink:href="#DejaVuSans-97"/>
       <use x="1135.351562" xlink:href="#DejaVuSans-116"/>
       <use x="1174.560547" xlink:href="#DejaVuSans-105"/>
       <use x="1202.34375" xlink:href="#DejaVuSans-101"/>
       <use x="1263.867188" xlink:href="#DejaVuSans-110"/>
       <use x="1327.246094" xlink:href="#DejaVuSans-116"/>
      </g>
     </g>
    </g>
   </g>
   <g id="patch_17">
    <path d="M 153.8 260.2 
L 153.8 26.8 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="patch_18">
    <path d="M 418.023087 260.2 
L 418.023087 26.8 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="patch_19">
    <path d="M 153.8 260.2 
L 418.023087 260.2 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="patch_20">
    <path d="M 153.8 26.8 
L 418.023087 26.8 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="text_23">
    <!-- Feature Importances -->
    <g transform="translate(223.827481 20.8)scale(0.12 -0.12)">
     <use xlink:href="#DejaVuSans-70"/>
     <use x="52.019531" xlink:href="#DejaVuSans-101"/>
     <use x="113.542969" xlink:href="#DejaVuSans-97"/>
     <use x="174.822266" xlink:href="#DejaVuSans-116"/>
     <use x="214.03125" xlink:href="#DejaVuSans-117"/>
     <use x="277.410156" xlink:href="#DejaVuSans-114"/>
     <use x="316.273438" xlink:href="#DejaVuSans-101"/>
     <use x="377.796875" xlink:href="#DejaVuSans-32"/>
     <use x="409.583984" xlink:href="#DejaVuSans-73"/>
     <use x="439.076172" xlink:href="#DejaVuSans-109"/>
     <use x="536.488281" xlink:href="#DejaVuSans-112"/>
     <use x="599.964844" xlink:href="#DejaVuSans-111"/>
     <use x="661.146484" xlink:href="#DejaVuSans-114"/>
     <use x="702.259766" xlink:href="#DejaVuSans-116"/>
     <use x="741.46875" xlink:href="#DejaVuSans-97"/>
     <use x="802.748047" xlink:href="#DejaVuSans-110"/>
     <use x="866.126953" xlink:href="#DejaVuSans-99"/>
     <use x="921.107422" xlink:href="#DejaVuSans-101"/>
     <use x="982.630859" xlink:href="#DejaVuSans-115"/>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="pf5091c3e1a">
   <rect height="233.4" width="264.223087" x="153.8" y="26.8"/>
  </clipPath>
 </defs>
</svg>













![result1](https://github.com/aadarshgupta1412/covid-symptoms-classification/assets/62350692/0584c821-6654-4f06-b0a9-d071090270db)
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (https://matplotlib.org/) -->
<svg height="288pt" version="1.1" viewBox="0 0 432 288" width="432pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 288 
L 432 288 
L 432 0 
L 0 0 
z
" style="fill:#ffffff;"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 47.55 243.2 
L 421.2 243.2 
L 421.2 28.8 
L 47.55 28.8 
z
" style="fill:#ffffff;"/>
   </g>
   <g id="patch_3">
    <path clip-path="url(#p33d5c294a3)" d="M 64.534091 4102.4 
L 92.263219 4102.4 
L 92.263219 163.872 
L 64.534091 163.872 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_4">
    <path clip-path="url(#p33d5c294a3)" d="M 99.195501 4102.4 
L 126.924629 4102.4 
L 126.924629 154.4384 
L 99.195501 154.4384 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_5">
    <path clip-path="url(#p33d5c294a3)" d="M 133.856911 4102.4 
L 161.586039 4102.4 
L 161.586039 149.7216 
L 133.856911 149.7216 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_6">
    <path clip-path="url(#p33d5c294a3)" d="M 168.518321 4102.4 
L 196.247449 4102.4 
L 196.247449 136.4288 
L 168.518321 136.4288 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_7">
    <path clip-path="url(#p33d5c294a3)" d="M 203.179731 4102.4 
L 230.908859 4102.4 
L 230.908859 165.5872 
L 203.179731 165.5872 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_8">
    <path clip-path="url(#p33d5c294a3)" d="M 237.841141 4102.4 
L 265.570269 4102.4 
L 265.570269 87.5456 
L 237.841141 87.5456 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_9">
    <path clip-path="url(#p33d5c294a3)" d="M 272.502551 4102.4 
L 300.231679 4102.4 
L 300.231679 122.2784 
L 272.502551 122.2784 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_10">
    <path clip-path="url(#p33d5c294a3)" d="M 307.163961 4102.4 
L 334.893089 4102.4 
L 334.893089 100.8384 
L 307.163961 100.8384 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_11">
    <path clip-path="url(#p33d5c294a3)" d="M 341.825371 4102.4 
L 369.554499 4102.4 
L 369.554499 93.9776 
L 341.825371 93.9776 
z
" style="fill:#800080;"/>
   </g>
   <g id="patch_12">
    <path clip-path="url(#p33d5c294a3)" d="M 376.486781 4102.4 
L 404.215909 4102.4 
L 404.215909 97.8368 
L 376.486781 97.8368 
z
" style="fill:#800080;"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <defs>
       <path d="M 0 0 
L 0 3.5 
" id="mc1fce968fa" style="stroke:#000000;stroke-width:0.8;"/>
      </defs>
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="78.398655" xlink:href="#mc1fce968fa" y="243.2"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 2 -->
      <defs>
       <path d="M 19.1875 8.296875 
L 53.609375 8.296875 
L 53.609375 0 
L 7.328125 0 
L 7.328125 8.296875 
Q 12.9375 14.109375 22.625 23.890625 
Q 32.328125 33.6875 34.8125 36.53125 
Q 39.546875 41.84375 41.421875 45.53125 
Q 43.3125 49.21875 43.3125 52.78125 
Q 43.3125 58.59375 39.234375 62.25 
Q 35.15625 65.921875 28.609375 65.921875 
Q 23.96875 65.921875 18.8125 64.3125 
Q 13.671875 62.703125 7.8125 59.421875 
L 7.8125 69.390625 
Q 13.765625 71.78125 18.9375 73 
Q 24.125 74.21875 28.421875 74.21875 
Q 39.75 74.21875 46.484375 68.546875 
Q 53.21875 62.890625 53.21875 53.421875 
Q 53.21875 48.921875 51.53125 44.890625 
Q 49.859375 40.875 45.40625 35.40625 
Q 44.1875 33.984375 37.640625 27.21875 
Q 31.109375 20.453125 19.1875 8.296875 
z
" id="DejaVuSans-50"/>
      </defs>
      <g transform="translate(75.217405 257.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-50"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_2">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="147.721475" xlink:href="#mc1fce968fa" y="243.2"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 4 -->
      <defs>
       <path d="M 37.796875 64.3125 
L 12.890625 25.390625 
L 37.796875 25.390625 
z
M 35.203125 72.90625 
L 47.609375 72.90625 
L 47.609375 25.390625 
L 58.015625 25.390625 
L 58.015625 17.1875 
L 47.609375 17.1875 
L 47.609375 0 
L 37.796875 0 
L 37.796875 17.1875 
L 4.890625 17.1875 
L 4.890625 26.703125 
z
" id="DejaVuSans-52"/>
      </defs>
      <g transform="translate(144.540225 257.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-52"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_3">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="217.044295" xlink:href="#mc1fce968fa" y="243.2"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 6 -->
      <defs>
       <path d="M 33.015625 40.375 
Q 26.375 40.375 22.484375 35.828125 
Q 18.609375 31.296875 18.609375 23.390625 
Q 18.609375 15.53125 22.484375 10.953125 
Q 26.375 6.390625 33.015625 6.390625 
Q 39.65625 6.390625 43.53125 10.953125 
Q 47.40625 15.53125 47.40625 23.390625 
Q 47.40625 31.296875 43.53125 35.828125 
Q 39.65625 40.375 33.015625 40.375 
z
M 52.59375 71.296875 
L 52.59375 62.3125 
Q 48.875 64.0625 45.09375 64.984375 
Q 41.3125 65.921875 37.59375 65.921875 
Q 27.828125 65.921875 22.671875 59.328125 
Q 17.53125 52.734375 16.796875 39.40625 
Q 19.671875 43.65625 24.015625 45.921875 
Q 28.375 48.1875 33.59375 48.1875 
Q 44.578125 48.1875 50.953125 41.515625 
Q 57.328125 34.859375 57.328125 23.390625 
Q 57.328125 12.15625 50.6875 5.359375 
Q 44.046875 -1.421875 33.015625 -1.421875 
Q 20.359375 -1.421875 13.671875 8.265625 
Q 6.984375 17.96875 6.984375 36.375 
Q 6.984375 53.65625 15.1875 63.9375 
Q 23.390625 74.21875 37.203125 74.21875 
Q 40.921875 74.21875 44.703125 73.484375 
Q 48.484375 72.75 52.59375 71.296875 
z
" id="DejaVuSans-54"/>
      </defs>
      <g transform="translate(213.863045 257.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-54"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_4">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="286.367115" xlink:href="#mc1fce968fa" y="243.2"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 8 -->
      <defs>
       <path d="M 31.78125 34.625 
Q 24.75 34.625 20.71875 30.859375 
Q 16.703125 27.09375 16.703125 20.515625 
Q 16.703125 13.921875 20.71875 10.15625 
Q 24.75 6.390625 31.78125 6.390625 
Q 38.8125 6.390625 42.859375 10.171875 
Q 46.921875 13.96875 46.921875 20.515625 
Q 46.921875 27.09375 42.890625 30.859375 
Q 38.875 34.625 31.78125 34.625 
z
M 21.921875 38.8125 
Q 15.578125 40.375 12.03125 44.71875 
Q 8.5 49.078125 8.5 55.328125 
Q 8.5 64.0625 14.71875 69.140625 
Q 20.953125 74.21875 31.78125 74.21875 
Q 42.671875 74.21875 48.875 69.140625 
Q 55.078125 64.0625 55.078125 55.328125 
Q 55.078125 49.078125 51.53125 44.71875 
Q 48 40.375 41.703125 38.8125 
Q 48.828125 37.15625 52.796875 32.3125 
Q 56.78125 27.484375 56.78125 20.515625 
Q 56.78125 9.90625 50.3125 4.234375 
Q 43.84375 -1.421875 31.78125 -1.421875 
Q 19.734375 -1.421875 13.25 4.234375 
Q 6.78125 9.90625 6.78125 20.515625 
Q 6.78125 27.484375 10.78125 32.3125 
Q 14.796875 37.15625 21.921875 38.8125 
z
M 18.3125 54.390625 
Q 18.3125 48.734375 21.84375 45.5625 
Q 25.390625 42.390625 31.78125 42.390625 
Q 38.140625 42.390625 41.71875 45.5625 
Q 45.3125 48.734375 45.3125 54.390625 
Q 45.3125 60.0625 41.71875 63.234375 
Q 38.140625 66.40625 31.78125 66.40625 
Q 25.390625 66.40625 21.84375 63.234375 
Q 18.3125 60.0625 18.3125 54.390625 
z
" id="DejaVuSans-56"/>
      </defs>
      <g transform="translate(283.185865 257.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-56"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_5">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="355.689935" xlink:href="#mc1fce968fa" y="243.2"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 10 -->
      <defs>
       <path d="M 12.40625 8.296875 
L 28.515625 8.296875 
L 28.515625 63.921875 
L 10.984375 60.40625 
L 10.984375 69.390625 
L 28.421875 72.90625 
L 38.28125 72.90625 
L 38.28125 8.296875 
L 54.390625 8.296875 
L 54.390625 0 
L 12.40625 0 
z
" id="DejaVuSans-49"/>
       <path d="M 31.78125 66.40625 
Q 24.171875 66.40625 20.328125 58.90625 
Q 16.5 51.421875 16.5 36.375 
Q 16.5 21.390625 20.328125 13.890625 
Q 24.171875 6.390625 31.78125 6.390625 
Q 39.453125 6.390625 43.28125 13.890625 
Q 47.125 21.390625 47.125 36.375 
Q 47.125 51.421875 43.28125 58.90625 
Q 39.453125 66.40625 31.78125 66.40625 
z
M 31.78125 74.21875 
Q 44.046875 74.21875 50.515625 64.515625 
Q 56.984375 54.828125 56.984375 36.375 
Q 56.984375 17.96875 50.515625 8.265625 
Q 44.046875 -1.421875 31.78125 -1.421875 
Q 19.53125 -1.421875 13.0625 8.265625 
Q 6.59375 17.96875 6.59375 36.375 
Q 6.59375 54.828125 13.0625 64.515625 
Q 19.53125 74.21875 31.78125 74.21875 
z
" id="DejaVuSans-48"/>
      </defs>
      <g transform="translate(349.327435 257.798437)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-49"/>
       <use x="63.623047" xlink:href="#DejaVuSans-48"/>
      </g>
     </g>
    </g>
    <g id="text_6">
     <!-- n_component -->
     <defs>
      <path d="M 54.890625 33.015625 
L 54.890625 0 
L 45.90625 0 
L 45.90625 32.71875 
Q 45.90625 40.484375 42.875 44.328125 
Q 39.84375 48.1875 33.796875 48.1875 
Q 26.515625 48.1875 22.3125 43.546875 
Q 18.109375 38.921875 18.109375 30.90625 
L 18.109375 0 
L 9.078125 0 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.1875 
Q 21.34375 51.125 25.703125 53.5625 
Q 30.078125 56 35.796875 56 
Q 45.21875 56 50.046875 50.171875 
Q 54.890625 44.34375 54.890625 33.015625 
z
" id="DejaVuSans-110"/>
      <path d="M 50.984375 -16.609375 
L 50.984375 -23.578125 
L -0.984375 -23.578125 
L -0.984375 -16.609375 
z
" id="DejaVuSans-95"/>
      <path d="M 48.78125 52.59375 
L 48.78125 44.1875 
Q 44.96875 46.296875 41.140625 47.34375 
Q 37.3125 48.390625 33.40625 48.390625 
Q 24.65625 48.390625 19.8125 42.84375 
Q 14.984375 37.3125 14.984375 27.296875 
Q 14.984375 17.28125 19.8125 11.734375 
Q 24.65625 6.203125 33.40625 6.203125 
Q 37.3125 6.203125 41.140625 7.25 
Q 44.96875 8.296875 48.78125 10.40625 
L 48.78125 2.09375 
Q 45.015625 0.34375 40.984375 -0.53125 
Q 36.96875 -1.421875 32.421875 -1.421875 
Q 20.0625 -1.421875 12.78125 6.34375 
Q 5.515625 14.109375 5.515625 27.296875 
Q 5.515625 40.671875 12.859375 48.328125 
Q 20.21875 56 33.015625 56 
Q 37.15625 56 41.109375 55.140625 
Q 45.0625 54.296875 48.78125 52.59375 
z
" id="DejaVuSans-99"/>
      <path d="M 30.609375 48.390625 
Q 23.390625 48.390625 19.1875 42.75 
Q 14.984375 37.109375 14.984375 27.296875 
Q 14.984375 17.484375 19.15625 11.84375 
Q 23.34375 6.203125 30.609375 6.203125 
Q 37.796875 6.203125 41.984375 11.859375 
Q 46.1875 17.53125 46.1875 27.296875 
Q 46.1875 37.015625 41.984375 42.703125 
Q 37.796875 48.390625 30.609375 48.390625 
z
M 30.609375 56 
Q 42.328125 56 49.015625 48.375 
Q 55.71875 40.765625 55.71875 27.296875 
Q 55.71875 13.875 49.015625 6.21875 
Q 42.328125 -1.421875 30.609375 -1.421875 
Q 18.84375 -1.421875 12.171875 6.21875 
Q 5.515625 13.875 5.515625 27.296875 
Q 5.515625 40.765625 12.171875 48.375 
Q 18.84375 56 30.609375 56 
z
" id="DejaVuSans-111"/>
      <path d="M 52 44.1875 
Q 55.375 50.25 60.0625 53.125 
Q 64.75 56 71.09375 56 
Q 79.640625 56 84.28125 50.015625 
Q 88.921875 44.046875 88.921875 33.015625 
L 88.921875 0 
L 79.890625 0 
L 79.890625 32.71875 
Q 79.890625 40.578125 77.09375 44.375 
Q 74.3125 48.1875 68.609375 48.1875 
Q 61.625 48.1875 57.5625 43.546875 
Q 53.515625 38.921875 53.515625 30.90625 
L 53.515625 0 
L 44.484375 0 
L 44.484375 32.71875 
Q 44.484375 40.625 41.703125 44.40625 
Q 38.921875 48.1875 33.109375 48.1875 
Q 26.21875 48.1875 22.15625 43.53125 
Q 18.109375 38.875 18.109375 30.90625 
L 18.109375 0 
L 9.078125 0 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.1875 
Q 21.1875 51.21875 25.484375 53.609375 
Q 29.78125 56 35.6875 56 
Q 41.65625 56 45.828125 52.96875 
Q 50 49.953125 52 44.1875 
z
" id="DejaVuSans-109"/>
      <path d="M 18.109375 8.203125 
L 18.109375 -20.796875 
L 9.078125 -20.796875 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.390625 
Q 20.953125 51.265625 25.265625 53.625 
Q 29.59375 56 35.59375 56 
Q 45.5625 56 51.78125 48.09375 
Q 58.015625 40.1875 58.015625 27.296875 
Q 58.015625 14.40625 51.78125 6.484375 
Q 45.5625 -1.421875 35.59375 -1.421875 
Q 29.59375 -1.421875 25.265625 0.953125 
Q 20.953125 3.328125 18.109375 8.203125 
z
M 48.6875 27.296875 
Q 48.6875 37.203125 44.609375 42.84375 
Q 40.53125 48.484375 33.40625 48.484375 
Q 26.265625 48.484375 22.1875 42.84375 
Q 18.109375 37.203125 18.109375 27.296875 
Q 18.109375 17.390625 22.1875 11.75 
Q 26.265625 6.109375 33.40625 6.109375 
Q 40.53125 6.109375 44.609375 11.75 
Q 48.6875 17.390625 48.6875 27.296875 
z
" id="DejaVuSans-112"/>
      <path d="M 56.203125 29.59375 
L 56.203125 25.203125 
L 14.890625 25.203125 
Q 15.484375 15.921875 20.484375 11.0625 
Q 25.484375 6.203125 34.421875 6.203125 
Q 39.59375 6.203125 44.453125 7.46875 
Q 49.3125 8.734375 54.109375 11.28125 
L 54.109375 2.78125 
Q 49.265625 0.734375 44.1875 -0.34375 
Q 39.109375 -1.421875 33.890625 -1.421875 
Q 20.796875 -1.421875 13.15625 6.1875 
Q 5.515625 13.8125 5.515625 26.8125 
Q 5.515625 40.234375 12.765625 48.109375 
Q 20.015625 56 32.328125 56 
Q 43.359375 56 49.78125 48.890625 
Q 56.203125 41.796875 56.203125 29.59375 
z
M 47.21875 32.234375 
Q 47.125 39.59375 43.09375 43.984375 
Q 39.0625 48.390625 32.421875 48.390625 
Q 24.90625 48.390625 20.390625 44.140625 
Q 15.875 39.890625 15.1875 32.171875 
z
" id="DejaVuSans-101"/>
      <path d="M 18.3125 70.21875 
L 18.3125 54.6875 
L 36.8125 54.6875 
L 36.8125 47.703125 
L 18.3125 47.703125 
L 18.3125 18.015625 
Q 18.3125 11.328125 20.140625 9.421875 
Q 21.96875 7.515625 27.59375 7.515625 
L 36.8125 7.515625 
L 36.8125 0 
L 27.59375 0 
Q 17.1875 0 13.234375 3.875 
Q 9.28125 7.765625 9.28125 18.015625 
L 9.28125 47.703125 
L 2.6875 47.703125 
L 2.6875 54.6875 
L 9.28125 54.6875 
L 9.28125 70.21875 
z
" id="DejaVuSans-116"/>
     </defs>
     <g transform="translate(193.628438 272.6625)scale(0.12 -0.12)">
      <use xlink:href="#DejaVuSans-110"/>
      <use x="63.378906" xlink:href="#DejaVuSans-95"/>
      <use x="113.378906" xlink:href="#DejaVuSans-99"/>
      <use x="168.359375" xlink:href="#DejaVuSans-111"/>
      <use x="229.541016" xlink:href="#DejaVuSans-109"/>
      <use x="326.953125" xlink:href="#DejaVuSans-112"/>
      <use x="390.429688" xlink:href="#DejaVuSans-111"/>
      <use x="451.611328" xlink:href="#DejaVuSans-110"/>
      <use x="514.990234" xlink:href="#DejaVuSans-101"/>
      <use x="576.513672" xlink:href="#DejaVuSans-110"/>
      <use x="639.892578" xlink:href="#DejaVuSans-116"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_6">
      <defs>
       <path d="M 0 0 
L -3.5 0 
" id="mbbcd20e83a" style="stroke:#000000;stroke-width:0.8;"/>
      </defs>
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="47.55" xlink:href="#mbbcd20e83a" y="243.2"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 90 -->
      <defs>
       <path d="M 10.984375 1.515625 
L 10.984375 10.5 
Q 14.703125 8.734375 18.5 7.8125 
Q 22.3125 6.890625 25.984375 6.890625 
Q 35.75 6.890625 40.890625 13.453125 
Q 46.046875 20.015625 46.78125 33.40625 
Q 43.953125 29.203125 39.59375 26.953125 
Q 35.25 24.703125 29.984375 24.703125 
Q 19.046875 24.703125 12.671875 31.3125 
Q 6.296875 37.9375 6.296875 49.421875 
Q 6.296875 60.640625 12.9375 67.421875 
Q 19.578125 74.21875 30.609375 74.21875 
Q 43.265625 74.21875 49.921875 64.515625 
Q 56.59375 54.828125 56.59375 36.375 
Q 56.59375 19.140625 48.40625 8.859375 
Q 40.234375 -1.421875 26.421875 -1.421875 
Q 22.703125 -1.421875 18.890625 -0.6875 
Q 15.09375 0.046875 10.984375 1.515625 
z
M 30.609375 32.421875 
Q 37.25 32.421875 41.125 36.953125 
Q 45.015625 41.5 45.015625 49.421875 
Q 45.015625 57.28125 41.125 61.84375 
Q 37.25 66.40625 30.609375 66.40625 
Q 23.96875 66.40625 20.09375 61.84375 
Q 16.21875 57.28125 16.21875 49.421875 
Q 16.21875 41.5 20.09375 36.953125 
Q 23.96875 32.421875 30.609375 32.421875 
z
" id="DejaVuSans-57"/>
      </defs>
      <g transform="translate(27.825 246.999219)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-57"/>
       <use x="63.623047" xlink:href="#DejaVuSans-48"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_7">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="47.55" xlink:href="#mbbcd20e83a" y="200.32"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 91 -->
      <g transform="translate(27.825 204.119219)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-57"/>
       <use x="63.623047" xlink:href="#DejaVuSans-49"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_8">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="47.55" xlink:href="#mbbcd20e83a" y="157.44"/>
      </g>
     </g>
     <g id="text_9">
      <!-- 92 -->
      <g transform="translate(27.825 161.239219)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-57"/>
       <use x="63.623047" xlink:href="#DejaVuSans-50"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_9">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="47.55" xlink:href="#mbbcd20e83a" y="114.56"/>
      </g>
     </g>
     <g id="text_10">
      <!-- 93 -->
      <defs>
       <path d="M 40.578125 39.3125 
Q 47.65625 37.796875 51.625 33 
Q 55.609375 28.21875 55.609375 21.1875 
Q 55.609375 10.40625 48.1875 4.484375 
Q 40.765625 -1.421875 27.09375 -1.421875 
Q 22.515625 -1.421875 17.65625 -0.515625 
Q 12.796875 0.390625 7.625 2.203125 
L 7.625 11.71875 
Q 11.71875 9.328125 16.59375 8.109375 
Q 21.484375 6.890625 26.8125 6.890625 
Q 36.078125 6.890625 40.9375 10.546875 
Q 45.796875 14.203125 45.796875 21.1875 
Q 45.796875 27.640625 41.28125 31.265625 
Q 36.765625 34.90625 28.71875 34.90625 
L 20.21875 34.90625 
L 20.21875 43.015625 
L 29.109375 43.015625 
Q 36.375 43.015625 40.234375 45.921875 
Q 44.09375 48.828125 44.09375 54.296875 
Q 44.09375 59.90625 40.109375 62.90625 
Q 36.140625 65.921875 28.71875 65.921875 
Q 24.65625 65.921875 20.015625 65.03125 
Q 15.375 64.15625 9.8125 62.3125 
L 9.8125 71.09375 
Q 15.4375 72.65625 20.34375 73.4375 
Q 25.25 74.21875 29.59375 74.21875 
Q 40.828125 74.21875 47.359375 69.109375 
Q 53.90625 64.015625 53.90625 55.328125 
Q 53.90625 49.265625 50.4375 45.09375 
Q 46.96875 40.921875 40.578125 39.3125 
z
" id="DejaVuSans-51"/>
      </defs>
      <g transform="translate(27.825 118.359219)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-57"/>
       <use x="63.623047" xlink:href="#DejaVuSans-51"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_10">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="47.55" xlink:href="#mbbcd20e83a" y="71.68"/>
      </g>
     </g>
     <g id="text_11">
      <!-- 94 -->
      <g transform="translate(27.825 75.479219)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-57"/>
       <use x="63.623047" xlink:href="#DejaVuSans-52"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_11">
      <g>
       <use style="stroke:#000000;stroke-width:0.8;" x="47.55" xlink:href="#mbbcd20e83a" y="28.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- 95 -->
      <defs>
       <path d="M 10.796875 72.90625 
L 49.515625 72.90625 
L 49.515625 64.59375 
L 19.828125 64.59375 
L 19.828125 46.734375 
Q 21.96875 47.46875 24.109375 47.828125 
Q 26.265625 48.1875 28.421875 48.1875 
Q 40.625 48.1875 47.75 41.5 
Q 54.890625 34.8125 54.890625 23.390625 
Q 54.890625 11.625 47.5625 5.09375 
Q 40.234375 -1.421875 26.90625 -1.421875 
Q 22.3125 -1.421875 17.546875 -0.640625 
Q 12.796875 0.140625 7.71875 1.703125 
L 7.71875 11.625 
Q 12.109375 9.234375 16.796875 8.0625 
Q 21.484375 6.890625 26.703125 6.890625 
Q 35.15625 6.890625 40.078125 11.328125 
Q 45.015625 15.765625 45.015625 23.390625 
Q 45.015625 31 40.078125 35.4375 
Q 35.15625 39.890625 26.703125 39.890625 
Q 22.75 39.890625 18.8125 39.015625 
Q 14.890625 38.140625 10.796875 36.28125 
z
" id="DejaVuSans-53"/>
      </defs>
      <g transform="translate(27.825 32.599219)scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-57"/>
       <use x="63.623047" xlink:href="#DejaVuSans-53"/>
      </g>
     </g>
    </g>
    <g id="text_13">
     <!-- Accuracy -->
     <defs>
      <path d="M 34.1875 63.1875 
L 20.796875 26.90625 
L 47.609375 26.90625 
z
M 28.609375 72.90625 
L 39.796875 72.90625 
L 67.578125 0 
L 57.328125 0 
L 50.6875 18.703125 
L 17.828125 18.703125 
L 11.1875 0 
L 0.78125 0 
z
" id="DejaVuSans-65"/>
      <path d="M 8.5 21.578125 
L 8.5 54.6875 
L 17.484375 54.6875 
L 17.484375 21.921875 
Q 17.484375 14.15625 20.5 10.265625 
Q 23.53125 6.390625 29.59375 6.390625 
Q 36.859375 6.390625 41.078125 11.03125 
Q 45.3125 15.671875 45.3125 23.6875 
L 45.3125 54.6875 
L 54.296875 54.6875 
L 54.296875 0 
L 45.3125 0 
L 45.3125 8.40625 
Q 42.046875 3.421875 37.71875 1 
Q 33.40625 -1.421875 27.6875 -1.421875 
Q 18.265625 -1.421875 13.375 4.4375 
Q 8.5 10.296875 8.5 21.578125 
z
M 31.109375 56 
z
" id="DejaVuSans-117"/>
      <path d="M 41.109375 46.296875 
Q 39.59375 47.171875 37.8125 47.578125 
Q 36.03125 48 33.890625 48 
Q 26.265625 48 22.1875 43.046875 
Q 18.109375 38.09375 18.109375 28.8125 
L 18.109375 0 
L 9.078125 0 
L 9.078125 54.6875 
L 18.109375 54.6875 
L 18.109375 46.1875 
Q 20.953125 51.171875 25.484375 53.578125 
Q 30.03125 56 36.53125 56 
Q 37.453125 56 38.578125 55.875 
Q 39.703125 55.765625 41.0625 55.515625 
z
" id="DejaVuSans-114"/>
      <path d="M 34.28125 27.484375 
Q 23.390625 27.484375 19.1875 25 
Q 14.984375 22.515625 14.984375 16.5 
Q 14.984375 11.71875 18.140625 8.90625 
Q 21.296875 6.109375 26.703125 6.109375 
Q 34.1875 6.109375 38.703125 11.40625 
Q 43.21875 16.703125 43.21875 25.484375 
L 43.21875 27.484375 
z
M 52.203125 31.203125 
L 52.203125 0 
L 43.21875 0 
L 43.21875 8.296875 
Q 40.140625 3.328125 35.546875 0.953125 
Q 30.953125 -1.421875 24.3125 -1.421875 
Q 15.921875 -1.421875 10.953125 3.296875 
Q 6 8.015625 6 15.921875 
Q 6 25.140625 12.171875 29.828125 
Q 18.359375 34.515625 30.609375 34.515625 
L 43.21875 34.515625 
L 43.21875 35.40625 
Q 43.21875 41.609375 39.140625 45 
Q 35.0625 48.390625 27.6875 48.390625 
Q 23 48.390625 18.546875 47.265625 
Q 14.109375 46.140625 10.015625 43.890625 
L 10.015625 52.203125 
Q 14.9375 54.109375 19.578125 55.046875 
Q 24.21875 56 28.609375 56 
Q 40.484375 56 46.34375 49.84375 
Q 52.203125 43.703125 52.203125 31.203125 
z
" id="DejaVuSans-97"/>
      <path d="M 32.171875 -5.078125 
Q 28.375 -14.84375 24.75 -17.8125 
Q 21.140625 -20.796875 15.09375 -20.796875 
L 7.90625 -20.796875 
L 7.90625 -13.28125 
L 13.1875 -13.28125 
Q 16.890625 -13.28125 18.9375 -11.515625 
Q 21 -9.765625 23.484375 -3.21875 
L 25.09375 0.875 
L 2.984375 54.6875 
L 12.5 54.6875 
L 29.59375 11.921875 
L 46.6875 54.6875 
L 56.203125 54.6875 
z
" id="DejaVuSans-121"/>
     </defs>
     <g transform="translate(21.329375 163.39375)rotate(-90)scale(0.12 -0.12)">
      <use xlink:href="#DejaVuSans-65"/>
      <use x="66.658203" xlink:href="#DejaVuSans-99"/>
      <use x="121.638672" xlink:href="#DejaVuSans-99"/>
      <use x="176.619141" xlink:href="#DejaVuSans-117"/>
      <use x="239.998047" xlink:href="#DejaVuSans-114"/>
      <use x="281.111328" xlink:href="#DejaVuSans-97"/>
      <use x="342.390625" xlink:href="#DejaVuSans-99"/>
      <use x="397.371094" xlink:href="#DejaVuSans-121"/>
     </g>
    </g>
   </g>
   <g id="patch_13">
    <path d="M 47.55 243.2 
L 47.55 28.8 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="patch_14">
    <path d="M 421.2 243.2 
L 421.2 28.8 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="patch_15">
    <path d="M 47.55 243.2 
L 421.2 243.2 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="patch_16">
    <path d="M 47.55 28.8 
L 421.2 28.8 
" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>
   </g>
   <g id="text_14">
    <!-- AdaBoost: Accuracy vs n_components -->
    <defs>
     <path d="M 45.40625 46.390625 
L 45.40625 75.984375 
L 54.390625 75.984375 
L 54.390625 0 
L 45.40625 0 
L 45.40625 8.203125 
Q 42.578125 3.328125 38.25 0.953125 
Q 33.9375 -1.421875 27.875 -1.421875 
Q 17.96875 -1.421875 11.734375 6.484375 
Q 5.515625 14.40625 5.515625 27.296875 
Q 5.515625 40.1875 11.734375 48.09375 
Q 17.96875 56 27.875 56 
Q 33.9375 56 38.25 53.625 
Q 42.578125 51.265625 45.40625 46.390625 
z
M 14.796875 27.296875 
Q 14.796875 17.390625 18.875 11.75 
Q 22.953125 6.109375 30.078125 6.109375 
Q 37.203125 6.109375 41.296875 11.75 
Q 45.40625 17.390625 45.40625 27.296875 
Q 45.40625 37.203125 41.296875 42.84375 
Q 37.203125 48.484375 30.078125 48.484375 
Q 22.953125 48.484375 18.875 42.84375 
Q 14.796875 37.203125 14.796875 27.296875 
z
" id="DejaVuSans-100"/>
     <path d="M 19.671875 34.8125 
L 19.671875 8.109375 
L 35.5 8.109375 
Q 43.453125 8.109375 47.28125 11.40625 
Q 51.125 14.703125 51.125 21.484375 
Q 51.125 28.328125 47.28125 31.5625 
Q 43.453125 34.8125 35.5 34.8125 
z
M 19.671875 64.796875 
L 19.671875 42.828125 
L 34.28125 42.828125 
Q 41.5 42.828125 45.03125 45.53125 
Q 48.578125 48.25 48.578125 53.8125 
Q 48.578125 59.328125 45.03125 62.0625 
Q 41.5 64.796875 34.28125 64.796875 
z
M 9.8125 72.90625 
L 35.015625 72.90625 
Q 46.296875 72.90625 52.390625 68.21875 
Q 58.5 63.53125 58.5 54.890625 
Q 58.5 48.1875 55.375 44.234375 
Q 52.25 40.28125 46.1875 39.3125 
Q 53.46875 37.75 57.5 32.78125 
Q 61.53125 27.828125 61.53125 20.40625 
Q 61.53125 10.640625 54.890625 5.3125 
Q 48.25 0 35.984375 0 
L 9.8125 0 
z
" id="DejaVuSans-66"/>
     <path d="M 44.28125 53.078125 
L 44.28125 44.578125 
Q 40.484375 46.53125 36.375 47.5 
Q 32.28125 48.484375 27.875 48.484375 
Q 21.1875 48.484375 17.84375 46.4375 
Q 14.5 44.390625 14.5 40.28125 
Q 14.5 37.15625 16.890625 35.375 
Q 19.28125 33.59375 26.515625 31.984375 
L 29.59375 31.296875 
Q 39.15625 29.25 43.1875 25.515625 
Q 47.21875 21.78125 47.21875 15.09375 
Q 47.21875 7.46875 41.1875 3.015625 
Q 35.15625 -1.421875 24.609375 -1.421875 
Q 20.21875 -1.421875 15.453125 -0.5625 
Q 10.6875 0.296875 5.421875 2 
L 5.421875 11.28125 
Q 10.40625 8.6875 15.234375 7.390625 
Q 20.0625 6.109375 24.8125 6.109375 
Q 31.15625 6.109375 34.5625 8.28125 
Q 37.984375 10.453125 37.984375 14.40625 
Q 37.984375 18.0625 35.515625 20.015625 
Q 33.0625 21.96875 24.703125 23.78125 
L 21.578125 24.515625 
Q 13.234375 26.265625 9.515625 29.90625 
Q 5.8125 33.546875 5.8125 39.890625 
Q 5.8125 47.609375 11.28125 51.796875 
Q 16.75 56 26.8125 56 
Q 31.78125 56 36.171875 55.265625 
Q 40.578125 54.546875 44.28125 53.078125 
z
" id="DejaVuSans-115"/>
     <path d="M 11.71875 12.40625 
L 22.015625 12.40625 
L 22.015625 0 
L 11.71875 0 
z
M 11.71875 51.703125 
L 22.015625 51.703125 
L 22.015625 39.3125 
L 11.71875 39.3125 
z
" id="DejaVuSans-58"/>
     <path id="DejaVuSans-32"/>
     <path d="M 2.984375 54.6875 
L 12.5 54.6875 
L 29.59375 8.796875 
L 46.6875 54.6875 
L 56.203125 54.6875 
L 35.6875 0 
L 23.484375 0 
z
" id="DejaVuSans-118"/>
    </defs>
    <g transform="translate(91.741406 22.8)scale(0.15 -0.15)">
     <use xlink:href="#DejaVuSans-65"/>
     <use x="66.658203" xlink:href="#DejaVuSans-100"/>
     <use x="130.134766" xlink:href="#DejaVuSans-97"/>
     <use x="191.414062" xlink:href="#DejaVuSans-66"/>
     <use x="260.017578" xlink:href="#DejaVuSans-111"/>
     <use x="321.199219" xlink:href="#DejaVuSans-111"/>
     <use x="382.380859" xlink:href="#DejaVuSans-115"/>
     <use x="434.480469" xlink:href="#DejaVuSans-116"/>
     <use x="473.689453" xlink:href="#DejaVuSans-58"/>
     <use x="507.380859" xlink:href="#DejaVuSans-32"/>
     <use x="539.167969" xlink:href="#DejaVuSans-65"/>
     <use x="605.826172" xlink:href="#DejaVuSans-99"/>
     <use x="660.806641" xlink:href="#DejaVuSans-99"/>
     <use x="715.787109" xlink:href="#DejaVuSans-117"/>
     <use x="779.166016" xlink:href="#DejaVuSans-114"/>
     <use x="820.279297" xlink:href="#DejaVuSans-97"/>
     <use x="881.558594" xlink:href="#DejaVuSans-99"/>
     <use x="936.539062" xlink:href="#DejaVuSans-121"/>
     <use x="995.71875" xlink:href="#DejaVuSans-32"/>
     <use x="1027.505859" xlink:href="#DejaVuSans-118"/>
     <use x="1086.685547" xlink:href="#DejaVuSans-115"/>
     <use x="1138.785156" xlink:href="#DejaVuSans-32"/>
     <use x="1170.572266" xlink:href="#DejaVuSans-110"/>
     <use x="1233.951172" xlink:href="#DejaVuSans-95"/>
     <use x="1283.951172" xlink:href="#DejaVuSans-99"/>
     <use x="1338.931641" xlink:href="#DejaVuSans-111"/>
     <use x="1400.113281" xlink:href="#DejaVuSans-109"/>
     <use x="1497.525391" xlink:href="#DejaVuSans-112"/>
     <use x="1561.001953" xlink:href="#DejaVuSans-111"/>
     <use x="1622.183594" xlink:href="#DejaVuSans-110"/>
     <use x="1685.5625" xlink:href="#DejaVuSans-101"/>
     <use x="1747.085938" xlink:href="#DejaVuSans-110"/>
     <use x="1810.464844" xlink:href="#DejaVuSans-116"/>
     <use x="1849.673828" xlink:href="#DejaVuSans-115"/>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p33d5c294a3">
   <rect height="214.4" width="373.65" x="47.55" y="28.8"/>
  </clipPath>
 </defs>
</svg>



















![result2](https://github.com/aadarshgupta1412/covid-symptoms-classification/assets/62350692/91e05d89-cfd1-4b52-8c5d-55cefd3c2559)
