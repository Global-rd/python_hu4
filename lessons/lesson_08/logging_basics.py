import logging

#HANDLER: hova íródjon a log üzenet
#FORMATTER: milyen formában jelenjen meg az üzenet
# a formattert adjuk hozzá a handler-hez, és a handler-t addjuk hozzá a logger-hez


file_handler = logging.FileHandler("app.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.DEBUG)


logger = logging.getLogger()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a criticalmessage")