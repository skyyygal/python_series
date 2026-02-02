"Encapsulation"
"Wrapping data and functions into a single unit(object)"

"Private attributes and methods. "
"""conceptual implementation in python
Private attributes and methods are meant to be used only within the class 
and are not accessible from outside class.

Public - can be accessed outside class. 
Private - cannot be accessed outside the class. but can be accessed through method. 
 We use __ -> double dash to make a variable or method private"""

class Account:
    def __init__(self, acc_no, account_pass):
        self.acc_no = acc_no
        self.__account_pass = account_pass

    def reset_pass(self):
        print(self.__account_pass)
   


    
acc= Account(1234, 8979)
print(acc.acc_no)
# print(acc.__account_pass) # Now account pass will throw an error. 
acc.reset_pass() #this will print the account pass. 





