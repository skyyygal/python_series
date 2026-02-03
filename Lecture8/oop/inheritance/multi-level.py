class Car:
    color = "black"
    @staticmethod
    def start():
        print("START")


    @staticmethod
    def stop():
        print("STOP")


class Toyata(Car):
    def __init__(self, brand):
        self.brand= brand

class Fortuner(Toyata):
    def __init__(self,type):
        self.type = type
        # 
# car1 = Toyata("Fortuner")
# car2 = Toyata("Prius")

car1 = Fortuner("Diesel")

print(car1.type)