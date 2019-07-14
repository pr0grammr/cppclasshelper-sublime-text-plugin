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
                files_list.append(ClassTokenizer().tokenize(file))
            except ClassValidationException as e:
                print(str(e))

    return files_list

# tests = read_files_as_tokenizers()
# a = 1


class TestClassTokenizer:

    def test_name_parsing(self):

        test_files = read_files_as_tokenizers()

        assert test_files[0]["name"] == "User"
        assert test_files[1]["name"] == "Window"


class TestTemplateTokenizer:

    def test_has_template(self):

        test_files = read_files_as_tokenizers()

        assert test_files[0]["template"][0]["typename"] == "class"
        assert test_files[0]["template"][0]["datatype"] == "T"

        assert test_files[0]["template"][1]["typename"] == "typename"
        assert test_files[0]["template"][1]["datatype"] == "D"

        assert test_files[1]["template"] == None


class TestNamespaceTokenizer:

    def test_has_namespace(self):

        test_files = read_files_as_tokenizers()

        assert test_files[0]["namespace"] == "sf::sd"
        assert test_files[1]["namespace"] == "OS"


class TestMethodTokenizer:

    def test_check_method_names(self):

        test_files = read_files_as_tokenizers()

        # testing first class methods
        methods_file_0 = test_files[0]["methods"]
        assert len(methods_file_0) == 14

        assert methods_file_0[0]["name"] == "User"
        assert methods_file_0[0]["return_type"] == None
        assert methods_file_0[0]["is_pure_virtual"] == False

        assert methods_file_0[1]["name"] == "User"
        assert methods_file_0[1]["return_type"] == None
        assert methods_file_0[1]["is_pure_virtual"] == False

        assert methods_file_0[2]["name"] == "~User"
        assert methods_file_0[2]["return_type"] == None
        assert methods_file_0[2]["is_pure_virtual"] == False

        assert methods_file_0[3]["name"] == "setName"
        assert methods_file_0[3]["return_type"] == "void"
        assert methods_file_0[3]["is_pure_virtual"] == False

        assert methods_file_0[4]["name"] == "getName"
        assert methods_file_0[4]["return_type"] == "std::string"
        assert methods_file_0[4]["is_pure_virtual"] == False
        assert methods_file_0[4]["is_const"] == True

        assert methods_file_0[5]["name"] == "play"
        assert methods_file_0[5]["return_type"] == "void"
        assert methods_file_0[5]["is_pure_virtual"] == True

        assert methods_file_0[10]["name"] == "getEnemy"
        assert methods_file_0[10]["return_type"] == "T"
        assert methods_file_0[10]["template"][0]["typename"] == "typename"
        assert methods_file_0[10]["template"][0]["datatype"] == "T"


        # testing second class methods
        methods_file_1 = test_files[1]["methods"]
        assert len(methods_file_1) == 3

        assert methods_file_1[2]["return_type"] == "int"
        assert methods_file_1[2]["name"] == "getSize"
        assert methods_file_1[2]["is_pure_virtual"] == False
        assert methods_file_1[2]["is_const"] == False
