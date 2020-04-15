import os

from Server_code.Database_functions.Database_file import Database
from Server_code.Console.Terminal import Output
from Server_code.variables.Configuration import Configuration


class StoreDBParameters():
    @staticmethod
    def store(parameters, database_file):
        """
        store the parameters in the database file
        :param parameters: The objects/instances of the class in libs/setup/parameter.py
        :param database_file: The database needs to be edited
        :return:
        """

        db = Database(database_file)
        table = Configuration.database_table

        # drop the original table
        db.drop(table)
        db.create(table, 'key TEXT', 'value TEXT', 'is_confidential TEXT')
        for each in parameters:
            db.insert(table, each.name, each.input, str(each.confidential))
        db.close()

        # only root user has access to the db file
        os.system("chmod %03d '%s'" % (600,  database_file))
        Output.green('parameters stored in database')
