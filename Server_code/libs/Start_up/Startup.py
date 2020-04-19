from libs.Start_up.Check_root import CheckRoot
from libs.Start_up.CommandlineArgs import VariableOption
from libs.variables.Variables_db import VariableDb
from libs.Start_up.Read_Paths import ReadPaths
from libs.Server_logging.Logging import Logger


class StartUp:

    def __init__(self):

        CheckRoot()

        Logger()

        ReadPaths()

        VariableOption()

        VariableDb()
