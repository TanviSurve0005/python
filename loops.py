#For Loops

for i in range (0,6):
    print(i)
    print("Hello World")

for a in range (5,51,5):
    print(a)
from itertools import repeat

n= int(input("Enter the Number here: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#While Loop

n= int(input("Enter the Number Here: "))
i=1
while i<=10:
    print(n,"X",i,"=", n*i)
    i +=1

#While True Loop

while True:
    num1 = int(input("Enter a numer here: "))
    num2 = int(input("Enter a numer here: "))

    print(num1+num2)
    repeat = input("Do you want to stop the program: ")
    if repeat == "yes":
        break

#Nested Loops
#It is mostly used in the Pattern Problems
for i in range(1,5):
     for j in range(1,11):
         print(j, end="")
     print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

#For Loop with Conditional Statements

for i in range(1,11):
    if i == 3:
        print("This song is Emotions")
    else:
        print(i)

for i in range (1,101):
    if i%8==0 and i%12==0:
        print(i)

n=1
while n<=10:
    if n==3:
        print("add this to favs")
    else:
        print(n)
    n +=1

#Break and Continue Statement

for i in range(1,11):
    if i==5:
        continue
    elif i ==9:
        break
    else:
        print(i)