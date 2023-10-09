

class Station:
    def __init__(self, name: str, code: str):
        self._name = name
        self._code = code

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code
