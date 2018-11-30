class Person:
    def __init__(self, name):
        self._name = name
        self._votes = {}

    @property
    def name(self):
        return self._name

    @property
    def votes(self):
        return self._votes

    def vote_for(self, voter_name, vote_value):
        self._votes[voter_name] = vote_value

    def __str__(self):
        return ("Name: " + self.name + ", votes: " + self.votes)
