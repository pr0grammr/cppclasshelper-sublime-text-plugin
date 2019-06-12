class Method:

    def __init__(self):
        self._name = None
        self._arguments = []
        self._return_type = None
        self._template = None
        self._keywords = []
        self._operator = None
        self._class = None

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
    def keywords(self):
        return self._keywords

    def add_keyword(self, keyword):
        self._keywords.append(keyword)

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator

    @property
    def related_class(self):
        return self._class

    @related_class.setter
    def related_class(self, related_clas):
        self._class = related_clas

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

        if not self._keywords:
            self._keywords = ""

        return template.format(
            template=self._template,
            return_type=self._return_type,
            operator=self._operator,
            namespace=namespace,
            class_name=self._class.name,
            template_types=method_template,
            method_name=self._name,
            arguments=', '.join(self._arguments),
            keywords=' '.join(self._keywords)
        ).strip()