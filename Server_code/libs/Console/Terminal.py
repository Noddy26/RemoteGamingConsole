from termcolor import colored
from libs.Server_logging.Logging import Logger


class Output(object):

    @staticmethod
    def red(text):
        message = colored(text, 'red')
        print(message)
        Logger.error(text)

    @staticmethod
    def white(text):
        message = colored(text, 'white')
        print(message)
        Logger.info(text)

    @staticmethod
    def green(text):
        message = colored(text, 'green')
        print(message)
        Logger.info(text)

    @staticmethod
    def yellow(text):
        message = colored(text, 'yellow')
        print(message)
        Logger.info(text)

    @staticmethod
    def blue(text):
        message = colored(text, 'blue')
        print(message)
        Logger.info(text)
