from method_generator.generator import Generator
from method_generator.exceptions import ClassValidationException
import os


def read_files_as_method_generators():
    test_files = [
        os.path.abspath("tests/files/User.hpp"),
        os.path.abspath("tests/files/Window.hpp")
    ]

    files_list = []

    for file in test_files:
        with open(file, 'r') as f:
            file = f.read()
            try:
                generator = Generator(file)
                files_list.append({
                    'definitions': generator.generate_method_list(generator.DEFINITIONS),
                    'names': generator.generate_method_list(generator.NAMES)
                })
            except ClassValidationException as e:
                print(str(e))

    return files_list


class TestGenerator:

    def test_has_correct_list_items(self):

        test_files = read_files_as_method_generators()

        mg0_definitions = test_files[0]['definitions']
        mg1_definitions = test_files[1]["definitions"]

        mg0_names = test_files[0]['names']
        mg1_names = test_files[1]['names']

        assert len(mg0_definitions) == 13
        assert len(mg1_definitions) == 3

        assert len(mg0_names) == 13
        assert len(mg1_names) == 3

        assert len(mg0_names) == len(mg0_definitions)
        assert len(mg1_names) == len(mg1_definitions)

