import yaml

from libs.FileFuctions.FileType import FileType

class YamlReader(FileType):

    @staticmethod
    def load(file):
        FileType.check(file, YamlReader.extension())
        return yaml.safe_load(file)

    @staticmethod
    def extension():
        return ".yml"

    @staticmethod
    def file_type():
        return 'YAML'
