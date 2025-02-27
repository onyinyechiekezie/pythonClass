import unittest

from ClassTasks.firsttask import get_occurrence


class TestFirstTask(unittest.TestCase):
    def test_get_occurrence_characters(self):
        self.assertEqual(get_occurrence("Bank"),{"B":1, "a":1, "n":1, "k":1 })


    def test_get_occurrence(self):
        self.assertEqual(get_occurrence("semicolon.africa"), {"s":1, "e":1, "m":1, "i":2, "c":2, "o":2, "l":1, "n":1, ".":1, "a":2, "f":1, "r":1})


    def test_get_occurrence2(self):
        self.assertEqual(get_occurrence("happy12"), {"h":1, "a":1, "p":2, "y":1, "1":1, "2":1})