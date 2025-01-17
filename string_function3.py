a = "Harry Potter"

#endswith() - Returns true if the string ends with the specified value
print(a.endswith("t", 6,9))

#Startswith() - Returns true if the string starts with the specified value
print(a.startswith("P",6,10))

#swapcase() - Swaps cases, lower case becomes upper and vise versa
print(a.swapcase())

#strip() - Returns a trimmed version of the string
b = "   ****Tanvi Surve....  "
print(b)
print(b.strip(". , *, "))

#spit() - Split the string at the specified seperator, and returns a list
c="TanviSurve#KunalSurve#Bubbly"
d="Hello. My name is Tanvi. I am 20 Years old"
print(c.split("#"))
print(d.split("."))

#ljust - Returns a left justified version of the string
a = "Harry Potter"
x = a.ljust(20, "*")
print(x, "is my favorite movie")

#rjust - Returns a right justified version of the string
x = a.rjust(20, "*")
print(x, "is my favorite movie")

#replace() - Returns a string where specified value is replaced with a specified value
e = "My name is: *"
print(e)
print(e.replace("*","Tanvi Surve"))

#rindex() - Searches the string for a specified value and returns the last position of where it was found
print(e.rindex("*"))