#random and exception handling

import random

x = random.randint(1, 6)
print(x)
y = random.random()
print(y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'Q', 'J', 'A']
random.shuffle(deck)
print(deck)

try:
    n = int(input("Enter numerator: "))
    d = int(input("Enter denominator: "))
    print(n / d)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero Idiot!!")
except ValueError as e:
    print("Please divide by an integer.")
    print(e)
except Exception as e:
    print("Error found. Check!!")
    print(e)
finally:
    print("This will always execute!")
