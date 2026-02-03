"Super method: Super() method is used to access methods of a parent class"

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("START")

    @staticmethod
    def stop():
        print("STOP")

class ToyataCar(Car):
    def __init__(self, name, type): #accessing type from car base class
        super().__init__(type)
        self.name = name
        super().start()
        
car2 = ToyataCar("Prius", "Electric")
print(car2.type)
