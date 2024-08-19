# zip(*iterables) - aggregate elements from two or more iterables (list, tuples, set, etc.)
#                   creates a zip object with paired elements stored in tuples for each element


usernames = ['Satvik', 'Divyagnan', 'TSP', 'Siva Mani']
passwords = ('sunnyreddy04', '!(&$', '2005', '172427')

users = dict(zip(usernames, passwords))
for i, j in users.items():
    print(i + ": " + j)
