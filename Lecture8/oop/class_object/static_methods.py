"Static Methods"

# Methods that don't use the self parameter. (work at class level)

class Student:
    @staticmethod #decorator
    def college():
        print("ABC College")


        """Decorators allow us to wrap another function
        in order to extend the behaviour of the wrapped function, 
        without permanently modifying it."""

        "So basically when we create a method we need self keyword to create an object in class, "
        "but static method runs it without self keyword, sometimes we don't always need self or object creating in the method, To run a simple fn"
        "Static method become handy."

        