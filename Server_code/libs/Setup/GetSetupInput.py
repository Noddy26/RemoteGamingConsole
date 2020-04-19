import sys

from libs.Setup.Confirm import Confirm
from libs.Setup.Get_input import GetInput
from libs.parameters.Parameters import Parameter
from libs.Console.Terminal import Output


class GetSetupInputs:
    def __init__(self, parameters_dictionary):
        self.parameter_list = list()
        for each in parameters_dictionary:
            parameter = Parameter(each)
            self.parameter_list.append(parameter)
    def get(self):
        try:
            for parameter in self.parameter_list:
                if GetInput(parameter).get() is False:
                    break
            if (not GetSetupInputs.confirm(self.parameter_list)):
                Output.red("Run --setup again")
                sys.exit(0)
        except:
            pass

        return self.parameter_list

    @staticmethod
    def confirm(parameters):
        Output.green("You have just provided the following information.")
        for each in parameters:
            if type(each.input_user) != str:
                each.input_user = ''
            if each.confidential is True:
                value = '*' * 15
            else:
                value = each.input_user

            Output.white("\t%s: %s" % (each.displaying_name, value))
        return Confirm.confirm('Verify the information shown above')
