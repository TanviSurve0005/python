#if-the statement
marks = 100
if marks >= 90:
    print("You will get a mobile phone")

print("Thank you")

#is-else statement
marks = 80
if marks >= 90:
    print("You will get a mobile phone")
else:
    print("No phone for a week")
print("Thank you")

#if-elif-else statement
marks = 50
if marks >= 90:
    print("You will get a mobile phone")
elif marks>=80:
    print("You will get a phone for a week")
else:
    print("You will get a phone for a One Day")
print("Thank you")

#neste-if statement
marks = 70
if marks >= 90:
    print("You will get a mobile phone")
    if marks>=80:
        print("You can go to a trip")
else:
    print("No one can give you a single things")
print("Thank you")

#short-hand-if statement
marks = 100
if marks >= 90: print("You will get a mobile phone")

print("Thank you")

#short-hand-if-else statement
marks = 80
print("You will get a mobile phone") if marks >= 90 else print("No phone for a month")

print("Thank you")