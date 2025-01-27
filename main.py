"""
Scrap image and its description from Dermoscopy Atls for single diagnosis.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

save_path = r'C:\Users\Aleksandra\PycharmProjects\saved_images'

# url = 'https://www.dermoscopyatlas.com/diagnosis/578?'
url = 'https://www.dermoscopyatlas.com/diagnosis/647?'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=url, headers=header)

soup = BeautifulSoup(r.content, 'html.parser')
cases = soup.findAll('img')
metadata = []
for c in cases:
    print(c.parent)
    if c.get('class') == ['image', 'img-responsive']:
        print(c.parent['href'])
        r_detail = requests.get(url=c.parent['href'], headers=header)
        if r_detail.status_code != 200:
            print(c.parent['href'], 'status code:', r_detail.status_code)
            continue
        detail_soup = BeautifulSoup(r_detail.content, 'html.parser')
        images = detail_soup.findAll('img')
        img_names = []
        for img in images:
            if img.get('class') == ['image', 'img-responsive']:
                img_url = img.get('src')
                image_name = img_url.split('/')[-1]
                img_names.append(image_name)
                print(image_name)
                img_data = requests.get(img_url, headers=header).content
                with open(os.path.join(save_path, image_name), 'wb') as handler:
                    handler.write(img_data)
        descriptions = detail_soup.findAll('b')

        description = descriptions[0].parent.get_text()
        history = descriptions[1].parent.get_text()
        metadata.append({'images': img_names, 'description': description, 'history': history})
    # print(r_detail)
metadata_df = pd.DataFrame(metadata)
metadata_df['history'] = metadata_df['history'].str.replace('\n', ' ')
metadata_df['description'] = metadata_df['description'].str.replace('\n', ' ')

metadata_df['history'] = metadata_df['history'].str.replace('\xa0', ' ')
metadata_df['description'] = metadata_df['description'].str.replace('\xa0', ' ')

metadata_df.to_csv(os.path.join(save_path, "metadata_atlas.csv"))
