import logging

class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger("automation_logger")
        logger.setLevel(logging.DEBUG)
        return logger