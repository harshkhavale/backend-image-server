# app.py

import os
from scraping.scraper import scrape_all_images
from ocr.process import process_image
from ocr.extract import extract_items_and_prices
from storage.db import insert_restaurant, insert_menu_item

def main():
    # Step 1: Scrape images
    scrape_all_images()

    # Step 2: OCR processing and extraction
    for image_file in os.listdir('data'):
        if image_file.endswith('.jpg'):
            ocr_text = process_image(os.path.join('data', image_file))
            items_and_prices = extract_items_and_prices(ocr_text)
            
           

if __name__ == "__main__":
    main()
