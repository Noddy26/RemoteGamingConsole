import signal
import sys
from Server_code.Database_functions.Encryt import Encryption
from Server_code.Console.Terminal import Output


class GetInput():

    def __init__(self, parameter):
        self.parameter = parameter

    def get(self):
        global input
        parameter = self.parameter
        # construct the prompting message
        prompt_message = parameter.prompt
        if (parameter.default != None):
            prompt_message += ' [%s]: ' % (parameter.default)

        displaying = (parameter.displaying_name + ": ")
        Output.white(displaying)

        while True:
            # check for Ctrl-c press
            signal.signal(signal.SIGINT, self._dynamic_menu_ctrlC_handler)
            # check for Ctrl-Z press
            signal.signal(signal.SIGTSTP, self._dynamic_menu_ctrlC_handler)

            if (input == ''):
                input = parameter.default

            if (GetInput.check_input_validity(self, input, parameter)):
                # process of valid input
                if (parameter.confidential):
                    input = Encryption.encrypt(input)
                parameter.input = input
                break
            else:
                Output.yellow("Please provide a value.")
        print('')
        return parameter

    def check_input_validity(self, input, parameter):
        if (input == None):
            return False
        return True

    def _dynamic_menu_ctrlC_handler(self, sig, frame):
        Output.red('Control C used to exit setup before setup was complete')
        sys.exit(0)
