student={
    "name":"neha",
    "score":{
        "chem":98,
        "phy":97,
        "math":99
        }    
        }

# typecast
print(list(student.keys()))  

print(len(student))

print(len(student.keys()))
print(student.keys())

print(student.values())

print(student.items())

print(student.get("key"))

student.update({"city":"kolkata"})
print(student)

