from .tokenizer import *
from .parser import *


class Generator:
    """
    generates all class method definitions
    """

    DEFINITIONS = 1
    NAMES = 2

    def __init__(self, source_code):
        self._source_code = source_code

    def _generate_method_display_name(self, method):

        if method.return_type is None:
            method.return_type = ""

        return "{} {}".format(method.return_type, method.name)

    def generate_method_list(self, return_mode):
        """
        generates a list of methods
        only includes the method names
        :param return_mode:
        :return: list
        """

        tokenized_source_code = ClassTokenizer().tokenize(self._source_code)
        klass = ClassParser().parse(tokenized_source_code)

        method_names_list = []
        method_definitions_list = []

        for method in klass.methods:

            if method.is_pure_virtual:
                continue

            key = self._generate_method_display_name(method)
            method_names_list.append(key)
            method_definitions_list.append(str(method))

        if return_mode == self.DEFINITIONS:
            return method_definitions_list
        elif return_mode == self.NAMES:
            return method_names_list
