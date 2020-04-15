from libs.Console.Terminal import Output


class Confirm(object):
    @staticmethod
    def confirm(message=None):
        if (message == None):
            message = "Are you sure?"
        yes = ['Yes']
        no = ['No']
        while True:
            Output.yellow(message + " [Yes] to confirm or [No] to cancel: ")
            user_input = input('')
            if (user_input in yes):
                return True
            elif (user_input in no):
                return False
            else:
                Output.red("invaild input")