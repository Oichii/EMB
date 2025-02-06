# EMB - Early Stage Melanoma benchmark Dataset

## Abstract
Early detection of melanoma is crucial for improving patient outcomes, as survival rates decline dramatically with disease progression. Despite significant achievements in deep learning methods for skin lesion analysis, several challenges limit their effectiveness in clinical practice. One of the key issues is the lack of knowledge about the melanoma stage distribution in the training data, raising concerns about the ability of these models to detect early-stage melanoma accurately. Additionally, publicly available datasets that include detailed information on melanoma stage and tumor thickness remain scarce, restricting researchers from developing and benchmarking methods specifically tailored for early diagnosis. Another major limitation is the lack of cross-dataset evaluations. Most deep learning models are tested on the same dataset they were trained on, failing to assess their generalization ability when applied to unseen data. This reduces their reliability in real-world clinical settings. To address these issues, we introduce an early-stage melanoma benchmark dataset, featuring images labeled according to T-category based on Breslow thickness. We evaluated several state-of-the-art deep learning models on this dataset and observed a significant drop in performance compared to their results on ISIC Challenge datasets. This finding highlights the models’ limited capability in detecting early-stage melanoma. By providing a resource for T-category-specific analysis and supporting cross-dataset evaluation, this work seeks to advance the development and clinical applicability of automated melanoma diagnostic systems. 

## Data 
download images from https://gallery.isic-archive.com/ where all thickness options in Melanoma Thickness (mm) are selected and "in situ" is selected from Melanoma Class

direct URL: https://shorturl.at/5NnpP

Use `web_scraping.py` to download images from: https://www.dermoscopyatlas.com/ 

Labels for obtained images can be found in `early_melanoma_benchmark_dataset_labels.csv`