import os
from logs.log_generator import log_generator
import logging

os.makedirs("logs", exist_ok=True)
logger_gen = log_generator("LOG_FILE_PATH")
logger_gen.log_config()

logging.info("This is an INFO log")
logging.warning("This is a WARNING log")
logging.error("This is an ERROR log")
logging.critical("This is a CRITICAL log")
logging.debug("This is a DEBUG log")
logging.fatal("This is a FATAL log")

