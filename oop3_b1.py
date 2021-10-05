class Customer():
    def __init__(self,name,date_of_birth,email,phone):
        self.name=name
        self.date_of_birth=date_of_birth
        self.email=email
        self.phone=phone
    def get_info(self):
        print(f"Name: {self.name}, Date_of_birth: {self.date_of_birth}, Email: {self.email}, Phone: {self.phone}")    

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def owner(self):
        return self._owner

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
        print(f"Số tài khoản: {self.account_number}, Họ và Tên: {self.owner.name},Ngày tháng năm sinh: {self.owner.date_of_birth},Số điện thoại: {self.owner.phone},Email: {self.owner.email},{self.balance}")

class SavingAccount(BankAccount):
    monthly_interest_rate=0.005
    def calculate_interest(self):
        print ("SỐ tiền tiết kiệm: ",self.balance*SavingAccount.monthly_interest_rate)
        
cus= Customer('Phương NT','1-1-20000','phuongnt@gmail.com','0456543452')
sav=SavingAccount('17897',cus,5000000)
sav.display()
sav.calculate_interest()