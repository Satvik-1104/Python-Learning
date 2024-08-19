# POOP - Python Object-Oriented Programming
# class and instance variables
# class variables are declared outside constructor
# instance variables are declared inside constructor
# inheritance
# multilevel inheritance - when a child class inherits another child class
# multiple inheritance - when a child is derived from more than one parent class
# method overriding
# method chaining - calling multiple methods sequentially
#                   each call performs an action on the same object and returns self
# passing objects as arguments

class Vehicle:

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def move(self):
        print("This {} {} moves".format(self.make, self.model))


class Bike(Vehicle):

    wheels = 2  # class variable
    running = True

    def drive(self):
        print("This {} {} is driving".format(self.make, self.model))

    def stop(self):
        print("This {} {} is parked".format(self.make, self.model))

    def turn_on(self):
        print("{} {}'s engine is started".format(self.make, self.model))
        return self

    def gas(self):
        print("{} {} is accelerating".format(self.make, self.model))
        return self

    def brake(self):
        print("{} {} is decelerating".format(self.make, self.model))
        return self

    def turn_off(self):
        print("{} {}'s engine is stopped".format(self.make, self.model))
        return self


def change_color(vehicle, color):
    vehicle.color = color


class Sport(Bike):
    def race(self):
        print("This {} {} is good for racing as it is a sports bike".format(self.make, self.model))

    def drive(self):
        print("{} {} is a sports bike. So it runs faster".format(self.make, self.model))


class Cruiser(Bike):
    def cruise(self):
        print("This {} {} is comfortable for travelling to far off places".format(self.make, self.model))

    def drive(self):
        print("{} {} is a cruiser. So it runs smoother".format(self.make, self.model))


class Fused(Sport, Cruiser):
    def comfy(self):
        print("This {} {} is comfortable for both cruising and racing".format(self.make, self.model))


bike_1 = Cruiser('Triumph', 'Rocket Gt', 2021, 'red')
bike_2 = Cruiser('Kawasaki', 'Vulcan S', 2019, 'black')
bike_3 = Sport('Ducati', 'Diavel', 2022, 'red')
bike_4 = Fused('Harley Davidson', 'Hotrod', 2020, 'blue')

print(bike_1.make)
print(bike_2.model)
print(bike_1.year)
print(bike_2.color)

change_color(bike_2, 'Dull Black')
print(bike_2.color)

print()
bike_1.drive()
bike_3.drive()
bike_2.stop()

print(Bike.wheels)

print()
bike_3.race()
bike_2.cruise()
bike_2.stop()
bike_3.stop()
bike_3.move()
bike_1.cruise()
bike_3.race()
bike_4.cruise()
bike_4.race()
bike_4.comfy()
bike_4.drive()

bike_1.turn_on().gas().brake().turn_off()
