a = ["Ross", "Rachel", "Monica", "Joe"]
print(a)
# Write a program to swap first and forth element.
a[0],a[3] = a[3],a[0]
print(a)

# Write a program to add new value at second position
a.insert(1,"Tanvi")
print(a)

#Write a program to delete a value from the 3rd position
a.pop(2)
print(a)

b = [13,7,12,10]

#write a program to multiply all the numbers in the list
mul = 1
for i in (b):
    mul *= i
print(mul)

# write a program to get largest number from the list
#Arrange the list in the ascending order then apply method on it
b.sort()
print(b)
print("The largest Value in the given list is :", b[-1])
print("The smallest Value in the given list is :", b[0])

