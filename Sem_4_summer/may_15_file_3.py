#user input and math module and if, else, elif
#logical operators (and, or, not)
#         not needs a set of parenthesis - not(statement)
#while loop
#for loop

import math
import time

name = input("What is your name?: ")
print("Hello " + name)

age = int(input("How old are you?: "))
print("You are " + str(age) + " years old")

if age < 0:
    print("Bro! Seriously?")
elif age < 18:
    print("You cannot watch Demon Slayer")
elif age < 60:
    print("You can enjoy demon Slayer")
elif age < 100:
    print("OK boomer")
elif age == 100:
    print("RIP")
else:
    print("Still Batting??")

height = float(input("How tall are you?: "))
print("You are " + str(height) + "cm tall")

print()
print(round(height))
print(math.ceil(height))
print(math.floor(height))
print(abs(height))
print(pow(height, 1.732))
print(math.sqrt(4))
print(max(height, 177, 190))

print()
temp = float(input("What is the temperature right now?: "))
if not (temp > 20 and temp < 37):
    print("The temperature is bad today")
    print("Stay inside")

elif not (temp < 20 or temp > 37):
    print("The temperature is good today")
    print("You can play outside")

print()
i = 0
while i < 10:
    print(i)
    i += 1

print()
college = ""
while len(college) == 0:
    college = input("Where are you studying?: ")

print()
for j in range(1, 101, 2):
    print(j)
    time.sleep(0.2)