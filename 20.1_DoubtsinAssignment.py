# Question: What are methods with respect to Classes and Objects?
'''
In OOPS, methods are functions that belong to a class and can be used by
its objects. They define behaviours of objects and allow them to perform
actions.

Types of Methods in Python Classes:
1. Instance Methods
2. Class Methods
3. Static Methods
'''

# 1. Instance Methods (Regular Methods):
# Work with individual objects (instances) of a class.
# Can access and modify instance variables (self.attribute).
# Always have self as the parameter.

class Car:
    total_cars = 0  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0  # default speed
        Car.total_cars += 1  # increment total_cars when a new car is created

    def accelerate(self, increase):  # instance method - it modifies self.speed, specific to car1
        self.speed += increase
        print(f"{self.brand} {self.model} is now going at {self.speed} kmph")

    @classmethod
    def get_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"


# Creating an object (instances)
car1 = Car("Toyota", "Corolla")
car1.accelerate(30)
print()
car2 = Car("Honda", "Civic")

print(Car.get_total_cars())

# 2. Class Methods (@classmethod)
# Works with the class itself, not individual objects.
# Use clas (instead of self) to access class-level attributes.
# Declared with the @classmethod decorator.

# 3. Static Methods (@staticmethod)
# Do not use self or cls.
# Independent ofunctions inside a class (for utility or helper tasks).
# Declared with @staticmethod.

class MathOperations:
    @staticmethod
    def add(x, y):  # static method because it does not depend on any class or instance variable
        return  x + y
print(MathOperations.add(5, 3))