# Create student class that takes name and marks of 3 subjects as argument in constructor. 
# Then create method to print the average.


class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
# this fn doesnt need self. 
# it will only work if we make it static or use self. 
#  or throws type error: TypeError: Student.college() takes 0 positional arguments but 1 was given
    @staticmethod
    def college():
        print("ABC College")

    
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("Hi", self.name, "Your avg score is:", sum/3)
       
    
s1 = Student("Anita", [99, 98, 99])
s1.get_average()

s1.name ="Anita Pandey"
s1.get_average()
s1.college()
