from libs.Start_up.Check_root import CheckRoot
from libs.Start_up.CommandlineArgs import VariableOption
from libs.variables.Variables_db import VariableDb


class StartUp:

    def __init__(self):

        CheckRoot()

        # Logger() - Coming soon

        VariableOption()

        VariableDb()
