class Method:
    """
    represents a C++ class method
    """

    def __init__(self):
        self._name = None
        self._arguments = []
        self._return_type = None
        self._template = None
        self._class = None
        self._is_const = False
        self._is_pure_virtual = False

        self._options = {
            "newline_after_template": False,
            "newline_after_method": False,
            "place_cursor_between_brackets": False
        }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def arguments(self):
        return self._arguments

    def add_argument(self, argument):
        self._arguments.append(str(argument))

    @property
    def return_type(self):
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        self._return_type = return_type

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        self._template = template

    @property
    def related_class(self):
        return self._class

    @related_class.setter
    def related_class(self, related_clas):
        self._class = related_clas

    @property
    def is_const(self):
        return self._is_const

    @is_const.setter
    def is_const(self, is_const):
        self._is_const = is_const

    @property
    def is_pure_virtual(self):
        return self._is_pure_virtual

    @is_pure_virtual.setter
    def is_pure_virtual(self, is_pure_virtual):
        self._is_pure_virtual = is_pure_virtual

    @property
    def options(self):
        return self._options

    def add_option(self, option, value):
        self._options[option] = value

    def __str__(self):
        """
        renders full method definition with all components
        :return: str
        """

        # creating empty method string to fill
        method = ""

        # check if class has template
        # place newline after each template if option is set
        if self._class.template is not None:
            method += str(self._class.template)
            if self._options["newline_after_template"]:
                method += "\n"
            else:
                method += " "

        # check if method has template
        # place newline after method if option is set
        if self._template is not None:
            method += str(self.template)
            if self._options["newline_after_template"]:
                method += "\n"
            else:
                method += " "

        # make sure to leave space between the definition components
        if self._return_type is not None:
            method += self._return_type + " "

        # insert 2 colons if class has namespace
        if self._class.namespace is not None:
            method += self._class.namespace + "::"

        method += self._class.name

        # render class templates; merging the template types
        if self._class.template is not None:
            class_template_types = []
            for template_type in self._class.template.template_types:
                class_template_types.append(str(template_type.name))

            method += "<{}>".format(', '.join(class_template_types))

        # connecting again the definition components
        method += "::"
        method += self._name

        # create list comprehension from method arguments
        # make sure to strip every argument
        if self._arguments:
            self._arguments = [x.strip() for x in self._arguments]
            self._arguments = ', '.join(self._arguments)
        else:
            self._arguments = ""

        # insert arguments
        method += "({}) ".format(self._arguments)

        # place newline after if option is set
        if self._options["newline_after_method"]:
            method += "\n"

        # place newline and tab after brackets, so cursor is placed between the brackets
        if self._options["place_cursor_between_brackets"]:
            method += "{\n\t}"
        else:
            method += "{}"

        # strip to only make sure, there are no spaces at begin and end of definition
        return method.strip()