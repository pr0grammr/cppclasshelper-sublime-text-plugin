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

    def __str__(self):

        template = "{template} {return_type} {namespace}{class_name}{template_types}::{method_name}({arguments}){keywords} {{}}"

        method_template = []

        if self._class.template:
            for template_type in self._class.template.template_types:
                method_template.append(str(template_type.name))

        if not self._template:
            self._template = ""

        if self._class.template:
            method_template = "<{}>".format(', '.join(method_template))
        else:
            method_template = ""

        if self._class.namespace:
            namespace = self._class.namespace + "::"
        else:
            namespace = ""

        return template.format(
            template=self._template,
            return_type=self._return_type,
            namespace=namespace,
            class_name=self._class.name,
            template_types=method_template,
            method_name=self._name,
            arguments=', '.join(self._arguments),
        ).strip()