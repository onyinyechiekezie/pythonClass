import unittest

from ClassTasks.thirdtask import get_string_and_ce
class TestSecondTask(unittest.TestCase):

    def test_get_string_and_ce(self):
        self.assertEqual(get_string_and_ce("helloo"), "helceloo")

    def test_get_string_and_ce_well(self):
        self.assertEqual(get_string_and_ce("joy"), "joyce")

    def test_get_string_and_ce_best(self):
        self.assertEqual(get_string_and_ce("cape"), "cacepe")


