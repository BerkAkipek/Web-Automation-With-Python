import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("test_logging_log.log")

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)
    logger.debug("Debug Statement.")
    logger.info("Info Statement")
    logger.warning("Warning Statement")
    logger.error("Error Statement")
    logger.critical("Critical statement")

# python3 -m pytest ./pytest_tests/test_logging.py -vs