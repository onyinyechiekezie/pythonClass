class Account:
    def __init__(self, first_name, last_name, pin):
        self.balance = 0
        self.account_number = "2302646517"
        self.pin = pin
        self.first_name = first_name
        self.last_name = last_name

    # def get_pin(self):
    #     return self.pin

    def get_first_name(self):
        return self.first_name


    def get_last_name(self):
        return self.last_name

    def set_pin(self, pin):
        self.pin = pin

    def is_exist(self):
        return True


    def get_balance(self, pin):
        self.validate_pin(pin)
        return self.balance


    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount


    def withdraw(self, amount, pin):
        self.validate_pin(pin)
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.balance < amount:
            raise ValueError("Insufficient Balance")
        self.balance -= amount


    def update(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return True
        return False


    def validate_pin(self, pin):
        if self.pin != pin:
            raise ValueError("Invalid PIN")
        return "PIN is correct"


    def get_account_name(self):
        return f"{self.first_name} {self.last_name}"


    def get_account_number(self):
        return self.account_number
