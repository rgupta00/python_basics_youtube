class Account:
    bank_name='sbi'
    no_of_customers=0

    @classmethod
    def print_bank_details(cls):
        return f'the bank details bank name : {Account.bank_name} and no of customer in our bank is {Account.no_of_customers}'

    def __init__(self, name, bal):
        self.name = name
        self.balance = bal
        Account.no_of_customers=Account.no_of_customers+1

    def deposit(self, amt):
        self.balance=self.balance+amt
        return  self.balance

    def withdraw(self, amt):
        self.balance = self.balance - amt
        return self.balance

    def __str__(self):
        return f'name of account holder is {self.name} and {self.balance}'


ob = Account('raj', 8000)
print(ob)
ob.deposit(1000)
print(ob)
ob.withdraw(2000)
print(ob)

ob2 = Account('ekta', 8000)

print(Account.print_bank_details())
print(Account.bank_name)

print(Account.no_of_customers)