import os
import logging
from logging.handlers import TimedRotatingFileHandler

class LogManager:
    def __init__(self, root_directory):
        self.__root_directory = root_directory

    def get_logger(self):
        log_filename = "arabic_verb"
        folder_name = "app_logs"
        
        log_folder_path = os.path.join(self.__root_directory, folder_name)
        os.makedirs(log_folder_path, exist_ok = True)
        log_file_path = os.path.join(log_folder_path, log_filename)

        # Create a TimedRotatingFileHandler that rotates at midnight and keeps 7 days of logs
        handler = TimedRotatingFileHandler(f"{log_file_path}.log",   # Log file name pattern
                                           when = "midnight",       # Rotate at midnight
                                           interval = 1,            # Rotate every 1 day
                                           backupCount = 7)         # Keep the last 7 log files (logs older than 7 days will be deleted)
    
        # Set the logging level and format
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Set up the logger
        logger = logging.getLogger("my_day_logger")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger
