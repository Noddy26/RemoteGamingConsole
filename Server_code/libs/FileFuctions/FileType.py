from libs.Console.Terminal import Output
from libs.FileFuctions.FilePaths import FilePaths


class FileType(object):
    @staticmethod
    def extension():
        pass

    @staticmethod
    def load(file):
        pass

    @staticmethod
    def check(file, ext):
        if (ext != FilePaths.get_extension(file.name)):
            Output.red("File name: %s\nExtension expected: %s" % (file.name, ext))
            Output.red("The file extension does not match this file type.")

    @staticmethod
    def file_type():
        return ''