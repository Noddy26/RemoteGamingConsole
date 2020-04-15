from Server_code.Setup.Confirm import Confirm
from Server_code.Setup.Get_input import GetInput
from Server_code.parameters.Parameters import Parameter
from Server_code.Console.Terminal import Output
from Server_code.Setup.setup import Setup


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
                del self.parameter_list[:]
                Setup.setup()
        except:
            pass

        return self.parameter_list

    @staticmethod
    def confirm(parameters):
        Output.green("You have just provided the following information.")
        for each in parameters:
            if type(each.input) != str:
                each.input = ''
            value = each.input
            if len(value) == 0:
                # print out eight stars to represent the password
                value = ''
            elif each.confidential:
                value = '*' * 8

            Output.white("\t%s: %s" % (each.displaying_name, value))
        return Confirm.confirm('Verify the information shown above')
