class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(f"{self.account_number}, {self.account_name},{self.balance}")

class SavingAccount(BankAccount):
    monthly_interest_rate=0.005
    def calculate_interest(self):
        print (self.balance*SavingAccount.monthly_interest_rate)

sav=SavingAccount('1','phuongnt',5000000)
sav.display()
sav.calculate_interest()