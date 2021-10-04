class Customer():
    def __init__(self,name,date_of_birth,email,phone):
        self.name=name
        self.date_of_birth=date_of_birth
        self.email=email
        self.phone=phone
    def get_info(self):
        print(f"Name: {self.name}, Date_of_birth: {self.date_of_birth}, Email: {self.email}, Phone: {self.phone}")    
        
cus= Customer('Phương NT','1-1-20000','phuongnt@gmail.com','0456543452')
cus.get_info()