import logging

logging.basicConfig(filename='.\\syntheticevent.log',
                    format='%(asctime) %(levelname) %(message)')


logger = logging.getLogger()
logger.addHandler()
logger.info("hello ji")
print(logger.handlers)

