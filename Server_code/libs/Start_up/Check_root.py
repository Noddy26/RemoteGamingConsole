import os
from libs.Console.Terminal import Output


class CheckRoot:

    def __init__(self):
        # check if user has root access
        if not self.check_root():
            Output.red("Must have root access or be run with sudo")
            os._exit(1)

    def check_root(self):
        if os.getuid() != 0:
            return False
        else:
            return True