import os
import sys
import logging

logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

logs_file_path = os.path.join(logs_dir, "logs.log")

logging_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(
    level=logging.INFO,
    format=logging_format,

    handlers=[
        logging.FileHandler(logs_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Deformity Detection")