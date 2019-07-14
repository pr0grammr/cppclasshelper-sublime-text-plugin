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
        assert test_files[1].namespace == "OS"

    def test_name_parsing(self):

        test_files = read_files_as_tokenizers()

        assert test_files[0].name == "User"
        assert test_files[1].name == "Window"

    def test_template_parsing(self):

        test_files = read_files_as_tokenizers()

        assert str(test_files[0].template) == "template <class T, typename D>"
        assert test_files[1].template == None

    def test_method_parsing(self):

        test_files = read_files_as_tokenizers()

        assert len(test_files[0].methods) == 14
        assert len(test_files[0].methods[0].arguments) == 0
        assert len(test_files[0].methods[1].arguments) == 2
