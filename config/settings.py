# config/settings.py

# Database configuration
DATABASE_URL = 'postgresql://postgres:harsh@localhost:5432/postgres'

# Directory to store downloaded and processed images
IMAGE_DIR = 'data'

# EasyOCR configuration
# Define the languages for OCR processing (e.g., 'en' for English)
OCR_LANGUAGES = ['en']  # Add other language codes as needed, e.g., ['en', 'hi']

# Preprocessing settings (can be expanded as needed)
PREPROCESSING = {
    'threshold': 150,  # Threshold for binarization
    'binary_max': 255,  # Max value for binary thresholding
}

# Additional settings (Optional, for future expansion)
DEBUG_MODE = True  # Set to False in production

# Logging configuration (Optional)
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG_MODE else 'INFO',
    },
}

# Tesseract command path (if using Tesseract OCR)
# Uncomment and adjust the path if using Tesseract
# TESSERACT_CMD = '/usr/local/bin/tesseract'  # Adjust based on your system

# Function to log messages (Optional utility)
import logging.config
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
