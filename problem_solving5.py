#Write a program to get Fibonacci Series up to 10 numbers
"""a=0
b=1
n = int(input("Enter your number here: "))
if n==1:
    print("1")
elif n<=0:
    print("0")
else:
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)

#Check whether the number is prime or not
number = int(input("Enter your number here: "))
if number <=1:
    print("It is not a Prime Number")
else:
    for i in range(2,number):
        if number % i == 0:
            print("It is not a Prime Number")
            break
    else:
            print("It is a Prime Number")

#Check whether the number is palindrome or not

number = int(input("Enter your number here: "))

if str(number) == str(number)[::-1]:
    print("The Number is Palindrome.")
else:
    print("The Number is not a Palindrome")"""


#Area Calculator
while True:
    print("-----Area Calculator------")
    print("""press 1 to get the area of square
    press 2 to get the area of rectangle
    press 3 to get the area of circle
    press 4 to get area of triangle"""
    )

    choice = int(input("Enter the number between the 1-4: "))

    if choice ==1:
        while True:
            print("Square Area")
            length= int(input("Enter the Length of the Square: "))
            square = length * length
            print("Area of the Square is: ", square)
            repeat = input("Do you want to try again with the Square?")
            if repeat=="no":
                break
            else:
                continue

    elif choice ==2:
        while True:
            print("Rectangle Area")
            length = int(input("Enter the Length of the Rectangle: "))
            breadth = int(input("Enter the Breadth of the Rectangle: "))
            rectangle = length * breadth
            print("Area of the Rectangle is: ", rectangle)
            repeat = input("Do you want to try again with the Rectangle?")
            if repeat == "no":
                break
            else:
                continue

    elif choice ==3:
        while True:
            print("Circle Area")
            radius = int(input("Enter the radius of the Circle: "))
            circle = ((22/7)*(radius**2))
            print("Area of the circle is: ",circle)
            repeat = input("Do you want to try again with the Circle?")
            if repeat == "no":
                break
            else:
                continue

    elif choice ==4:
        while True:
            print("Triangle Area")
            base = int(input("Enter the Base of the triangle: "))
            height = int(input("Enter the height of the triangle: "))
            triangle = 0.5*base*height
            print("Area of the triangle is: ",triangle)
            repeat = input("Do you want to try again with the Triangle?")
            if repeat == "no":
                break
            else:
                continue

    else:
        print("Please Enter the correct choice")

    repeat1 = input("Do you want to repeat the menu?")
    if repeat1=="no":
        break
    else:
        continue