from Server_code.FileFuctions.FileReader import FileReader
from Server_code.parameters.Dictionary import Dictionary
from Server_code.Setup.GetSetupInput import GetSetupInputs
from Server_code.parameters.StoreDBParameters import StoreDBParameters
from Server_code.Console.Terminal import Output
from Server_code.variables.Configuration import Configuration


class Setup():

    @staticmethod
    def setup():
        file_path = Configuration.setup_detail_file
        setup_detail = FileReader(file_path).get()
        Output.red("WARNING All Data in database file will get overridden if you have already run setup.")
        parameter_dict = Dictionary.get_value(setup_detail, 'parameters', type=list, file_path=file_path)
        parameters = GetSetupInputs(parameter_dict).get()

        db_parameters = list()
        for each in parameters:
            if each.stored_in_db:
                db_parameters.append(each)

        # store inputs database
        StoreDBParameters.store(db_parameters, Configuration.database_file)

        # setup complete
        Output.green(Dictionary.get_value(setup_detail, 'last_message', '', type=str))

Setup.setup()