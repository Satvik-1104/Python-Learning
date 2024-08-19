# Higher Order Functions - a function that either:
#                          1. accepts a function as an argument
#                                   or
#                          2. returns a function
#                          (In Python, functions are also treated as objects)
# lambda functions in Python - function return in one line using lambda keyword
#                              accepts any number of arguments but has only one expression
#                              (think of it as a shortcut)
#                              (useful if needed for a short period of time, throw-away)
# sort() method - used with lists
# sort() function - used with iterables
# map() function - applies a function to each item in an iterable (tuple, list, etc)
#                  map(function, iterable)
# filter() function - creates a collection of elements from an iterable
#                     for which a function returns true
#                     filter (function, iterable)
# reduce function - apply a function to an iterable and reduce it to a single cumulative value
#                   performs function on first two elements and repeats process until 1 value remains
#                   reduce (function, iterable)
#                   import functools


import functools
# accepting a function as argument
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def intro(func):
    text = func("I am Vadisetti Pranay Satvik Reddy")
    print(text)


intro(loud)
intro(quiet)


# returning a function
def dividend(x):
    def divisor(y):
        return x / y
    return divisor


divide = dividend(90)
for i in range(1, 46):
    print(divide(i))


# lambda function
#          lambda parameter:expression


print()
# def double(x):
#     return x * 2
double = lambda x: x * 2
print(double(13))
multiply = lambda x, y: x * y
print(multiply(5, 8))
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Pranay Satvik Reddy", "Vadisetti"))
age_check = lambda age: True if age >= 18 else False
print(age_check(19))


# lists - sort() method
students = [
    ('Satvik', 'A', 19),
    ('Siva Mani', 'C', 18),
    ('Jignesh', 'A', 20),
    ('Divyagnan', 'B', 22),
    ('Pranav', 'D', 12)
]

age = lambda ages: ages[2]
grade = lambda grades: grades[1]
name = lambda names: names[0]

students.sort(key=name)
for i in students:
    print(i)
print()
students.sort(key=name, reverse=True)
for i in students:
    print(i)
print()
students.sort(key=grade)
for i in students:
    print(i)
print()
students.sort(key=grade, reverse=True)
for i in students:
    print(i)
print()
students.sort(key=age)
for i in students:
    print(i)
print()
students.sort(key=age, reverse=True)
for i in students:
    print(i)
print()


# iterables - sort() function
student = (
    ('Satvik', 'A', 19),
    ('Siva Mani', 'C', 18),
    ('Jignesh', 'A', 20),
    ('Divyagnan', 'B', 22),
    ('Pranav', 'D', 12)
)

sorted_students = sorted(student, key=name)
for i in student:
    print(i)
print()
sorted_students = sorted(student, key=name, reverse=True)
for i in student:
    print(i)
print()
sorted_students = sorted(student, key=grade)
for i in student:
    print(i)
print()
sorted_students = sorted(student, key=grade, reverse=True)
for i in student:
    print(i)
print()
sorted_students = sorted(student, key=age)
for i in student:
    print(i)
print()
sorted_students = sorted(student, key=age, reverse=True)
for i in student:
    print(i)
print()


# map function
store = [
    ('Shirt', 880),
    ('Pants', 1300),
    ('Jacket', 1450),
    ('Shoes', 2000),
    ('Socks', 160)
]

to_dollars = lambda data: (data[0], data[1] / 83.47)
store_US = map(to_dollars, store)
for i in store_US:
    print(i)
print()


# filter function
friends = [
    ('Ramu', False),
    ('Divya', True),
    ('Sai', False),
    ('Siva Mani', False),
    ('Pranav', True),
]


def free_fire(data):
    return data[1] == True


free_fire_buddies = filter(free_fire, friends)
for i in free_fire_buddies:
    print(i)
print()


# reduce function
letters = ['H', 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x, y: x + y, letters)
print(word)
print()

numbers = [2, 2, 1, 2, 2, 1, 3, 6]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product)
