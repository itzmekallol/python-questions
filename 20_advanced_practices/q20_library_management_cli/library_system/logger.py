"""
logger.py — sets up a standard-library logger that writes library
activity to a log file, for the "Logging" requirement.
"""

import logging
import os


def get_logger(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "library.log")

    logger = logging.getLogger("library_system")
    logger.setLevel(logging.INFO)

    # avoid adding duplicate handlers if get_logger() is called more than once
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
