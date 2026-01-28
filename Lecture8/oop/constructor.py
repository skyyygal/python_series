# __init__ Function 
"constructor"

# All classes have a function call __init__(),which is always executed when the object is being initiated

# creating class 
class Student:
    def __init__(self, fullname):
        self.name = fullname

# creating object

s1 = Student("Anita")
print(s1.name)

'''The self parameter is a reference to the current 
instance of the class and is used to access variable that 
belong to the class.'''