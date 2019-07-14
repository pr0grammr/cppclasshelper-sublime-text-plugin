class Datatype:
    """
    represents a datatype
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        """
        renders datatype name
        :return: str
        """

        return self._name