# keyword arguments
# nested function calls - function calls inside a functions
# variable scope
#       order - L(local), E(enclosing), G(global), B(built in)

# *args - parameter that will pack all arguments into a tuple
#         useful so that a function can accept varying number of arguments
# **kwargs - parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying number of keyword arguments

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="reddy", middle="pranay satvik", first = "vadisetti")
print()

num = input("Enter a number: ")
print(str(round(abs(float(num)))))
print()


def sum(* args):
    sum = 0
    for i in args:
        sum += i
    return sum


result = sum(1, 2, 3, 5)
print(result)


def hi(**kwargs):
    print("Hi!!", end="")
    for key, value in kwargs.items():
        print(value, end=" ")


hi(title = "Mr.", first = "Pranay", middle = "Satvik", last = "Reddy")