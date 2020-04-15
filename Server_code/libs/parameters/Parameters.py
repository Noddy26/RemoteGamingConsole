from libs.parameters.Dictionary import Dictionary


class Parameter():
    name = 'name'
    displaying_name = 'displaying_name'
    prompt = 'prompt'
    default = 'default'
    confidential = 'confidential'
    stored_in_db = 'stored_in_db'

    def __init__(self, parameter_dict):
        self.name = Dictionary.get_value(parameter_dict, Parameter.name)
        self.displaying_name = Dictionary.get_value(parameter_dict, Parameter.displaying_name, default=self.name,
                                                    type=str)
        self.prompt = Dictionary.get_value(parameter_dict, Parameter.prompt, default=None, type=str)
        self.default = Dictionary.get_value(parameter_dict, Parameter.default, default=None, type=str)
        self.confidential = Dictionary.get_value(parameter_dict, Parameter.confidential, default=False)
        self.stored_in_db = Dictionary.get_value(parameter_dict, Parameter.stored_in_db, default=False)
        self.input = None