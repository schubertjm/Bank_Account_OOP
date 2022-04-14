class BankAccount:
    bank_name = "First National Schubert Bank"
    all_accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    @classmethod
    def all_bank_account_info(cls):
        total_balance = 0
        avg_int_rate = 0
        for account in cls.all_accounts:
            total_balance += account.balance
            avg_int_rate += account.int_rate
        return round(total_balance,2), round(avg_int_rate / len(cls.all_accounts),2)
    @staticmethod
    def int_rate_correct_format(rate):
        if type(rate) == float:
            return True
        else:
            return False
    @staticmethod
    def account_postive(balance):
        if balance <= 0:
            return False
        else:
            return True
    @staticmethod
    def can_withdrawal(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdrawal(self.balance, amount):
            self.balance -= amount
        else:
            print(f"Insuffient funds to withdrawal {amount}")
        return self
    def display_account_info(self):
        print(f"Bank Account has {self.balance} at {self.int_rate} interest rate")
        return self
    def yield_interest(self):
        if BankAccount.account_postive(self.balance):
            if BankAccount.int_rate_correct_format(self.int_rate):
                self.balance += round(self.balance * self.int_rate,2)
            else:
                print("Interest Rate is in incorrect format")
        else:
            print(f"Insuffient funds - {self.balance}")
        return self

CA_123456 = BankAccount(.03,100)
CA_987654 = BankAccount(.01, 450.35)

CA_123456.deposit(50).deposit(100).deposit(150).withdraw(20).display_account_info().yield_interest().display_account_info()
CA_987654.deposit(20).deposit(20).withdraw(5).withdraw(5).withdraw(5).withdraw(5).display_account_info().yield_interest().display_account_info()
print(BankAccount.all_bank_account_info())