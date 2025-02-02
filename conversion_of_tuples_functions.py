#When we want to insert or delete the things in the tuple just
# covert it into the list and then perform the list functions
a = ("Oneplus","Nokia", "Redmi")
print(type(a))
print(a)
a = list(a)
print(type(a))

a.append("vivo")
a.insert(1, "Tanvi")
a.insert(1, "Tanvi")
print(a)

print(a.count("Tanvi"))
print(a.index("Nokia"))