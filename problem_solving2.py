#Write a program to check if a number is positive or not

number = int(input("Enter your Number: "))
if number>0 :
    print("The number is positive")
else:
    print("The number is negative")

#Write a program to check if a number is odd or even

number = int(input("Enter your Number: "))
if number%2==0 :
    print("The number is Odd")
else:
    print("The number is Even")

#Write a program to create area calculator

print("-----Area Calculator------")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get area of triangle"""
)

choice = int(input("Enter the number between the 1-4: "))

if choice ==1:
    print("Square Area")
    length= int(input("Enter the Length of the Square: "))
    square = length * length
    print("Area of the Square is: ", square)
elif choice ==2:
    print("Rectangle Area")
    length = int(input("Enter the Length of the Rectangle: "))
    breadth = int(input("Enter the Breadth of the Rectangle: "))
    rectangle = length * breadth
    print("Area of the Rectangle is: ", rectangle)
elif choice ==3:
    print("Circle Area")
    radius = int(input("Enter the radius of the Circle: "))
    circle = ((22/7)*(radius**2))
    print("Area of the circle is: ",circle)
elif choice ==4:
    print("Triangle Area")
    base = int(input("Enter the Base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    triangle = 0.5*base*height
    print("Area of the triangle is: ",triangle)
else:
    print("Please Enter the correct choice")

#Write a program check whether the passed letter is vowel or not

letter = input("Enter the letter here: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("The letter is Vowel")
else:
    print("Letter is not Vowel")

#Write a program to check if a number is single digit number,or multiple digit number

number = int(input("Enter the number here: "))
if number<10:
    print("The number is single digit")
elif number>=9 and number<=99:
    print("The number is two digit")
elif number>=99 and number<=999:
    print("The number is Three digit")
elif number>=999 and number<=9999:
    print("The number is four digit")
elif number>=9999 and number<=99999:
    print("The number is five digit")
else:
    print("Enter the correct Number")