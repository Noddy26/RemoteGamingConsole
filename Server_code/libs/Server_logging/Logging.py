import logging
import os


class Logger(object):
    _static_logger = None

    def __init__(self, name='logger', level=logging.DEBUG):
        self.file = 'debug_server.log'
        if os.path.exists("Server_logs") is False:
            os.mkdir("Server_logs")
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter('Server: %(asctime)s:%(levelname)s:%(msg)s', )
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
        fh = logging.FileHandler("Server_logs/" + self.file)
        with open("Server_logs/" + self.file, "w") as f:
            f.write("*****************Start Server of Log********************\n")
        return fh
