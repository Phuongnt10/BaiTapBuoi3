class BankAccount:
    def __init__(self,account_number, account_name, balance=0):
        self._balance=balance
        self._account_number=account_number
        self._account_name=account_name

    @property  
    def get_account_number(self):
        return self._account_number
    
    @property      
    def  get_account_name(self):
        return self._account_name
    @property    
    def balance(self):
        return self._balance   

    @balance.setter
    def balance(self,balance):
        if balance >=0:
            self._balance=balance
        else:
             print("Số dư không hợp lệ")   
    def display(self):
       ##print("Thông tin tài khoản là:",f"{self.get_account_number()}  {self.get_account_name()}  {self.balance()}")
        print(self.get_account_number, self.get_account_name, self.balance)

    def  withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance-=amount
        else:
            print("Số dư không không đủ") 

    def deposit(self, amount):
        if amount >0:
            self.balance+=amount
        else:
            print("Số dư không hợp lệ") 

bank=BankAccount('19001919','Nguyen Thi Phuong',10000000)
bank.withdraw(500)
bank.deposit(3000000)
bank.display()
