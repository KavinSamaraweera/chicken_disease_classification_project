# For simplicity, we use this constructor file to create logging module

import os
import sys
import logging

#Display logging string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#Initializing final log
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # print log on terminal
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
