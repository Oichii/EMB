import os
from combine_csvs import get_ajcc_stage
import pandas as pd
import matplotlib.pyplot as plt
path = r''
folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
data = []
for c in folders:
    if c=='isic_images_combined':
        continue
    df = pd.read_csv(os.path.join(path, c, 'metadata.csv'), index_col=False)
    print(os.path.join(path, c, 'metadata.csv'), df.columns)
    data.append(df.loc[:, ['isic_id', 'mel_thick_mm', 'image_type', 'mel_class']])
new = pd.concat(data, ignore_index=True)
new.update(new[new['mel_class']=='melanoma in situ'].loc[:, 'mel_thick_mm'].fillna(0))
new['mel_class'] = new['mel_class'].fillna('unknown')
# new[new['mel_class']=='melanoma in situ'] = new[new['mel_class']=='melanoma in situ'].loc[:, 'mel_thick_mm'].fillna(0)
new = new.dropna()

new['stage_ajcc'] = new['mel_thick_mm'].apply(get_ajcc_stage)

new['stage_ajcc'].value_counts().plot(kind='bar')
plt.show()

new['image_type'].value_counts().plot(kind='bar')
plt.show()
new = new.drop_duplicates()

new.to_csv(os.path.join(path, 'isic_cleaned_3.csv'), index=False)
