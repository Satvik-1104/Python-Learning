# thread - a flow of execution. Like a separate order of instructions.
#          However, each thread takes a turn running to achieve concurrency
#          GIL = (Global interpreter Lock)
# allows only one thread to hold the control of the Python Interpreter at any one time

# cpu bound - program/task spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound - program/task spends most of its time waiting for external events (user input, web scraping)
#            se multithreading

# daemon thread - a thread that runs in the background, not important for the program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non_daemon threads cannot actually be killed, stay alive until the task is complete
#                 ex: background tasks, garbage collection, waiting for input, long-running processes

import threading
import time

start = time.perf_counter()


def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("This program has run for " + str(count) + " secs")


def eat_breakfast():
    time.sleep(3)
    print("You ate Breakfast")


def drink_coffee():
    time.sleep(4)
    print("you drank Coffee")


def study():
    time.sleep(5)
    print("You have Studied")


# eat_breakfast()
# drink_coffee()
# study()

x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

# d = threading.Thread(target=timer, daemon=False)
d = threading.Thread(target=timer, daemon=True)
d.start()

# join is used for synchronization
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter() - start)
