import logging
import os
from logging.handlers import RotatingFileHandler

# Define log directory and filename
LOG_DIR = "logs"
LOG_FILE = "app.log"
os.makedirs(LOG_DIR, exist_ok=True)

# Full path for log file
log_path = os.path.join(LOG_DIR, LOG_FILE)

# Formatter for logs
formatter = logging.Formatter(
    fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Rotating File Handler (max 5MB per file, 5 backup files)
file_handler = RotatingFileHandler(
    log_path, maxBytes=5*1024*1024, backupCount=5
)
file_handler.setFormatter(formatter)

# Stream Handler (console)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Function to get a logger
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding handlers multiple times
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    logger.propagate = False
    return logger
