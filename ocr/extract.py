# ocr/extract.py

import re

def extract_items_and_prices(text):
    # Improved regex to handle different price formats
    pattern = r'(.+?)\s+(\d+[\.,]?\d*\s?[₹$€£]?)'
    items_and_prices = re.findall(pattern, text)
    return [{'item': item.strip(), 'price': price.strip()} for item, price in items_and_prices]
