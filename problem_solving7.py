#Convert the following dictionary into JSON format.

import json
student_data = {"name" : "David", "age" : 13, "marks":87}
print(type(student_data))
data = json.dumps(student_data)
print(data)
print(type(data))

#Pretty print following json data.
student_data = {"name" : "David", "age" : 13, "marks":87}
data = json.dumps(student_data, indent=4 , separators = (",","="))
print(data)

#Sort the following json keys and write them into a file.
student_data = {"name" : "David", "age" : 13, "marks":87}
f = open("demo.json","w")
data = json.dumps(student_data, indent=4, sort_keys= True)
f.write(data)
print("The data has been added to the file")

#Access the nested key "marks" from the following nested data
student_data = '''{ 
    "student": {
        "grade": {
            "name": "David",
            "marks": {
                "math": 87
            }
        }
    }
}'''

data = json.loads(student_data)
print(data["student"]["grade"]["marks"])