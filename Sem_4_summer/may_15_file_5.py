# nested loops
# loop control statements (break, continue, pass)

rows = 6
for i in range(rows):
    for j in range(i):
        print("*", end="")
    for j in range(i, 5):
        print("!", end="")
    for j in range(5, 10 - i):
        print("!", end="")
    for j in range(10 - i, 10):
        print("*", end="")
    print()

name = ""

while True:
    name = input("What is your name?: ")
    if len(name) != 0:
        break

aadhaar = "5602-0693-7169"
for i in aadhaar:
    if i == '-':
        continue
        print(" - found")
    else:
        print(i, end="")
print()

for i in aadhaar:
    if i == '-':
        pass
        print()
        print(" - found")
    else:
        print(i, end="")