from libs.FileFuctions.FileReader import FileReader
from libs.parameters.Dictionary import Dictionary
from libs.Setup.GetSetupInput import GetSetupInputs
from libs.parameters.StoreDBParameters import StoreDBParameters
from libs.Console.Terminal import Output
from libs.variables.Configuration import Configuration


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
