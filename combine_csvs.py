"""
Merge data scraped from Dermoscopy atlas.
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


def get_ajcc_stage(thickness):
    """
    stage classification according to https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7652033/
    """
    if thickness == 0:
        return 0
    elif 0 < thickness <= 1:
        return 1
    elif 1 < thickness <= 2:
        return 2
    elif 2 < thickness <= 4:
        return 3
    elif thickness > 4:
        return 4
    else:
        print(thickness)
        return -1


if __name__ == '__main__':
    path = r'saved_images'
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    data = []
    for c in folders:
        df = pd.read_csv(os.path.join(path, c, 'metadata_cleared.csv'), index_col=False)
        print(df)
        if c == 'in_situ_melanoma':
            df['stage'] = 0
        data.append(df)
        print("done", c)
    new = pd.concat(data, ignore_index=True)
    new.loc[(new['type'] == 'clinincal'), 'type'] = 'clinical'
    print(new)
    data_to_save = new[(new['type'] == 'clinical') | (new['type'] == 'dermoscopic')]
    data_to_save = data_to_save.drop(['history', 'description'], axis="columns")
    data_to_save['cathegory'] = 'MEL'
    data_to_save['label'] = 6

    data_to_save.loc[data_to_save['thickness'] == '?', 'thickness'] = np.nan

    data_to_save = data_to_save.dropna()

    data_to_save['thickness'] = pd.to_numeric(data_to_save['thickness'])
    data_to_save['stage_ajcc'] = data_to_save['thickness'].apply(get_ajcc_stage)

    data_to_save['stage_ajcc'].value_counts().plot(kind='bar')
    plt.show()

    data_to_save['type'].value_counts().plot(kind='bar')
    plt.show()

    data_to_save.to_csv(os.path.join(path, 'atlas_scraped_cleaned.csv'), index=False)