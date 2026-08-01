
"""
====================================================
ALPHA v2.0
Logger Module
====================================================
"""

import logging
from logging.handlers import RotatingFileHandler
from config import LOG_FILE

LOGGER_NAME = "ALPHA"

logger = logging.getLogger(LOGGER_NAME)

if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def info(message):
    logger.info(message)


def warning(message):
    logger.warning(message)


def error(message):
    logger.error(message)


def critical(message):
    logger.critical(message)


info("========== ALPHA v2 Logger Started ==========")
