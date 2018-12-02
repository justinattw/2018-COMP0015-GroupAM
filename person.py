class Person:

    """
    Constants
    """
    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 15

    MIN_VOTE = 0
    MAX_VOTE = 100

    def __init__(self, name, votes={}):
        self.name = name
        self.votes = votes

    def __str__(self):
        return 'Name: ' + self.name + '\nVotes: ' + str(self.votes)

    def __repr__(self):
        return 'Name: ' + self.name + ', Votes: ' + str(self.votes)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """
        We don't allow empty names
        """
        if name.isalpha():
            self._name = name
        else:
            raise ValueError('Name must consist of alphabetical characters')

    def is_valid_person_name(person_name, minimum=MIN_NAME_LENGTH, maximum=MAX_NAME_LENGTH):
        """
        Check the string contains only characters from the alphabet
        and check that it is the right length.

        :param the_string: the string to be validated
        :param isalpha: ensures only alphabetical characters
        :param minimum: the minimum length of the string
        :param maximum: the maximum length of the string
        :returns: True if the string conforms to the conditions and False if it does not.
        """
        return person_name.isalpha() and minimum <= len(person_name) <= maximum

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, votes):
        self._votes = votes

    def is_valid_vote(self, vote, minimum=MIN_VOTE, maximum=MAX_VOTE):
        """ Checks if the vote is an integer and falls betwen the minimum and maximum.
        Minimum is 0 and maximum is 100 by default.

        @return boolean value
        """
        if not points.isInteger():
            raise TypeError('Vote must be an integer')
        if minimum <= int(points) <= maximum:
            raise ValueError(('Vote must be between {} and {}').format(self.MIN_VOTE, self.MAX_VOTE))
        else:
            return True

    def vote_for(self, voter_name, vote_value):
        self._votes[voter_name] = vote_value
