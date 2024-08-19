#dictionary - faster but takes more space, changeable and unordered, unique

capitals = {
                "USA": "Washington DC",
                "India": "New Delhi",
                "Sri Lanka": "Colombo",
                "France": "Paris"
           }

for key, value in capitals.items():
    print(key + ": " + value)

print()
print(capitals["India"])
print(capitals.get("Germany"))

print(capitals.values())
print(capitals.keys())
print(capitals.items())

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
capitals.pop("Sri Lanka")
print(capitals)
capitals.clear()