import unittest

from ClassTasks.secondtask import swap_last_characters

class TestSecondTask(unittest.TestCase):

    def test_that_characters_are_swapped(self):
        self.assertEqual(swap_last_characters("abc","xyz"), ("xyc","abz"))

    def test_that_function_returns_correct_value(self):
        self.assertEqual(swap_last_characters("heart", "there"), ("thart", "heere"))

    def test_function_again(self):
        self.assertEqual(swap_last_characters("onesy", "twosy"), ("twesy", "onosy"))