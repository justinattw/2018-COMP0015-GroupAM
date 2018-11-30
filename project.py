class Project:
    def __init__(self, name, members):
        self._name = name
        self._members = members

    @property
    def name(self):
        return self._name

    @property
    def members(self):
        return self._members
