# Walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# assigning a function to a variable

# happy = True
# print(happy)

print(happy := True)
print()

# foods = list()
# while True:
#     food = input("what food do you like? (type 'quit' to exit loop): ")
#     if food == 'quit':
#         break
#     foods.append(food)
# print(foods)

foods = list()
while (food := input("What foods do you like? (type 'quit' to exit loop): ")) != 'quit':
    foods.append(food)

print(foods)

say = print
say("Whoa!! I can't believe this works :o !!")
