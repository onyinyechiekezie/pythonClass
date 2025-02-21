import unittest
# from data_structure import myarray
from data_structure.myarray import MyArray

class TestMyArray(unittest.TestCase):

    # def setUp(self):
    #     MyArray(4)



    def test_that_my_array_is_empty(self):
        myarray = MyArray([])
        self.assertTrue(myarray.isEmpty())

    def test_that_my_array_is_full(self):
        myarray = MyArray(5)
        self.assertTrue(myarray.isFull())

    def test_that_element_can_be_added_to_array(self):
        myarray = MyArray(3)
        myarray.add(1)
        myarray.add(2)
        myarray.add(3)
        self.assertEqual(myarray.size, 3)


    def test_that_elements_can_be_removed_from_array(self):
        myarray = MyArray(3)
        myarray.add(1)
        myarray.add(2)
        myarray.add(3)
        self.assertEqual(myarray.size, 3)
        myarray.remove(2)
        self.assertEqual(myarray.size, 2)

    def test_my_array_contains_an_element(self):
        myarray = MyArray(3)
        myarray.add(1)
        myarray.add(2)
        myarray.add(3)
        self.assertTrue(myarray.contains(3))

    def test_my_array_pops(self):
        myarray = MyArray(3)
        myarray.add(1)
        myarray.add(2)
        myarray.add(3)
        self.assertEqual(myarray.pop(2), 3)

    def test_elements_can_be_inserted_into_array(self):
        myarray = MyArray(3)
        myarray.add(1)
        myarray.add(2)
        self.assertEqual(myarray.insert(2,3),3)


    # def test_that_elements_in_array_cannot_exceed_5(self):
    #     myarray = MyArray(5)
    #     myarray.add(1)
    #     myarray.add(2)
    #     myarray.add(3)
    #     myarray.add(4)
    #     myarray.add(5)
    #     self.assertRaises(ValueError, myarray.add(6))




