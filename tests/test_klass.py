from class_generator import ClassGenerator

FILES = [
    "files/dynamicmap.json",
    "files/user.json"
]


def test_method_rendering():
    for file in FILES:
        generator = ClassGenerator(file)
        for method in generator.generate():
            assert str(method["method"]) == method["expected"]
