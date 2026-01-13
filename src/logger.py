import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

def get_logger(name: str = __name__) -> logging.Logger:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        filemode="a",
        encoding="utf-8",
        format='[%(asctime)s] %(lineno)d %(filename)s %(levelname)s - %(message)s',
        level=logging.INFO,
        force=True,  # ensures config applies even if logging was already configured
    )
    return logging.getLogger(name)

# Example usage:
# from src.logger import get_logger
# logger = get_logger(__name__)
# logger.info("Pipeline started")
# logger.error("An error occurred")