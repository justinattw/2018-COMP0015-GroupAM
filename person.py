class Person:

    """ Constants used to validate inputs in main program, including
        person_name and vote values.
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
        return '\nMember name: ' + self.name + ',\tVotes: ' + str(self.votes)

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

    def is_valid_vote(vote, minimum=MIN_VOTE, maximum=MAX_VOTE):
        """ Checks if the vote is an integer and falls betwen the
            minimum and maximum.
            Minimum and maximum are constants set at the start
            of this module.

        @return boolean value
        """
        # if not Person.is_integer(vote):
        #     raise TypeError ('Vote must be an integer')
        #     return False
        # if not minimum <= int(vote) <= maximum:
        #     raise ValueError(('Vote must be between {} and {}')
        #                       .format(minimum, maximum))
        #     return False

        return Person.is_integer(vote) and minimum <= int(vote) <= maximum

    def is_integer(number):
        """ Checks if an input is an is_integer

        @return boolean value
        """
        try:
            int(number)
            return True
        except ValueError:
            return False

    def vote_for(self, voter_name, vote_value):
        self._votes[voter_name] = vote_value

    def get_name(self):
        return self.name

    def get_votes(self):
        return self.votes
