import unittest


from arraylist import myarray

class MyTestCase(unittest.TestCase):

    def test_that_isempty(self):
        arraylist = myarray([])
        self.assertTrue(arraylist.is_empty())





if __name__ == '__main__':
    unittest.main()
