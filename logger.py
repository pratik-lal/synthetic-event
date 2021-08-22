import logging

# Create logger
logger = logging.getLogger("synthetic events")
logger.setLevel(logging.DEBUG)

# File handler
fh = logging.FileHandler(filename="log/agent.log", mode="a")
fh.setLevel(logging.DEBUG)

# log file formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)
# logger.info("hello logger!")
# print(logger)

