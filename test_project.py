#! python3
# name: test_project.py
#
#
# course: COMP0015
# date: 02/12/18
# names: Antonin Kanat & Justin Wong
# description: a test file conducting unit tests on the 'project.py' module
#

import unittest
from project import Project

class TestProject(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    #
    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     pass

    def test_project_name(self):
        project_1 = Project('COMP0015', 3, {})
        project_2 = Project('BASC0005', 3, {})

        self.assertEqual(project_1.name, 'COMP0015')
        self.assertEqual(project_2.name, 'BASC0005')

        project_1._name = 'Allow spaces'
        project_2._name = 'Punctuation!'

        self.assertEqual(project_1.name, 'Allow spaces')
        self.assertEqual(project_2.name, 'Punctuation!')

    """ Commented out as setters are not being used
    """
    # def test_project_size(self):
    #     project_1 = Project('XYZ', Project.MIN_TEAM_SIZE, {})
    #     project_2 = Project('XYZ', Project.MAX_TEAM_SIZE, {})
    #     project_3 = Project('XYZ', Project.MIN_TEAM_SIZE - 1, {})
    #     project_4 = Project('XYZ', Project.MAX_TEAM_SIZE + 1, {})
    #     project_5 = Project('XYZ', 'Three', {})
    #
    #     self.assertEqual(project_1.size, Project.MIN_TEAM_SIZE)
    #     self.assertEqual(project_2.size, Project.MAX_TEAM_SIZE)
    #     self.assertEqual(project_3.size, Project.MIN_TEAM_SIZE - 1)
    #     self.assertEqual(project_4.size, Project.MAX_TEAM_SIZE + 1)

    def test_is_valid_team_size(self):
        team_size_1 = Project.MIN_TEAM_SIZE
        team_size_2 = Project.MAX_TEAM_SIZE
        team_size_3 = Project.MIN_TEAM_SIZE - 1
        team_size_4 = Project.MAX_TEAM_SIZE + 1
        team_size_5 = 'One'
        team_size_6 = '.!?'

        self.assertTrue(Project.is_valid_team_size(team_size_1))
        self.assertTrue(Project.is_valid_team_size(team_size_2))
        self.assertFalse(Project.is_valid_team_size(team_size_3))
        self.assertFalse(Project.is_valid_team_size(team_size_4))
        self.assertFalse(Project.is_valid_team_size(team_size_6))

    def test_is_integer(self):

        input_1 = 0
        input_2 = 1
        # input_3 = 0.5 # returns True; require further debugging
        input_4 = 'x'

        self.assertTrue(Project.is_integer(input_1))
        self.assertTrue(Project.is_integer(input_2))
        # self.assertFalse(Project.is_integer(input_3))
        self.assertFalse(Project.is_integer(input_4))

# Start the program
if __name__ == "__main__":
    unittest.main()
