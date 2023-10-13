"""
Levels:
    DEBUG (not shown by default)
    INFO (not shown by default)
    WARNING
    ERROR
    CRITICAL
"""
import logging.handlers
import datetime
from constants import LOG_FILE_MAX_SIZE, LOG_BACKUP_COUNT

# Basic setup
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)-8s: [%(filename)s:%(lineno)d] %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     filename='logs/logs.txt'
# )
#
# logger = logging.getLogger(__name__)

# Advanced setup
def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Dynamically generate the filename based on the current date
    current_date = datetime.date.today().isoformat()   # returns date in the format YYYY-MM-DD
    filename = f"logs/app-{current_date}.txt"

    # Create a rotating file handler
    handler = logging.handlers.RotatingFileHandler(
        filename, maxBytes=LOG_FILE_MAX_SIZE, backupCount=LOG_BACKUP_COUNT
    )

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        # "%(asctime)s %(levelname)-8s: [%(name)s] [%(filename)s:%(lineno)d] %(message)s",
        "%(asctime)s %(levelname)-8s: [%(name)s.py:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

logger = setup_logger()

def test():
    print(datetime.datetime.utcnow().date().isoformat())
    logger.info("Only shown if basicConfig is enabled")
    logger.warning("this is a warning")
    logger.debug("a debug one")
    logger.critical("a scary critical one 😅")  # don't use emojis in production ;)
