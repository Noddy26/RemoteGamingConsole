from Server_code.Console.Terminal import Output
from Server_code.FileFuctions.TypeCheck import TypeCheck


class Dictionary(object):
    @staticmethod
    def set_value(dictionary, key, value):
        TypeCheck.dict(dictionary)
        TypeCheck.str(key)
        dictionary[key] = value
        return True

    @staticmethod
    def get_value(dictionary, key, default=Exception(), file_path=None, type=None, add_default=False):

        if not (TypeCheck.dict(dictionary) & TypeCheck.str(key)):
            Output.red("The argument's type is not correct")

        try:
            value = dictionary[key]
            if (type != None):
                TypeCheck.type(type, value, key, file_path)
        except KeyError:
            if (isinstance(default, Exception)):

                # If default value is not set
                Output.red("The dictionary:")
                Output.white(dictionary)
                Output.red("was supposed to have the key: '%s'" % key)
                if (file_path == None):
                    raise KeyError(
                        "Cannot locate the YAML file which contains this key error. Check the previous output for the wrong type.")
                else:
                    Output.red("This error occurred in the YAML file '%s'" % (file_path))
            else:
                value = default
                if (add_default):
                    Dictionary.set_value(dictionary, key, value)

        return value

    @staticmethod
    def remove_key(dictionary, key):
        try:
            del dictionary[key]
        except KeyError:
            pass
        return dictionary