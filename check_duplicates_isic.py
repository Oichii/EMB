"""
Duplicate removal between benchmark set and ISIC datasets
1. ISIC ID based duplicate removal
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

thickness_data = pd.read_csv(r"combined_stage_data.csv")
thickness_path = r'images'

thickness_data = thickness_data.drop_duplicates()

isic_data = {
    'ISIC-2017_Training_Part3_GroundTruth.csv': 'image_id',
    'ISIC-2017_Validation_Part3_GroundTruth.csv': 'image_id',
    'ISIC-2017_Test_v2_Part3_GroundTruth.csv': 'image_id',
    'ISIC_2019_Training_GroundTruth.csv': 'image',
    'ISIC_2020_Training_GroundTruth.csv': 'image_name',
    'ISIC2018_Task3_Validation_GroundTruth.csv': 'image',
    'ISIC2018_Task3_Training_GroundTruth.csv': 'image',
    'ISIC2018_Task3_Test_GroundTruth.csv': 'image'
}
in_attributes = ['ISIC_0021187', 'ISIC_0021780', 'ISIC_0022317', 'ISIC_0023747', 'ISIC_0024095', 'ISIC_0021816',
                'ISIC_0023371', 'ISIC_0023508', 'ISIC_0023755', 'ISIC_0023924']

challenge_duplicates = ['ISIC_1605945', 'ISIC_0023807', 'ISIC_0023890', 'ISIC_0023769', 'ISIC_0023670', 'ISIC_0046471',
                        '374_1', 'ISIC_0022113', 'ISIC_0021908', 'ISIC_0023705', 'ISIC_0021917', 'ISIC_0021745',
                        'ISIC_0021706', 'ISIC_0023671', 'ISIC_0023806', 'ISIC_0022306', 'ISIC_0024108', 'ISIC_0021399',
                        'ISIC_0021646', 'ISIC_0023843', 'ISIC_0021534', 'ISIC_0022328', 'ISIC_0023706', 'ISIC_0022022',
                        'ISIC_0024015', 'ISIC_0023853', 'ISIC_0021530', 'ISIC_0021985', 'ISIC_0021188', 'ISIC_0023642',
                        'ISIC_0022000', 'ISIC_0022685', 'ISIC_0022339']

# ISIC ID based duplicate removal
duplicate_ids = []
for dataset in isic_data.keys():
    isic_2017_data = pd.read_csv(
        fr'labels\{dataset}')
    duplicates = 0
    same_isic_id = isic_2017_data[(isic_2017_data[isic_data[dataset]].isin(in_attributes))]
    print("same isic id ", same_isic_id)
    for row in thickness_data.itertuples():
        isic_id = row.image
        if not isic_2017_data[isic_2017_data[isic_data[dataset]]==isic_id].empty:
            # print(isic_id, row)
            duplicates += 1
            duplicate_ids.append(isic_id)
    print(dataset, duplicates, duplicate_ids, len(duplicate_ids))
duplicate_ids = np.unique(duplicate_ids)
print(len(duplicate_ids))
data = thickness_data[~(thickness_data['image'].isin(duplicate_ids))]

data = data[~(thickness_data['image'].isin(challenge_duplicates))]
data.to_csv('combined_stage_data_duplicate_removed_challenge.csv', index=False)
