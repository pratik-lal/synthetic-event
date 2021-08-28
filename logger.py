import logging
from logging import handlers
import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read("./syntheticevent.config")
log_file_backcup = config.getint("Log", "LogFileRetention")


# Create logger
logger = logging.getLogger("synthetic events")
logger.setLevel(logging.DEBUG)

# File handler
# fh = logging.FileHandler(filename="log/agent.log", mode="a")
fh = logging.handlers.RotatingFileHandler(filename="log/agent.log", mode="a",
                                          maxBytes=1000000,
                                          backupCount=log_file_backcup)
fh.setLevel(logging.DEBUG)

# log file formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)
# logger.info("hello logger! hello logger! hello logger! hello logger!")
# print(logger)

