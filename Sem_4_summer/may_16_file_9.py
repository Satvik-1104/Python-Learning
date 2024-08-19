# Duck typing - concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("This Duck is walking")

    def talk(self):
        print("This Duck is Qwuaking")


class Chicken:

    def walk(self):
        print("Tbis Chicken is walking")

    def talk(self):
        print("This Chicken in Clucking")


class Person:

    def catch(self, duck):

        duck.walk()
        duck.talk()
        print("You caught the Critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)  # this works because chicken has the same methods as duck does
# So, it walks like a Duck and Qwuaks like a Duck, So it is a Duck