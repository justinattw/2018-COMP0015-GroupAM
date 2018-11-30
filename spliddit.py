from enum import Enum
from person import Person
from project import Project

class Menu:

    class Choices(Enum):
        ABOUT = 'A'
        CREATE_PROJECT = 'C'
        ENTER_VOTES = 'V'
        SHOW_PROJECTS = 'S'
        QUIT = 'Q'

    def print(self):
        """ Prints the menu for the application. """
        print("\nWelcome to Spliddit\n")
        description = {
            Menu.Choices.ABOUT: 'About',
            Menu.Choices.CREATE_PROJECT: 'Create Project',
            Menu.Choices.ENTER_VOTES: 'Enter Votes',
            Menu.Choices.SHOW_PROJECTS: 'Show Projects',
            Menu.Choices.QUIT: 'Quit',
        }
        for choice in Menu.Choices:
            print('\t {} ({})'.format(description[choice].ljust(15, ' '),
                                      choice.value))

    def select(self):
        ## Prints the menu, prompts the user for an option and validates the option.
        #
        #  :returns: a character representing the option.

        while True:
            self.print()
            answer = input("\nEnter an option: ").strip()
            try:
                return Menu.Choices(answer.upper())
            except ValueError:
                pass


class Spliddit:
    MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']
    MINIMUM_NAME_LENGTH = 3  # Used to validate team member's name and project name
    MAXIMUM_NAME_LENGTH = 15

    MINIMUM_TEAM_SIZE = 3
    MAXIMUM_TEAM_SIZE = 5

    MIN_VOTE = 0
    MAX_VOTE = 100

    def __init__(self):
        self.projects = {}

    def print_menu(self):
        Menu().print_menu()

    def pick_project(self):
        """ Lets the user pick a project to be voted on from the projects dictionary.

        :returns: a Project object
        """
        if not self.projects:
            print('Please create a project first.')
            return None

        pick_key = input('\n\tEnter the project name: ')
        existing_projects = [i for i in self.projects]
        while pick_key not in self.projects:
            print("\n\tPlease choose from an existing project. "
                  "\n\nAvailable projects: ", end="")
            print(*existing_projects, sep=', ')
            pick_key = input("\n\tEnter project: ")
        return self.projects[pick_key]

    def about(self):
        """Prints a description of the application. """
        about_string = ("\n\nWelcome to Spliddit. "
                        "This application will allocate grades to "
                        "project participants \nbased off the votes of their "
                        "peers.\n"
                        "Based on code by Rae Harbird."
                        "\n\n2018 UCL Antonin Kanat & Justin Wong")
        print(about_string)

    def create_project(self):
        """ Sets up a project from the information entered by the user.

        :returns: a dictionary containing the project name and the names
                  of team members
        """
        project_name = self.get_project_name()
        team_size = self.get_team_size()
        members = self.get_team_names(team_size)
        return Project(project_name, members)

    def get_project_name(self):
        """Prompts the user for a project name and validates it.
        Invariants: a project name must be between the minimum and
                    maximum length and cannot be blank. The name must
                    contain only alphabetic characters.
        :returns: a string containing the project name.
        """
        project_name = input("\n\tEnter project name: ")
        while not self.is_valid_project_name(project_name):
            print(("\n\t\tThe project name must be between {} and {} characters"
                   ". Please try again.\n")
                   .format(self.MINIMUM_NAME_LENGTH, self.MAXIMUM_NAME_LENGTH))
            project_name = input("\n\tEnter project name: ")
        return project_name

    def is_valid_person_name(self, the_string, minimum=MINIMUM_NAME_LENGTH, maximum=MAXIMUM_NAME_LENGTH):
        """
        Check the string contains only characters from the alphabet
        and check that it is the right length.

        :param the_string: the string to be validated
        :param minimum: the minimum length of the string
        :param maximum: the maximum length of the string
        :returns: True if the string conforms to the conditions and False if it does not.
        """
        return the_string.isalpha() and minimum <= len(the_string) <= maximum

    def is_valid_project_name(self, the_string, minimum=MINIMUM_NAME_LENGTH, maximum=MAXIMUM_NAME_LENGTH):
        """
        Check the string contains the allowable length.

        :param the_string: the string to be validated
        :param minimum: the minimum length of the string
        :param maximum: the maximum length of the string
        :returns: True if the string conforms to the conditions and False if it does not.
        """
        return minimum <= len(the_string) <= maximum

    def get_team_size(self):
        """ Prompts the user for the team size and validates it.
        Invariants: the team size must be between the minimum and maximum size.

        :returns: the number of people in the team.
        """
        team_size = input("\n\tEnter the number of team members: ")

        while not self.is_valid_team_size(team_size):
            print(("\n\t\tThe team size must be between {} and {}. Please try "
                   "again.")
                   .format(self.MINIMUM_TEAM_SIZE, self.MAXIMUM_TEAM_SIZE))
            team_size = input("\n\tEnter the number of team members: ")

        return int(team_size)

    def is_valid_team_size(self, size, minimum=MINIMUM_TEAM_SIZE, maximum=MAXIMUM_TEAM_SIZE):
        """ Checks whether the team size is greater than or equal to the minimum size
        and less than or equal to the maximum size.
        @return True or False.
        """
        try:
            return minimum <= int(size) <= maximum
        except ValueError:
            return False

    def get_team_names(self, team_size):
        """Gets the names for the people in the team and creates according
        Person objects. Duplicate team names are not allowed.
        @return a list containing the Person pbjects.
        """
        project_members = []
        team_names = []  #  list of names used for detection of duplicates
        i = 0
        while i < team_size:
            team_name = self.get_person_name(i)
            if team_name not in team_names:
                team_names.append(team_name)
                project_members.append(Person(team_name))
                i = i + 1
            else:
                print(("\n\t\tSorry, you already have a team member called {}."
                      " Please try again.").format(team_name))
        return project_members

    def get_person_name(self, i):
        """Prompts the user for a person's name and validates it.
        @return a string containing the person's name.

        Invariants: a person's name must be between the minimum and maximum length
        and cannot be blank. The name must contain at least one alphabetic character
        and may contain numbers.
        """
        person_name = input(("\n\tEnter the name of team member {}: ")
                            .format(i+1))

        while not self.is_valid_person_name(person_name):
            print(("\n\t\tThe name must be between {} and {} characters long "
                   "and may contain only alphabetical characters.")
                   .format(self.MINIMUM_NAME_LENGTH, self.MAXIMUM_NAME_LENGTH))
            person_name = input(("\n\tEnter the name of team member {}: ")
                                .format(i+1))
        return person_name

    def vote_menu(self):
        """Makes user pick an existing project and cast votes in it.

        @return back to the main menu
        """
        project = self.pick_project()
        if project:
            self.cast_vote(project)

    def cast_vote(self, project):
        """Allows all team members to vote on other members.

        @return back to vote_menu, and thus the main menu.

        Invariants: vote must be an integer between the 0 and 100,
        all votes by one member must add up to 100.
        """
        proj_members = project.members
        print('\tThere are {} members.\n'.format(len(proj_members)))
        for member in proj_members:
            print("\nEnter " + member.name + "'s votes, points must add up to 100.")
            self.member_votes(member, proj_members)

    def member_votes(self, voter, proj_members):
        """ Does it make sense to separate this from cast_vote? """
        summa = 0
        while summa != 100:
            print()
            for member in proj_members:
                if member != voter:
                    vote_value = self.get_vote_value(voter.name, member.name)
                    voter.vote_for(member.name, vote_value)
                    summa += int(vote_value)
            if summa != 100:
                print('\tPoints must add up to 100. Please try again.')
                summa = 0

    def get_vote_value(self, voter, votee):
        """Takes input for the vote, checks if it is valid.

        :returns: an integer.
        """
        vote_value = input('\tEnter ' + voter + "'s vote for " + votee + ': ')
        while self.is_valid_vote(vote_value) == False:
            print(("\n\tYour vote must be an integer between {} and {}. "
                   "Try again.").format(self.MIN_VOTE, self.MAX_VOTE))
            vote_value = input("\tEnter " + voter + "'s vote for " + votee + ': ')
        return int(vote_value)

    def is_valid_vote(self, vote, minimum=MIN_VOTE, maximum=MAX_VOTE):
        """ Checks if the vote is an integer and falls betwen the minimum and maximum.
        Minimum is 0 and maximum is 100 by default.

        @return boolean value
        """
        try:
            return minimum <= int(vote) <= maximum
        except ValueError:
            return False

    def show_projects(self):
        """ Show_projects will be implemented in final deliverable. Show_projects
        displays a message notifying user that this feature is not yet
        available.
        """
        show_projects_string = "\nShow Projects feature is not yet implemented."
        print(show_projects_string)

    def main(self):
        """The menu is displayed until the user quits"""
        menu = Menu()

        while True:
            choice = menu.select()
            if choice == Menu.Choices.ABOUT:
                self.about()
            elif choice == Menu.Choices.CREATE_PROJECT:
                project = self.create_project()
                self.projects[project.name] = project
            elif choice == Menu.Choices.ENTER_VOTES:
                self.vote_menu()
            elif choice == Menu.Choices.SHOW_PROJECTS:
                self.show_projects()
            elif choice == Menu.Choices.QUIT:
                break
            else:
                assert False

        print("\n\nThe program has ended.")
