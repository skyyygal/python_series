"""
# Introduction

Inheritance 
When one class derives the properties/methods of another class(parent/base)

eg: class Car:
    def start():
    def stop():
    color = "brown"

class ToyatoCar(Car):
"""

'''
Types of inheritance. 

1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance

'''

class Car:
    color = "black"
    @staticmethod
    def start():
        print("START")

    @staticmethod
    def stop():
        print("STOP")

class Toyata(Car):
    def __init__(self, name):
        self.name = name
        
car1 = Toyata("Fortuner")
car2 = Toyata("Prius")

print(car1.name)
print(car1.start())
print(car1.color)