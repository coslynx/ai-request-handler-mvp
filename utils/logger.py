import logging
import os

class Logger:
    def __init__(self):
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        self.logger = logging.getLogger("AIRequestHandler")
        self.logger.setLevel(log_level)

        # Create console handler
        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # Add the console handler to the logger
        self.logger.addHandler(ch)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

logger = Logger()