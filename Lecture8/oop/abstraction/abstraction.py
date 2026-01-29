" Abstraction - "
"Hiding the implementation details of a class and only showing the essential feature to the user. "

# problem: Create Account class with 2 attributes: balance and account no.
# Create method for debit, credit and printing the balance.

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit_amount(self, amount):
        self.balance-=amount
        print("Rs.", amount, "was debited.")
        print("Total bal:",self.get_bal())

    def credit_amount(self, amount):
     self.balance+=amount
     print("Rs.", amount, "was credited.")
     print("Total bal:",self.get_bal())


    def get_bal(self):
       
       return self.balance

    
acc= Account(10000, 123)
print(acc.balance)
print(acc.account_no)
acc.debit_amount(1000)
acc.credit_amount(500)

