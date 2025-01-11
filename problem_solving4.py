#A= "Why fit in, When you are Born to Stand Out!"
# Write a program to find the length of the following string

string = "Why fit in, When you are Born to Stand Out!"
print(len(string))

#Write a program to check how many times alphabet o is occurring

print(string.count("O"))
print(string.count("o"))

#Write a  program to convert the whole string into lower and upper case

a=string.lower()
print(a)
b=string.upper()
print(b)

# Write a program to convert the following string into a title.
c= string.title()
print(c)

#write a program to find the index number of "fit in".
print(string.find("fit in"))


for i in range(1,6):
    for j in range(1, i+1):
         print("*", end="")
    print()

for i in range(1,6):
    for j in range(1, i+1):
         print(i, end="")
    print()

for i in range(1,6):
    for j in range(6, i,-1):
         print(i, end="")
    print()

for i in range(1,6):
    for j in range(5, i, -1):
         print(" ", end=" ")
    for k in range (i):
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(i, 0 ,-1):
        print(j, end=" ")
    print()

for i in range(1,6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
for i in range(5, 0 ,-1):
    for k in range(0, i-1):
        print("*", end=" ")
    print()

for i in range(1,11):
    for j in range(1,i+1):
        print(i*j, end=" ")
    print()