#Write a program to find sum of all the even numbers up to 50

"""sum = 0
for i  in range(1,51):
    if i%2==0:
        print(i)
        sum +=i
print(sum)
#Write a program to write 20 numbers and their square numbers

for i in range(1,21):
    print(i, "=", i*i)

#Write a program to find sum of first 10 odd numbers


# Initialize variables
count = 0
sum_odd = 0
number = 1  # Start with the first odd number

# Iterate through the first 10 odd numbers
while count < 10:
    sum_odd += number  # Add current odd number to sum
    number += 2  # Move to the next odd number
    count += 1  # Increment count

# Print the sum of the first 10 odd numbers
print("Sum of the first 10 odd numbers:", sum_odd)
from loops import repeat

#Write a program to check if number is divisible by 8 and 12, up to 100 numbers

for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i)"""

#Write a program to make Supermarket Billing System

while True:
    name= input("Enter your Name: ")
    total =0
    while True:
        quantity = int(input("Enter the Quantity:"))
        amount = float(input("Enter your Amount: "))
        total += quantity*amount
        repeat = input("You want to add the Items anymore? (yes/no): ")
        if repeat == "Yes":
            continue
        else:
            break

    print("-"*40)
    print("Billing Printing")
    print("Name: ",name)
    print("Total Amount: ",total)
    print("-" * 40)
    repeat1 = input("You want to Make More bills? (yes/no): ")
    if repeat1=="yes":
        continue
    else:
        break


