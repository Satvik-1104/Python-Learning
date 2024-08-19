# string format - optional method that gives users more command when displaying outputs

animal = "quick brown fox"
item = "lazy dog"

print("A " + animal + " jumped over the " + item)

print("A {0} jumped over the {1}".format(animal, item))  # positional arguments - 0, 1 are default,
#                                                                avoiding them works too
print("A {1} jumped over the {0}".format(animal, item)) # positional arguments

print("A {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword arguments
print("A {item} jumped over the {animal}".format(animal="cow", item="moon"))
print("A {animal} jumped over the {animal}".format(animal="cow", item="moon"))

text = "A {} jumped over the {}"
print(text.format(animal, item))

# padding
name = "Satvik"

print("Hi! My name is {:10}".format(name))
print("Hi! My name is {:<10}".format(name))
print("Hi! My name is {:>10}".format(name))
print("Hi! My name is {:^10}".format(name))

# for numbers

pi = 3.14159
print("The number pi is {}".format(pi))
print("The number pi is {:.3f}".format(pi))

n = 1000
print("The number is {}".format(n))
print("The number is {:,}".format(n))
print("The number is {:b}".format(n))
print("The number is {:o}".format(n))
print("The number is {:x}".format(n))
print("The number is {:X}".format(n))
print("The number is {:e}".format(n))
print("The number is {:E}".format(n))
