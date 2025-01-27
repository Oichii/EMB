import pandas as pd
import os
import re

path_to_images = r''
csv_path = os.path.join(path_to_images, 'metadata_atlas.csv')
df = pd.read_csv(csv_path)

new_data = []
for row in df.itertuples(index=False):
    img = row.images.strip("[]").split(',')
    for i in img:
        name = re.sub('[^A-Za-z0-9._-]+', '', i)
        print(name)
        new_data.append({"image": name, "description": row.description, "history": row.history, "thickness": 0,
                         "type": "dermoscopic"})
new_df = pd.DataFrame(new_data)
new_df.to_csv(os.path.join(path_to_images, "metadata_cleared.csv"), index=False)
