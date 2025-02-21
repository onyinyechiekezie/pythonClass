import unittest
from data_structure.myset import MySet


class TestMySet(unittest.TestCase):
    # def setUp(self):
    #     myset = MySet(4)

    def test_that_my_set_isEmpty(self):
        myset = MySet(4)
        self.assertTrue(myset.isEmpty())

    def test_that_my_set_adds_element(self):
        myset = MySet(2)
        myset.add(1)
        myset.add(2)
        self.assertEqual(myset.size, 2)

    def test_that_my_set_contains_an_element(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        myset.add(3)
        # self.assertEqual(myset.size, 3)
        # myset.contains(2)
        self.assertTrue(myset.contains(2))

    def test_that_myset_can_sort(self):
        myset = MySet(3)
        myset.add(3)
        myset.add(2)
        myset.add(1)
        self.assertEqual(myset.sort(), [1, 2, 3])







    # def test_that_element_can_be_removed(self):
    #     myset = MySet(4)
    #     myset.add(1)
    #     myset.add(2)
    #     myset.add(3)
    #     myset.remove(2)
    #     self.assert