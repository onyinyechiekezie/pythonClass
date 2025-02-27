import unittest
from ClassTasks.fourthtask import get_mix_upper


class TestFifthTask(unittest.TestCase):

    def test_that_fuction_works_correctly(self):
        string = "sEmIColOn"
        actual = get_mix_upper(string)
        result = "EICOsmoln"
        self.assertEqual(actual, result)

    def test_that_function_picks_upper_and_lower_case(self):
        string = "OnYiI"
        actual = get_mix_upper(string)
        result = "OYIni"
        self.assertEqual(actual, result)

    def test_that_function_picks_lower_case(self):
        string = "onyii"
        actual = get_mix_upper(string)
        result = "onyii"
        self.assertEqual(actual, result)