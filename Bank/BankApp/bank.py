from BankApp.account import Account


class Bank:
    def __init__(self):
        self.number_of_accounts = 0
        self.accounts = []

    def get_number_of_accounts(self):
        return self.number_of_accounts

    def create_account(self, first_name, last_name, pin, account_number):
        new_account = Account(first_name, last_name, pin)
        self.accounts.append(new_account)
        self.number_of_accounts += 1

    def get_first_name(account):
        return account.first_name

    def get_last_name(account):
        return account.last_name

    # def get_pin(self, account):
    #     return account.get_pin()

