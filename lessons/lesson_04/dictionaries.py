from pprint import pprint

student = {
    "name": "John",
    "age": 18,
    "grades": {"grammar": [1,2,3],
               "math": [4,5,5]},
    "major": "computer science",
    "is_active": True
}

pprint(student)

#accessing values
print(student["grades"]["grammar"][-1])
print(type(student["grades"]))

#accessing keys
print(student.keys())
print(type(student.keys()))

#accessing keys
print(student.values())
print(type(student.values()))

#modifying values
student["name"] = "Harry"
pprint(student)

print(student["grades"]["math"].append(1))
pprint(student)


#mapping table

us_grade_mapping = {
    5: "A",
    4: "B",
    3: "C",
    2: "D",
    1: "F"
}

latest_grade = int(input("Grade: "))
us_grade = us_grade_mapping[latest_grade]
print(us_grade)