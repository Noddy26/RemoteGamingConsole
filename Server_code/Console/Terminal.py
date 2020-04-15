from termcolor import colored


class Output(object):

    @staticmethod
    def red(text):
        message = colored(text, 'red')
        print(message)

    @staticmethod
    def white(text):
        message = colored(text, 'white')
        print(message)

    @staticmethod
    def green(text):
        message = colored(text, 'green')
        print(message)

    @staticmethod
    def yellow(text):
        message = colored(text, 'yellow')
        print(message)

    @staticmethod
    def blue(text):
        message = colored(text, 'blue')
        print(message)
