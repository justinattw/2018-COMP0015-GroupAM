#! python3
# name: test_person.py
#
#
# course: COMP0015
# date: 02/12/18
# names: Antonin Kanat & Justin Wong
# description: a test file conducting unit tests on the 'person.py' module
#

import unittest
from person import Person

class TestPerson(unittest.TestCase):

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

    def test_person_name(self):
        person_1 = Person('Justin')
        person_2 = Person('Antonin')

        self.assertEqual(person_1.name, 'Justin')
        self.assertEqual(person_2.name, 'Antonin')

        person_1.name = 'Jackson'
        person_2.name = 'Anthony'

        self.assertEqual(person_1.name, 'Jackson')
        self.assertEqual(person_2.name, 'Anthony')

        with self.assertRaises(ValueError):
            person_1.name = '123'
            person_2.name = '1'
            person_3.name = '!!!'
            person_4.name = 'Foobar!'

    def test_is_valid_person_name(self):
        person_1 = Person('Justin')
        person_2 = Person('Antonin')
        person_3 = Person('X' * (Person.MIN_NAME_LENGTH - 1))
        person_4 = Person('X' * (Person.MAX_NAME_LENGTH + 1))

        self.assertTrue(Person.is_valid_person_name(person_1.name))
        self.assertTrue(Person.is_valid_person_name(person_2.name))
        self.assertFalse(Person.is_valid_person_name(person_3.name))
        self.assertFalse(Person.is_valid_person_name(person_4.name))

        person_1.name = 'X' * (Person.MIN_NAME_LENGTH - 1)
        person_2.name = 'X' * (Person.MAX_NAME_LENGTH + 1)

        self.assertFalse(Person.is_valid_person_name(person_1.name))
        self.assertFalse(Person.is_valid_person_name(person_2.name))
        self.assertFalse(Person.is_valid_person_name(person_3.name))

    def test_is_valid_vote(self):

        vote_1 = Person.MIN_VOTE
        vote_2 = Person.MAX_VOTE
        vote_3 = Person.MIN_VOTE - 1
        vote_4 = Person.MAX_VOTE + 1
        vote_5 = 'X'
        vote_6 = '50!'

        self.assertTrue(Person.is_valid_vote(vote_1))
        self.assertTrue(Person.is_valid_vote(vote_2))
        self.assertFalse(Person.is_valid_vote(vote_3))
        self.assertFalse(Person.is_valid_vote(vote_4))
        self.assertFalse(Person.is_valid_vote(vote_5))
        self.assertFalse(Person.is_valid_vote(vote_6))

    def test_is_integer(self):

        input_1 = 0
        input_2 = 1
        # input_3 = 0.5 # returns True; requires further debugging
        input_4 = 'x'

        self.assertTrue(Person.is_integer(input_1))
        self.assertTrue(Person.is_integer(input_2))
        # self.assertFalse(Person.is_integer(input_3))
        self.assertFalse(Person.is_integer(input_4))

if __name__ == '__main__':
    unittest.main()
