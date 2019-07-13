from method_generator.parser import ClassParser
from method_generator.tokenizer import ClassTokenizer
from method_generator.exceptions import ClassValidationException
import os

def read_files_as_tokenizers():
    test_files = [
        os.path.abspath("tests/files/User.hpp"),
        os.path.abspath("tests/files/Window.hpp")
    ]

    files_list = []

    for file in test_files:
        with open(file, 'r') as f:
            file = f.read()
            try:
                token_object = ClassTokenizer().tokenize(file)
                files_list.append(ClassParser().parse(token_object))
            except ClassValidationException as e:
                print(str(e))

    return files_list


class TestClassParser():

    def test_has_namespace(self):

        test_files = read_files_as_tokenizers()

        assert test_files[0].namespace == "sf::sd"