class Method:

    def __init__(self):
        self._name = None
        self._arguments = []
        self._return_type = None
        self._template = None
        self._class = None
        self._is_const = False
        self._is_pure_virtual = False

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

    def render(self):

        # creating empty method string to fill
        method = ""

        if self._class.template is not None:
            method += str(self._class.template) + " "

        if self._template is not None:
            method += str(self.template) + " "

        if self._return_type is not None:
            method += self._return_type + " "

        if self._class.namespace is not None:
            method += self._class.namespace + "::"

        method += self._class.name

        if self._class.template is not None:
            class_template_types = []
            for template_type in self._class.template.template_types:
                class_template_types.append(str(template_type.name))

            method += "<{}>".format(', '.join(class_template_types))

        method += "::"
        method += self._name

        if self._arguments:
            self._arguments = [x.strip() for x in self._arguments]
            self._arguments = ', '.join(self._arguments)
        else:
            self._arguments = ""

        method += "({})".format(self._arguments)
        method += " {}"

        return method.strip()