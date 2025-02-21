import unittest
from MyTv.my_tv import Television

class MyTestCase(unittest.TestCase):
    def setUp(self):
         self.tv = Television()

    # def test_default_state_of_tv_is_off(self):
    #     self.tv.is_on()
    #     self.assertTrue(self.tv.is_on())

    def test_turn_on(self):
        self.tv.turn_off()
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)


    def test_turn_off(self):
        self.tv.turn_on()
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on)


    def test_increase_volume_level(self):
        self.tv.turn_on()
        self.tv.volume_level = 1
        self.assertEqual(self.tv.volume_level, 1)
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.assertEqual(self.tv.volume_level, 3)












