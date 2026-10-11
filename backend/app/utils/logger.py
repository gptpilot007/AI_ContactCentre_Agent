import logging
import logging.config
import yaml
import os

LOG_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "logging",
    "logs_config.yaml"
)

def setup_logging():
    if os.path.exists(LOG_CONFIG_PATH):
        with open(LOG_CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

def get_logger(name):
    setup_logging()
    return logging.getLogger(name)
