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

# tests = read_files_as_tokenizers()
# test_method = tests[0].methods[1]
# print(str(test_method))
# a = 1


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


class TestMethodParser:

    def test_method_parsing(self):

        test_files = read_files_as_tokenizers()

        methods_0 = test_files[0].methods

        assert len(methods_0) == 14
        assert len(methods_0[0].arguments) == 0
        assert len(methods_0[1].arguments) == 2
        assert len(methods_0[2].arguments) == 0
        assert len(methods_0[3].arguments) == 1
        assert methods_0[3].arguments[0] == "std::string name"
        assert len(methods_0[4].arguments) == 0
        assert methods_0[4].is_const == True
        assert methods_0[5].is_pure_virtual == True
        assert len(methods_0[6].arguments) == 0
        assert methods_0[6].return_type == "void"
        assert str(methods_0[10].template) == "template <typename T>"

        # testing full output from methods
        assert methods_0[0].render() == "template <class T, typename D> sf::sd::User<T, D>::User() {}"
        assert methods_0[1].render() == "template <class T, typename D> sf::sd::User<T, D>::User(std::string name, int skillLevel) {}"
        assert methods_0[2].render() == "template <class T, typename D> sf::sd::User<T, D>::~User() {}"
        assert methods_0[3].render() == "template <class T, typename D> void sf::sd::User<T, D>::setName(std::string name) {}"
        assert methods_0[4].render() == "template <class T, typename D> std::string sf::sd::User<T, D>::getName() {}"
        assert methods_0[6].render() == "template <class T, typename D> void sf::sd::User<T, D>::move() {}"
        assert methods_0[7].render() == "template <class T, typename D> GameState* sf::sd::User<T, D>::getGameState() {}"
        assert methods_0[8].render() == "template <class T, typename D> GameRef& sf::sd::User<T, D>::getGameRef() {}"
        assert methods_0[9].render() == "template <class T, typename D> SuperPower* sf::sd::User<T, D>::getSuperPower() {}"
        assert methods_0[10].render() == "template <class T, typename D> template <typename T> T sf::sd::User<T, D>::getEnemy() {}"
        assert methods_0[11].render() == "template <class T, typename D> template <typename T> T sf::sd::User<T, D>::getSomethingElse() {}"
        assert methods_0[12].render() == "template <class T, typename D> void sf::sd::User<T, D>::foo() {}"
        assert methods_0[13].render() == "template <class T, typename D> void sf::sd::User<T, D>::stop() {}"