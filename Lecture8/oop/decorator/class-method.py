"""
Class Method
 - A class method is bound to the class and receives the class as an implicit first argument. 
 Note - Static method can access or modify class state and generally for utility. 
eg: 
class Student:
@classmethod #decorator
def college (cls):
pass
 
 """

class Person:
    name = "anonymous"

    # def changeName(self, name):
        # note: self is an object.
        # self.name = name #this is creating new instance of the name. 
        #to change class attribute we can change it to. 
        # Person.name = name
        # or 
        # self.__class__.name = name
        # but to directly access the class method in fn. In the eg syntax above

    @classmethod
    def changeName(cls, name): #this cls is not self or obj, this is referring to the class.
        cls.name = name
p1 = Person()
p1.changeName("Anita")
print(Person.name)
print(p1.name)