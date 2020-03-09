import logging
import os
import time

from ClientGui.variables.Configuration import Configuration


class Logger(object):
    _static_logger = None

    def __init__(self, name='logger', level=logging.DEBUG):
        self.file = 'debug_' + Configuration.Username + '.log'
        if os.path.exists("Logging/logs") is False:
            os.mkdir("Logging/logs")
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter(Configuration.Username + ': %(asctime)s:%(levelname)s:%(msg)s', )
        fh = self._logfile()
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        Logger._static_logger = logger

    def shutdownLogger(self):
        print("Log is being stopped")
        logging.shutdown()

    @staticmethod
    def debug(msg):
        Logger._static_logger.debug(msg)

    @staticmethod
    def info(msg):
        Logger._static_logger.info(msg)

    @staticmethod
    def warning(msg):
        Logger._static_logger.warning(msg)

    @staticmethod
    def error(msg):
        Logger._static_logger.error(msg)

    @staticmethod
    def critical(msg):
        Logger._static_logger.critical(msg)

    def _logfile(self):
        fh = logging.FileHandler("Logging/logs/" + self.file)
        with open("Logging/logs/" + self.file, "w") as f:
            f.write("*****************Start of Log********************\n")
        return fh
