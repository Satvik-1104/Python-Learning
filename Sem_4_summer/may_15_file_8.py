#indexing and functions

def isCapitalized(name):
    if name[0].islower():
        print("lower")
        return name.capitalize()


def getLastName(name):
    last_name = name[:9].upper()
    print(last_name)


def getFirstName(name):
    first_name = name[10:].lower()
    print(first_name)


def getLastLetter(name):
    last_letter = name[-1]
    print(last_letter)


name = "vadisetti Pranay Satvik Reddy"
name = isCapitalized(name)
print(name)
print()

getLastName(name)

getFirstName(name)

getLastLetter(name)