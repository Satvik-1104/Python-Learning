# list comprehension - a way to create new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

# Dictionary comprehension - create dictionaries using an expression
#                            can replace for loops and certain lambda functions
# dictionary = {key: expression for key, value in iterable}
# dictionary = {key: expression for key, value in iterable if conditional}
# dictionary = {key: (if / else) for key, value in iterable}
# dictionary = {key: function(value) for key, value in iterable}

squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares_lc = [i * i for i in range(1, 11)]
print(squares_lc)

students = [100, 90, 55, 79, 81, 46, 87, 56, 41, 23, 89]
passed = list(filter(lambda x: x >= 60, students))
print(passed)

passed_lc = [i for i in students if i >= 60]
print(passed_lc)

passed_lc_if_else = [i if i >= 60 else "FAIL" for i in students]
print(passed_lc_if_else)

countries = {
    'India': 40,
    'Canada': 22,
    'Pakistan': 35,
    'Nepal': 26,
    'Bangladesh': 37,
    'Singapore': 45
}

print()
d_c = {key: round((9/5)*value) + 32 for (key, value) in countries.items()}
print(d_c)

d_c_if = {key: value for key, value in countries.items() if value <= 30}
print(d_c_if)

d_c_if_else = {key: "COLD" if value <= 30 else "HOT" for key, value in countries.items()}
print(d_c_if_else)


def check_temp(value):
    if value < 26:
        return "COLD"
    elif 26 <= value <= 34:
        return "NORMAL"
    else:
        return "HOT"


d_c_func = {key: check_temp(value) for key, value in countries.items()}
print(d_c_func)
