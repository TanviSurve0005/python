# Tuples are the collection of ordered and the un-mutable data

a = ("Mango", "Banana", "Apple",1,2,58,87)
print(type(a))
print(a)

b = ("Ironman",)
print(type(b))
print(b)

#Slicing and Iterations in the Tuples
#Slicings
print(a[1:3])

print(a[:3])

print(a[2:])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

#Iterations

#With for loop
for i in (a):
    print(i)
#Along with range and length in for loop
for i in range(len(a)):
    print(a[i])


#Along with while loop
i =0
while i < len(a):
    print(a[i])
    i+=1