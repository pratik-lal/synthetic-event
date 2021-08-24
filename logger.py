import logging
from logging import handlers

# Create logger
logger = logging.getLogger("synthetic events")
logger.setLevel(logging.DEBUG)

# File handler
# fh = logging.FileHandler(filename="log/agent.log", mode="a")
fh = logging.handlers.RotatingFileHandler(filename="log/agent.log", mode="a", maxBytes=1000000, backupCount=10)
fh.setLevel(logging.DEBUG)

# log file formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)
# logger.info("hello logger! hello logger! hello logger! hello logger!")
# print(logger)

