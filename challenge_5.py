
class account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def withdrawl(self, amount):
        self.balance -= amount   
        
    def deposit(self, amount):
         self.balance += amount     
    
    def get_balance(self):
        return self.balance

class savings_acccount(account):
    def __init__(self,title, balance, intrest_rate):
        super().__init__(title, balance)
        self.intrest_rate = intrest_rate
    
    def intrest_amount(self):
        intrestamount = (self.intrest_rate * self.balance)/100
        return intrestamount
        

account_obj = account("ashish", 2000)
print(account_obj.balance)
print(account_obj.get_balance())
savings_object = savings_acccount("ashish", 2000, 5)
print(savings_object.intrest_amount())