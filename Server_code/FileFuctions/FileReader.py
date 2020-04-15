from Server_code.Console.Terminal import Output
from Server_code.FileFuctions.FilePaths import FilePaths
from Server_code.FileFuctions.YamlReader import YamlReader


class FileReader(object):
    def __init__(self, file_path, second_peek=None):
        super(FileReader, self).__init__()

        self.file_types = list()
        self.file_types.append(YamlReader)
        #self.file_types.append(JsonReader)
        #self.file_types.append(ConfReader)

        self.file_path = file_path
        self.second_peek = second_peek


    def get(self):
        if (type(self.file_path) == type(dict())):
            return self.file_path

        reader = None
        for each in self.file_types:
            extension = FilePaths.get_extension(self.file_path)
            if (each.extension() == extension):
                reader = each
                break

        if (reader == None):
            Output.red("Cannot recognize the file type of the file: %s" % (self.file_path))

        if FilePaths.path_exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = reader.load(f)
            return data
        else:
            Output.red("File path invalid: %s" % (self.file_path))