# abstract class - Acts as a template
#                  used when we need to define a hierarchy of classes that
#                  share common attributes and behaviours
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class - a class which contains one or more abstract methods
# abstract method - a method which has a declaration but doesn't have an implementation

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You ride this Car")

    def stop(self):
        print("You stop the Car")


class Motorcycle(Vehicle):
    def go(self):
        print("You ride this Motorcycle")

    def stop(self):
        print("You stop the motorcycle")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
