"""
Property - 
We use @property decorator on any method in the class to use the method as a property.

"""

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage =  str((self.phy + self.chem +self.math)/3) +"%"


    # def calcPercentage(self):
        # self.percentage =  str((self.phy + self.chem +self.math)/3) +"%"
    


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) +"%"
    # 
s1 = Student(98, 97, 99)
print(s1.percentage)
s1.phy =86
print(s1.percentage)
