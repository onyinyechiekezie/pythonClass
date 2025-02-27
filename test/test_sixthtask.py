import unittest
from ClassTasks.sixthtask import get_number_of_occurrences


class TestSixthTask(unittest.TestCase):

    def test_get_number_occurrence(self):
        self.assertEqual(get_number_of_occurrences("semicolon", "o"),("o", 2))

    def test_function_works_correctly(self):
        self.assertEqual(get_number_of_occurrences("package", "a"),("a", 2))

    def test_function_works_correctly_2(self):
        self.assertEqual(get_number_of_occurrences("hell", "e"),("e", 1))