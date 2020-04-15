import sys
from libs.Database_functions.Encryt import Encryption
from libs.Console.Terminal import Output


class GetInput():

    def __init__(self, parameter):
        self.parameter = parameter

    def get(self):
        parameter = self.parameter
        # construct the prompting message
        prompt_message = parameter.prompt
        if (parameter.default != None):
            prompt_message += ' [%s]: ' % (parameter.default)

        displaying = (parameter.displaying_name + ": ")


        while True:
            Output.yellow("\n" + prompt_message)
            input_user = input(displaying)
            if (input_user == ''):
                input_user = parameter.default
                Output.green("Defaulted to %s" + parameter.default)

            if (GetInput.check_input_validity(self, input_user, parameter)):
                # process of valid input
                if (parameter.confidential):
                    input_user = Encryption.encrypt(input_user)
                parameter.input_user = input_user
                break
            else:
                Output.red("Please provide a value.")
        return parameter

    def check_input_validity(self, input_user, parameter):
        if (input_user == None):
            return False
        return True

    def _dynamic_menu_ctrlC_handler(self, sig, frame):
        Output.red('Control C used to exit setup before setup was complete')
        sys.exit(0)
