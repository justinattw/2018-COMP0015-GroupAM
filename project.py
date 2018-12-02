class Project:

    """
    Constants used to validate project name and team sizes
    """
    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 15

    MIN_TEAM_SIZE = 3
    MAX_TEAM_SIZE = 5

    def __init__(self, project_name, project_size, project_members):
        self._name = project_name
        self._size = project_size
        self._members = project_members

    def __str__(self):
        return "Name: " + self.name + "\nSize: " + str(self.size) + "\nMembers: " \
                + str(self.members)

    def __repr__(self):
        return '\n{Project Name: ' + self.name + ', Size: ' + str(self.size) + \
                 ', Members: ' + str(self.members) + '}'


    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, project_name, minimum=MIN_NAME_LENGTH, maximum=MAX_NAME_LENGTH):
    #     if self.is_valid_project_name(project_name) == False:
    #         raise ValueError(("Project name must be between {} and {} "
    #                           "characters long.")
    #                           .format(str(minimum), str(maximum)))
    #     self._name = project_name

    def is_valid_project_name(project_name, minimum=MIN_NAME_LENGTH, maximum=MAX_NAME_LENGTH):
        """
        Check the string contains the allowable length. We allow non-alphabetical characters

        :param project_name: the string to be validated
        :param minimum: the minimum length of project_name
        :param maximum: the maximum length of project_name
        :returns: True if the string conforms to the conditions and False if it does not.
        """
        return minimum <= len(project_name.strip()) <= maximum

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, project_size, minimum=MIN_TEAM_SIZE, maximum=MAX_TEAM_SIZE):
        if not self.is_valid_team_size(project_size):
            raise ValueError (("Team size must be between {} and {}")
                               .format(str(minimum), str(maximum)))
        self._size = project_size

    def is_valid_team_size(team_size, minimum=MIN_TEAM_SIZE, maximum=MAX_TEAM_SIZE):
        """ Checks whether the team size is greater than or equal to the minimum size
        and less than or equal to the maximum size.

        :param team_size: the team size we are checking against
        :param minimum: minimum team size allowed
        :param maximum: maximum team size allowed
        @returns: True or False.
        """
        return Project.is_integer(team_size) and minimum <= int(team_size) <= maximum

    def is_integer(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, project_members):
        if len(project_members) == self.size:
            self._members = project_members

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_members(self):
        return self.members
