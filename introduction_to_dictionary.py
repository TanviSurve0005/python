#Dictionary are allow user to write the data in the form of keys and values
employee_data = {"name" : "John", "age" : 24, "gender" : "Male"}
"""print(employee_data["age"])

#Iteration in Dictionary

#Printing all the key names one by one
for x in employee_data:
    print(x)"""

#Printing all the values names one by one
for x in employee_data:
    print(employee_data[x])

#Use value function
for x in employee_data.values():
    print(x)

#Using Item function

for x,y in employee_data.items():
    print(x,":",y)