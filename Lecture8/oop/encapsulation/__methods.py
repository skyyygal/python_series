class Person:
    __name = "anonymous" #conceptually private. 

    def __hello(self, name):
        print("Hello", name)

    def welcome(self):
        self.__hello(self.__name)
p1 = Person()

p1.welcome()
