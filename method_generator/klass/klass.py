class Klass:
    """
    represents a C++ class
    """

    def __init__(self, name):
        self._name = name
        self._methods = []
        self._template = None
        self._namespace = None

    @property
    def name(self):
        return self._name

    @property
    def methods(self):
        return self._methods

    def add_method(self, method):
        self._methods.append(method)

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        self._template = template

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        self._namespace = namespace











