# ocr/process.py

import easyocr

def perform_ocr_easyocr(image_path):
    reader = easyocr.Reader(['en'])  # Initialize with English language
    results = reader.readtext(image_path, detail=0)  # detail=0 gives plain text output
    return ' '.join(results)

def process_image(image_path):
    processed_image_path = preprocess_image(image_path)
    return perform_ocr_easyocr(processed_image_path)
