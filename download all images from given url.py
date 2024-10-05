#downloads all images from a given url :) DOESMT WORK ???

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_images(url, folder='images'):
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Get the webpage content
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Download each image
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        
        # Make the URL absolute
        img_url = urljoin(url, img_url)
        
        try:
            # Get the image content
            img_response = requests.get(img_url, headers=headers)
            img_response.raise_for_status()
            
            # Get the image name
            img_name = os.path.join(folder, os.path.basename(img_url))
            if not os.path.splitext(img_name):  # If no extension, add .jpg
                img_name += '.jpg'
            
            # Save the image
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
        
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {img_url}: {e}")

# insert target hereeeeeeeeeee
download_images('https://www.heavensgate.com/')

