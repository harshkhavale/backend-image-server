# scraping/scraper.py

import requests
from bs4 import BeautifulSoup
import os
from scraping.urls import restaurant_urls

def scrape_menu_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menu_images = soup.find_all('img', class_='menu-image')
    image_urls = [img['src'] for img in menu_images]
    return image_urls

def download_image(url, folder='data'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    response = requests.get(url)
    filename = os.path.join(folder, url.split('/')[-1])
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename

def scrape_all_images():
    for url in restaurant_urls:
        image_urls = scrape_menu_images(url)
        for image_url in image_urls:
            download_image(image_url)

if __name__ == "__main__":
    scrape_all_images()
