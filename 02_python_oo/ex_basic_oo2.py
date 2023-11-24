class Account:
    __bank_name='sbi'
    __no_of_customers=0
    @classmethod
    def print_bank_details(cls):
        return f'the bank details bank name : {Account.__bank_name} and no of customer in our bank is {Account.__no_of_customers}'

    def __init__(self, name, bal):
        self.__name = name
        self.__balance = bal
        Account.__no_of_customers=Account.__no_of_customers+1

    def deposit(self, amt):
        self.__balance=self.__balance+amt
        return  self.__balance

    def withdraw(self, amt):
        self.__balance = self.__balance - amt
        return self.__balance

    def __str__(self):
        return f'name of account holder is {self.__name} and {self.__balance}'


ob = Account('raj', 8000)
# print(ob.__balance)
print(ob)
ob.deposit(1000)
print(ob)
ob.withdraw(2000)
print(ob)

ob2 = Account('ekta', 8000)

print(Account.print_bank_details())