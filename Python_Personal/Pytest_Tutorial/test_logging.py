import inspect
import logging

class BaseLog:
    def Log(self):
        loggerName = inspect.stack()[1][3]
        fileHandler = logging.FileHandler('file.log')
        fileFormat = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(fileFormat)

        logger = logging.getLogger(loggerName)
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        # DEBUG < INFO < WARN < ERROR < FATAL

        # logger.debug("a message statement")
        # logger.info("information logging")
        # logger.warning("warning warning!!")
        # logger.error("error message")
        # logger.critical("critical error")
        return logger

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger