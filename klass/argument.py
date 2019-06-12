from .datatype import Datatype


class Argument(Datatype):

    def __init__(self):
        super(Argument, self).__init__()

        self._operator = None
        self._keyword = None

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        self._keyword = keyword

    def __str__(self):
        template = SETTINGS["method"]["argument"]

        return template.format(
            keyword=self._keyword,
            identifier=self._identifier,
            operator=self._operator,
            datatype=self._datatype
        )