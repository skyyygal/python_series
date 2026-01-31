"del Keyword"
# Used to delete object properties or object itself. 
# del s1.name
# del s1


class Student:
    def __init__(self):
        self.name = "Anita"
        self.age = 25

s1 = Student()
print(s1.name)
print(s1.age)
del s1.age
# print(s1.age)
del s1

print(s1)