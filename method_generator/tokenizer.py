import re
from .exceptions import ClassValidationException


class Tokenizer:

    """
    base tokenizer
    """

    @classmethod
    def tokenize(cls, input_str):
        pass


class ClassTokenizer(Tokenizer):

    """
    class tokenizer
    creates tokens for all class components
    """
    @classmethod
    def tokenize(cls, input_str):

        # strip comments and keywords
        input_str = cls._strip_class_metadata(input_str)

        class_context = re.search(r"class\s+([A-Za-z]+[0-9]*)\s*\{(.*)\}[;]*", input_str, re.DOTALL)
        cls._class_obj = {}

        if class_context is None:
            raise ClassValidationException("Class context could not be parsed")
        else:
            cls._class_obj["name"] = class_context.group(1)
            class_context = class_context.group(2)

            # parse all class members with various tokenizers
            try:
                cls._class_obj["namespace"] = NamespaceTokenizer().tokenize(input_str)
                cls._class_obj["template"] = TemplateTokenizer().tokenize(input_str)
                cls._class_obj["name"] = cls._parse_class_name(input_str)
                cls._class_obj["methods"] = MethodTokenizer().tokenize(class_context)

            except ClassValidationException as e:
                raise ClassValidationException(str(e))

            return cls._class_obj

    @classmethod
    def _strip_class_metadata(cls, input_str):
        """
        strip comments and access keywords
        :return: void
        """
        input_str = re.sub(r"(//(.*)\n+)", "", input_str)
        input_str = re.sub(r"\/\*{1,2}(.|\n)*?\*\/", "", input_str, re.DOTALL)
        input_str = re.sub(r"(public:|private:|protected:)", "", input_str, re.DOTALL)

        return input_str

    @classmethod
    def _parse_class_name(cls, input_str):
        """
        get name of class
        :return: str
        """
        match = re.search(r"class\s+([A-Za-z]+[0-9]*)\s*\{", input_str)
        if match is not None:
            return match.group(1)


class NamespaceTokenizer:

    """
    namespace tokenizer
    creates tokens for class namespace
    """
    @classmethod
    def tokenize(cls, input_str):
        """
        parses namespace ans returns name of namespace with delimiter as string

        :raises ClassValidationException
        :param input_str:
        :return:
        """

        match = re.search(r"(namespace)\s+([\w:]+)", input_str)

        if match and match.group(2) is None and match.group(1) is None:
            raise ClassValidationException("Could not parse class namespace")

        if match and match.group(2) is not None:
            return match.group(2)

        return None


class TemplateTokenizer:

    """
    template tokenizer
    creates tokens for method or class template
    """
    @classmethod
    def tokenize(cls, input_str):
        """
        parses method or class template and returns dict with placeholder name
        and placeholder datatype

        :raises ClassValidationException
        :param input_str:
        :return: dict
        """
        match = re.search(r"(template){1}\s+<(.*)>", input_str)

        if not match:
            return None

        if match and match.group(1) is None and match.group(2) is None:
            raise ClassValidationException("Could not parse template")

        typenames = []

        # iterate over typenames defined in template to fetch template datatypes
        for typename in match.group(2).split(','):
            typename = typename.strip().split(' ')

            typenames.append({
                "typename": typename[0].strip(),
                "datatype": typename[1].strip()
            })

        return typenames


class MethodTokenizer(Tokenizer):

    """
    method tokenizer
    creates tokens for all class methods
    """
    # class constants
    KEYWORD_PURE_VIRTUAL = "= 0"
    KEYWORD_CONST = "const"
    KEYWORD_METHOD_PREFIXES = ["virtual", "friend"]

    @classmethod
    def tokenize(cls, input_str):

        methods = []

        # split after every semicolon to get all class members
        for method in input_str.split(';'):
            method = method.strip()

            if not method:
                continue

            # check if class member is a method
            method_match = re.search(r"\((.*)\)(.*)$", method.strip())

            if method_match is not None and method_match.group(1) is not None:

                # set method dict to fill
                # set default properties
                method_dict = {
                    "is_const": False,
                    "is_pure_virtual": False
                }

                # find part before opening and closing brackets
                method_name_parts = re.search(r"(.*)\(.*\)", method, re.DOTALL)

                if method_name_parts is None:
                    continue

                method_name_parts = method_name_parts.group(1)
                method_name_parts_split = method_name_parts.split(' ')

                # check if method might be a contructor or destructor and set method name equal to first key
                if len(method_name_parts) == 1:
                    method_name = method_name_parts_split[0]
                else:
                    method_name = method_name_parts_split[-1]

                method_dict["name"] = method_name

                if cls._is_constructor_or_destructor(method_name_parts):
                    method_dict["return_type"] = None
                else:
                    method_dict["return_type"] = cls._parse_return_type(method_name_parts_split)

                # check if method is a pure virtual method
                if method_match.group(2) is not None:

                    # check if method is const
                    if cls.KEYWORD_CONST in method_match.group(2):
                        method_dict["is_const"] = True

                    # check if method is a pure virtual method
                    if cls.KEYWORD_PURE_VIRTUAL in method_match.group(2):
                        method_dict["is_pure_virtual"] = True

                # parse template
                method_dict["template"] = TemplateTokenizer().tokenize(method_name_parts)

                # get method arguments and pass it to dict like in the method signature
                method_arguments = re.search(r".*\((.*)\)", method)
                method_dict["arguments"] = None
                if method_arguments is not None and method_arguments.group(1) is not None:
                    method_dict["arguments"] = [x.strip() for x in method_arguments.group(1).split(',')]

                # append method dict to methods list
                methods.append(method_dict)

        return methods

    @classmethod
    def _parse_return_type(cls, method_parts):
        """
        parse return type of method
        :param method_parts:
        :return: str
        """

        # check if first key is a reserved keyword like friend or virtual
        if len(method_parts) == 1:
            return method_parts[0]

        return method_parts[-2]

    @classmethod
    def _is_constructor_or_destructor(cls, method_name):
        """
        check if method name is constructor or destructor
        :param method_name:
        :return: bool
        """
        return len(method_name.split(' ')) == 1
