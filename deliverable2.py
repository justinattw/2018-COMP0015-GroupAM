#! python3
# name: deliverable2.py
#
#
# course: COMP0015
# date: 02/12/18
# names: Antonin Kanat & Justin Wong
# description: the second deliverable of the Fair Grade Allocator, containing
# a main menu, create project and enter votes feature
#
# Based on code from Rae Harbird
#

from person import Person
from project import Project

def main():

    MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']

    def print_menu():
        """ Prints the menu for the application """
        menu_string = ("\nWelcome to Spliddit:\n\n"
                      "\tAbout\t\t(A)\n"
                      "\tCreate Project\t(C)\n"
                      "\tEnter Votes\t(V)\n"
                      "\tShow Project\t(S) \n"
                      "\tQuit\t\t(Q)")
        print(menu_string)

    def is_valid_option(option):
        if len(option.strip()) == 0:
            return False
        elif option[0].upper() in MENU_CHOICES:
            return True
        else:
            return False

    def get_option():
        option = '*'

        while not is_valid_option(option):
            print_menu()
            option = input("\nEnter an option: ")

        return option.upper()

    option = '*'
    while option != 'Q':
        option = get_option()
        if option == 'A':
            about()
        elif option == 'C':
            create_project()
        elif option == 'V':
            enter_votes()
        elif option == 'S':
            show_projects()
    print("\n\nThis program has ended, good-bye.")

def about() :
    about_string = ("\n\nWelcome to Spliddit. "
                   "This application will allocate grades to project "
                   "participants \nbased off the votes of their "
                   "peers.\n"
                   "Based on code by Rae Harbird."
                   "\n\n2018 UCL Antonin Kanat & Justin Wong")
    print(about_string)

""" Initialising dictionary which stores information on all projects. This
    is added to through create_project(), and manipulated through enter_votes()
"""
projects_dict = {}

def create_project():
    """ Creates a project from the information entered by the user.

    First defines functions required for create_project() in chronological
    order (for convenient readability), then it runs the defined functions.

    @returns a dictionary containing the project name, team size, names
        of team members and their votes (which are initialised to {})
    """
    def get_project_name():
        """Prompts the user for a project name and validates it.
        Invariants: a project name must be between the minimum and
                    maximum length and cannot be blank. We allow the name to
                    contain any character type,
        @returns a string containing the project name.
        """
        project_name = input("\n\tEnter project name: ")
        while Project.is_valid_project_name(project_name) is not True:
            print(("\n\t\tThe project name must be between {} and {} "
                   "characters . Please try again.")
                   .format(Project.MIN_NAME_LENGTH, Project.MAX_NAME_LENGTH))
            project_name = input("\n\tEnter project name: ")
        return project_name

    def get_team_size():
        """ Prompts the user for the team size and validates it.
        Invariants: the team size must be between the minimum and maximum size.

        @returns the number of people in the team.
        """
        team_size = input("\n\tEnter the number of team members: ")
        while Project.is_valid_team_size(team_size) is not True:
            print(("\n\t\tThe team size must be an integer between {} and {}. "
                   "Please try again.")
                   .format(Project.MIN_TEAM_SIZE, Project.MAX_TEAM_SIZE))
            team_size = input("\n\tEnter the number of team members: ")

        return int(team_size)

    def get_member_names(team_size):
        """Gets the names for the people in the team and creates according
        Person objects. Duplicate team names are not allowed.
        @return a list containing the Person pbjects.
        """
        project_members = []
        team_names = []  #  list of names used for detection of duplicates
        i = 0
        while i < team_size:
            team_name = get_person_name(i)
            if team_name not in team_names:
                team_names.append(team_name)
                person = Person(team_name)
                project_members.append(person)
                i += 1
            else:
                print(("\n\t\tSorry, you already have a team member called {}."
                      " Please try again.").format(team_name))

        return project_members

    def get_person_name(i):
        """Prompts the user for a person's name and validates it.
        @return a string containing the person's name.

        Invariants: a person's name must be between the minimum and maximum
        length and cannot be blank. It may only contain alphabetical characters
        """
        person_name = input(("\n\t\tEnter the name of team member {}: ")
                            .format(i+1))

        while not Person.is_valid_person_name(person_name):
            print(("\n\t\tThe name must be between {} and {} characters long "
                   "and may contain only alphabetical characters.")
                   .format(Person.MIN_NAME_LENGTH, Person.MAX_NAME_LENGTH))
            person_name = input(("\n\t\tEnter the name of team member {}: ")
                                .format(i+1))
        return person_name

    project_name = get_project_name()
    team_size = get_team_size()
    project_members = get_member_names(team_size)
    project = Project(project_name, team_size, project_members)
    projects_dict[project.name] = project

def enter_votes():
    """ Enables users to enter votes for members in previously created projects

    First defines all functions required for enter_votes() in chronological
    order (for convenient readability), then it runs the defined functions.
    """

    def pick_project():
        """ Lets the user pick a project from the projects dictionary to
            access and enter votes on.

        @returns a Project object
        """
        if not projects_dict:
            print('\n\tPlease create a project first.')
            return None

        pick_project = ""
        existing_projects = [i for i in projects_dict]

        while pick_project not in existing_projects:
            """ Displays projects that have already been created to give user
                a list of options to choose from.
            """
            print("\n\tPlease choose from the following projects: ", end="")
            print(*existing_projects, sep=', ')
            pick_project = input("\n\tEnter the project name (case sensitive): ")
        return projects_dict[pick_project]

    def cast_vote(project):
        """ Goes through each member in a Project and prompts
            votes. It is used in conjunction with member_votes() and
            get_vote_value()
        """
        proj_members = project.members
        print('\n\tThere are {} members.'.format(len(proj_members)))
        for member in proj_members:
            print("\nEnter " + member.name + "'s votes, points must add up to"
                   " 100.")
            member_votes(member, proj_members)

    def member_votes(voter, proj_members):
        """ Counts and sums the total vote score given by a voter. It ensures
            that the given scores do not exceed the maximum total allowed.

        Invariants: summa counts the total number of points given. It
                    initialises and re-initialises to 0.
        """
        summa = 0
        while summa != int(Person.MAX_VOTE):
            print()
            for member in proj_members:
                if member != voter:
                    vote_value = get_vote_value(voter.name, member.name)
                    voter.vote_for(member.name, vote_value)
                    summa += int(vote_value)
            if summa != int(Person.MAX_VOTE):
                print(('\tPoints must add up to {}. Please try again.')
                        .format(Person.MAX_VOTE))
                summa = 0

    def get_vote_value(voter, votee):
        """ Gets vote scores from voters, assigning them to each member.

        @returns the votes given from a member assigned to another member.
        """
        vote_value = input('\tEnter ' + voter + "'s vote for " + votee + ': ')
        while not Person.is_valid_vote(vote_value):
            print(("\n\tYour vote must be an integer between {} and {}. "
                   "Try again.").format(Person.MIN_VOTE, Person.MAX_VOTE))
            vote_value = input(("\tEnter " + voter + "'s vote for " + votee
                                + ': '))
        return int(vote_value)

    project = pick_project()
    if project:
        cast_vote(project)


def show_projects():
    """ Show_projects will be fully  implemented in final deliverable.
    Show_projects displays a message notifying user that this feature is not
    yet available.
    """
    show_projects_string = ("\nShow Projects feature is not yet implemented "
                            "as of Deliverable 2.\n\n")
    print(show_projects_string)

    """
    The following body of code is a provisional attempt at displaying
    projects. It displays projects in a dictionary form. As deliverable 2 does
    not require a Show Projects feature, we have excluded it from the program.
    """
    # show_projects_string = ("For now, show_projects will print a "
    #                         "dictionary containing created projects and "
    #                         "corresponding votes.\n\n")
    # print(show_projects_string + str(projects_dict))

# Start the program
if __name__ == "__main__":
    main()
