import argparse
import sys

from Server_code.Setup.setup import Setup
from Server_code.Start_up.HelpMenu import Help
from Server_code.Start_up.version import GetVersion


class VariableOption():

    def __init__(self):

        parser = argparse.ArgumentParser()

        main_group = parser.add_argument_group()

        main_group.add_argument("-v", "--version", action="store_true", default=False,
                                help="display version information")
        main_group.add_argument("-s", "--setup", action="store_true", default=False,
                                help="sets up the tool")
        main_group.add_argument("-h", "--help", action="store_true", default=True,
                                help="Displays command line options")

        newList = sys.argv[2:]
        args = parser.parse_args(newList)

        for each in newList:
            if (each == "--setup" or each == "-s") and (len(sys.argv[2:]) > 1):
                parser.error("argument -s/--setup: not allowed with other arguments")
            elif (each == "--version" or each == "-v") and (len(sys.argv[2:]) > 1):
                parser.error("argument -v/--version: not allowed with other arguments")


        if (args.version):
            GetVersion()
            sys.exit()

        if (args.setup):
            Setup.setup()
            sys.exit()

        if (args.help):
            Help()
            sys.exit()
