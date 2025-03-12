#!/usr/bin/env python3
"""
Storm911 Application Entry Point
Run this script to start the Storm911 application.
"""

import os
import sys
import logging
from app import run_app
from config import LOGGING_CONFIG, LOGS_DIR

def setup_logging():
    """Configure logging for the application."""
    log_file = os.path.join(LOGS_DIR, 'storm911.log')
    
    # Ensure logs directory exists
    os.makedirs(LOGS_DIR, exist_ok=True)
    
    # Configure logging
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("Starting Storm911 Application")

def main():
    """Main entry point for the application."""
    try:
        # Setup logging
        setup_logging()
        
        # Run the application
        run_app()
        
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
