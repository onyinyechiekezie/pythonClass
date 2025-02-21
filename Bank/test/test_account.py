import unittest
from BankApp.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Autumn", "Jordan", "2121")

    def test_account_exist(self):
        self.assertTrue(self.account.is_exist())

    def test_account_balance(self):
        self.assertEqual(0, self.account.get_balance("2121"))

    def test_account_deposit(self):
        self.account.deposit(5000)
        self.assertEqual(5000, self.account.get_balance("2121"))

    def test_that_negative_amount_cannot_be_deposited(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-3000)
        self.assertEqual("Amount cannot be negative", str(context.exception))

    def test_account_withdraw_deposit_10k_withdraw_5k_balance_5k(self):
        self.account.deposit(10000)
        self.assertEqual(10000, self.account.get_balance("2121"))
        self.account.withdraw(5000, "2121")
        self.assertEqual(5000, self.account.get_balance("2121"))

    def test_for_pin_update(self):
        updated = self.account.update("2121", "1212")
        self.assertTrue(updated)

    def test_account_name_for_first_name_and_last_name(self):
        self.assertEqual("Autumn Jordan", self.account.get_account_name())

    def test_account_number(self):
        self.assertEqual("2302646517", self.account.get_account_number())

if __name__ == "__main__":
    unittest.main()
