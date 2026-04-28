from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__) # "__main__"

def main():
    logger.info("Application started!")
    logger.debug("Debug info here")
    try:
        1 / 0
    except ZeroDivisionError as e:
        logger.exception(f"An error occurred {e}")

main()
