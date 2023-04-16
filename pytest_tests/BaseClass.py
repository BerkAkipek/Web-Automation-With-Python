import logging
import inspect


class BaseClass:

    def test_logging_demo(self):
        logger_name = inspect.stack()[1][3]

        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("test_logging_log.log")

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
    
        return logger
    
