a= ["Thor", "Hulk", "Hulk", "Ironman", "Captian America"]
print(a)

# to find length of a list
print(len(a))

# to count an occurence of a particular element
print(a.count("Hulk"))

# to add to the list
a.append("Tanvi")
print(a)

# to add to a specific location
a.insert(1, "Vision")
print(a)

# to remove from a list
a.remove("Hulk")
print(a)

# to remove from the specific location
a.pop(0)
print(a)

# to create the copy of the list
b = []
print(b)
b = a.copy()
print(b)

# to access a copy of a list
print(a.index("Ironman"))

# to extend an element
c = ["Vision", "Spiderman"]
a.extend(c)
print(a)

# to reverse the list
a.reverse()
print(a)

# to sort the list
a.sort()
print(a)

# to clear all the data from the list
a.clear()
print(a)