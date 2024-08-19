# file handling

import os

path = "C:\\Users\\HP\\PycharmProjects\\satvik_py\\text.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")
print()

try:
    with open('text2.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("The file you referred to doesn't exist!!!")

with open ("text.txt", "a") as file:
    file.write("\nThis line is also appended into the file!")

with open ("text2.txt", "w") as file:
    file.write("This file didn't exist actually. It is created just now")