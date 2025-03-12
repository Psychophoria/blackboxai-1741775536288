"""
Configuration settings for the Storm911 application.
"""

import os
import logging
from typing import Dict, Any

# Directory Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
EXPORTS_DIR = os.path.join(BASE_DIR, 'exports')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

# Color Scheme
COLORS = {
    "primary_blue": "#007bff",
    "secondary_gray": "#6c757d",
    "success_green": "#28a745",
    "danger_red": "#dc3545",
    "warning_yellow": "#ffc107",
    "info_cyan": "#17a2b8",
    "light_gray": "#f8f9fa",
    "dark_gray": "#343a40",
    "white": "#ffffff",
    "black": "#000000"
}

# Font Settings
TITLE_FONT = ("Helvetica", 24, "bold")
HEADER_FONT = ("Helvetica", 18, "bold")
NORMAL_FONT = ("Helvetica", 14)
SMALL_FONT = ("Helvetica", 12)

# Window Settings
WINDOW_SIZE = "1280x720"
MIN_WINDOW_SIZE = (800, 600)

# API Settings
API_BASE_URL = "https://api.readymode.com/v1"
API_TIMEOUT = 30  # seconds

# Email Settings
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "use_tls": True,
    "sender_email": "noreply@storm911.com",
    "sender_name": "Storm911 Support"
}

# PDF Settings
PDF_CONFIG = {
    "page_size": "Letter",
    "margin": 72,  # 1 inch in points
    "font_name": "Helvetica",
    "font_size": 12
}

# Logging Configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'storm911.log'),
            'mode': 'a',
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# Application Settings
APP_SETTINGS = {
    "app_name": "Storm911",
    "version": "1.0.0",
    "company": "AssureCall",
    "support_email": "support@assurecall.com",
    "support_phone": "1-800-SUPPORT"
}

# Cache Settings
CACHE_CONFIG = {
    "enable_cache": True,
    "cache_dir": TEMP_DIR,
    "max_cache_size": 100 * 1024 * 1024,  # 100MB
    "cache_ttl": 3600  # 1 hour
}

# Feature Flags
FEATURES = {
    "enable_dark_mode": True,
    "enable_notifications": True,
    "enable_auto_save": True,
    "enable_analytics": False
}
