from .datatype import Datatype


class TemplateType(Datatype):
    """
    represents a template type
    """

    def __init__(self, typename, name):
        super(TemplateType, self).__init__(name)

        self._typename = typename

    @property
    def typename(self):
        return self._typename

    @typename.setter
    def typename(self, typename):
        self._typename = typename

    def __str__(self):
        """
        renders template type with datatype and placeholder
        :return: str
        """

        return "{typename} {datatype}".format(typename=self._typename, datatype=self._name)