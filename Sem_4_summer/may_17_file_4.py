# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
# Python will assign the __name__ variable a value of '__main__' if
# it is the initial module being run

# *****************************************************************
# if __name__ == '__main__'
# *****************************************************************

# why?
# 1. Module can be run as standalone program
# 2. Module can be imported and used by other modules
# 3. Allows modules to have some flexibility


def hello():
    print("Hello")


if __name__ == '__main__':
    hello()