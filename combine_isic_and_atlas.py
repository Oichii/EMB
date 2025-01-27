"""
Merge ISIC Archive data with data scraped from Dermoscopy Atlas (https://www.dermoscopyatlas.com/)
"""

import pandas as pd

isic_csv = pd.read_csv(r'isic_cleaned.csv')
isic_csv = isic_csv.rename(
    columns={'isic_id': 'image', 'mel_thick_mm': 'thickness', 'image_type': 'type', 'mel_class': 'mel_class',
             'stage_ajcc': 'stage_ajcc'
             })
isic_csv = isic_csv.drop(['mel_class'], axis=1)
isic_csv['cathegory'] = 'MEL'
isic_csv['label'] = 6
isic_csv['source'] = 'ISIC'

scraped_csv = pd.read_csv(r'atlas_scraped_cleaned.csv')
scraped_csv = scraped_csv.drop(['stage'], axis=1)
scraped_csv['image'] = scraped_csv['image'].str.split('.').str.get(0)
scraped_csv['source'] = 'Atlas'

combined = pd.concat([isic_csv, scraped_csv])

# list of duplicate images based on czkawka
images_to_remove = ['ISIC_0023554', 'ISIC_0023266', 'ISIC_6584579', 'ISIC_8253057', '383_1', '383_3', '383_2']
combined = combined[~(combined['image'].isin(images_to_remove))]

combined.to_csv('combined_stage_data.csv', index=False)
