import unittest
from ClassTasks.fifthtask import remove_special_characters


class TestFifthTask(unittest.TestCase):

    def test_that_fuction_works_correctly(self):
        string = "he,ll.o"
        actual = remove_special_characters(string)
        result = "hello"
        self.assertEqual(actual, result)

    def test_function_with_numbers(self):
        string = "ony%ii2@3"
        actual = remove_special_characters(string)
        result = "onyii23"
        self.assertEqual(actual, result)


    def test_function_works_with_alphabet(self):
        string = "onyii"
        actual = remove_special_characters(string)
        result = "onyii"
        self.assertEqual(actual, result)
