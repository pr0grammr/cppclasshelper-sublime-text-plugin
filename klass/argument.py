class Argument:

    def __init__(self):
        super(Argument, self).__init__()

        self._datatype = None
        self._operator = None
        self._keyword = None
        self._identifier = None

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

    @property
    def datatype(self):
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        self._datatype = datatype

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        self._identifier = identifier

    def __str__(self):
        template = "{datatype}{operator} {identifier}"

        if not self._operator:
            self._operator = ""

        return template.format(
            keyword=self._keyword,
            identifier=self._identifier,
            operator=self._operator,
            datatype=self._datatype
        )
