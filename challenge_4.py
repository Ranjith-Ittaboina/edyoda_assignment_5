class account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class savings_acccount(account):
    def __init__(self,title, balance, intrest_rate):
        super().__init__(title, balance)
        self.intrest_rate = intrest_rate

account_obj = account("ashish", 5000)
savings_acccount_obj = savings_acccount("ashish", 5000, 5)
print(savings_acccount_obj.title)
print(savings_acccount_obj.balance)
print(savings_acccount_obj.intrest_rate)

