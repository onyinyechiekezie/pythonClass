import unittest
from data_structure.mystack import MyStack

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.my_stack = MyStack()

    def test_that_is_empty(self):
        self.assertTrue(self.my_stack.is_empty())

    def test_that_push_element(self):
        item = 1
        self.my_stack.push(item)
        self.assertEqual(self.my_stack.stackList, [item])

    def test_that_push_multiple_elements(self):
        items = [1,2,3,4]
        for item in items:
            self.my_stack.push(item)
        self.assertEqual(self.my_stack.stackList, items)

    def test_that_pop_element(self):
        item = 1
        self.my_stack.push(item)
        self.assertEqual(self.my_stack.pop(), item)

    def test_that_pop_multiple_elements(self):
        items = [1,2,3,4]
        for item in items:
            self.my_stack.push(item)
            self.assertEqual(self.my_stack.pop(),item)