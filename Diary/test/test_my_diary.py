import unittest
from DiaryApp.my_diary import MyDiary
from DiaryApp.entry import Entry


class TestMyDiary(unittest.TestCase):
    def setUp(self):
        self.my_diary = MyDiary("user", "password")

    def test_that_my_diary_exists(self):
        self.assertTrue(self.my_diary.is_exist())

    def test_that_my_diary_is_empty(self):
        self.assertTrue(self.my_diary.is_empty())

    def test_that_incorrect_password_does_not_unlock_diary(self):
        incorrect_password = "wrongpassword"
        with self.assertRaises(ValueError):
            self.my_diary.unlock_diary(incorrect_password)

    def test_that_correct_password_unlocks_diary(self):
        correct_password = "password"
        self.my_diary.unlock_diary(correct_password)
        self.assertFalse(self.my_diary.is_diary_locked)

    def test_that_diary_is_locked(self):
        self.my_diary.lock_diary()
        self.assertTrue(self.my_diary.is_diary_locked)

    def test_create_entry_method_when_diary_is_locked(self):
        self.my_diary.lock_diary()
        self.assertTrue(self.my_diary.is_diary_locked)
        self.my_diary.create_entry("My Entry", "I created a diary")
        self.assertTrue(self.my_diary.is_diary_locked)

    def test_create_entry_method_when_diary_is_unlocked(self):
        self.my_diary.unlock_diary("password")
        self.assertFalse(self.my_diary.is_diary_locked)
        self.my_diary.create_entry("My Entry", "I created a diary")
        self.assertEqual(len(self.my_diary.entries), 1)
        self.assertEqual(self.my_diary.entries[0].title, "My Entry")
        self.assertEqual(self.my_diary.entries[0].body, "I created a diary")

    def test_that_diary_can_create_multiple_entries(self):
        self.my_diary.unlock_diary("password")
        self.assertFalse(self.my_diary.is_diary_locked)
        self.my_diary.create_entry("My First Entry", "I created a diary.")
        self.my_diary.create_entry("My Second Entry", "It's exciting.")
        self.assertEqual(len(self.my_diary.entries), 2)
        self.assertEqual(self.my_diary.entries[0].title, "My First Entry")
        self.assertEqual(self.my_diary.entries[0].body, "I created a diary.")
        self.assertEqual(self.my_diary.entries[1].title, "My Second Entry")
        self.assertEqual(self.my_diary.entries[1].body, "It's exciting.")

    def test_find_entry_by_id(self):
        self.my_diary.unlock_diary("password")
        self.assertFalse(self.my_diary.is_diary_locked)
        self.my_diary.create_entry("My Entry", "I created a diary.")
        self.my_diary.create_entry("My Second Entry", "It's exciting.")
        found_entry = self.my_diary.find_entry_by_id(1)
        self.assertEqual(found_entry.title, "My Entry")

    def test_delete_entry_by_id(self):
        self.my_diary.unlock_diary("password")
        self.assertFalse(self.my_diary.is_diary_locked)
        self.my_diary.create_entry("My Entry", "I created a diary.")
        self.my_diary.create_entry("My Second Entry", "It's exciting.")
        self.assertEqual(len(self.my_diary.entries), 2)
        self.my_diary.delete_entry(1)
        self.assertEqual(len(self.my_diary.entries), 1)

    def test_update_entry(self):
        self.my_diary.unlock_diary("password")
        self.assertFalse(self.my_diary.is_diary_locked)
        self.my_diary.create_entry("My Entry", "I created a diary.")
        self.my_diary.update_entry(1, "My Entry", "I created a diary updated.")
        self.assertEqual(len(self.my_diary.entries), 1)
        self.assertEqual(self.my_diary.entries[0].body, "I created a diary updated.")


if __name__ == '__main__':
    unittest.main()
