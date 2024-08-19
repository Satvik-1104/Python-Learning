#lists - []: ordered and changeable
#tuples - (): ordered and unchangeable
#sets - {}: unordered and changeable and no duplicate values
#2D - lists

food = ["pizza", "hamburger", "spaghetti"]
print(food)
for items in food:
    print(items)

food.append("biryani")
food.remove("spaghetti")
food.pop()
food.insert(0, "apricot")
food.sort()

print()
for i in food:
    print(i)

drinks = ["coffee", "coke", "milkshake"]
dinner = ["maggi", "yippee", "knorr"]
dessert = ["vanilla", "butterscotch", "chocolate"]

meal = [drinks, dessert, dinner]

print(meal)

print()
student = ("satvik", 19, "male")
print(student.count("satvik"))
print(student.index("male"))

print()
utensils = {"fork", "spoon", "knife"}
for x in utensils:
    print(x)

set1 = {"cat", "dog", "mice"}
set2 = {"lizard", "dinosaur", "fish"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
print(utensils)

set1.update(set2)
print(set1)

animals = set1.union(set2)
print(animals)
print(set1.difference(set2))
print(set1.intersection(set2))