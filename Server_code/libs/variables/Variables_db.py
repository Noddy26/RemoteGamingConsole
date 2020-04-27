import os
import sqlite3
import sys

from libs.Console.Terminal import Output
from libs.Database_functions.Database_file import DatabaseLite
from libs.Database_functions.Encryt import Encryption
from libs.FileFuctions.FilePaths import FilePaths
from libs.variables.Configuration import Configuration


class VariableDb():

    def __init__(self):
        if not self.check_db():
            Output.red("Configuration error: Please run. --setup ")
            sys.exit(0)

        db = DatabaseLite(Configuration.database_file)
        try:
            result = db.select('*', Configuration.database_table)
            for record in result:
                key = record[0]
                value = record[1]
                if str(value).__contains__("="):
                    value = Encryption.decrypt(value)

                setattr(Configuration, key, value)

        except(sqlite3.DatabaseError):
            if FilePaths.path_exists(Configuration.database_file):
                os.remove(Configuration.database_file)
                Output.red("File Deleted")
            Output.red("This is not a database file. Run --setup to create new file.")
        finally:
            db.close()

    def check_db(self):
        if not FilePaths.path_exists(Configuration.database_file):
            return False
        else:
            return True
