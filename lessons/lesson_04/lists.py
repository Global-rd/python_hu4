from typing import List
letters = ["a", "b", "a", "c", "d"]
print(letters)

mixed_type_list = ["a", True, 3, 3.14, None]
print(mixed_type_list)
print(type(mixed_type_list))


letters = list()

#indexing
names = ["Tim", "Jimmy", "Sarah"]

print(names[0])
print(names[:2])

numbers = list(range(1,10))
print(numbers)
print(type(numbers))

names[0] = "Jim"
print(names)

names[:2] = ["Timmy", "Jeremy"]
print(names)

#inserting more
names[1:2] = ["Tarah", "Mariah"]
print(names)

#inserting less
names[1:3] = ["James"]
print(names)

#names[1:3] = "Timmy" bad practice!
print(names)

#methods

names.append("Cathlyn")
print(names)

names.extend(["Bruno", "Timothy"])
print(names)
print(len(names))

names.insert(2, "Jimmy")
print(names)

#remove by value
names.remove("Jimmy")
print(names)

#remove by index
names.pop(2)

del names[1]

#sorting
names.sort()

#full deletion
names.clear()

chocolates = input("Give me your 3 favourite chocolates separated by a comma!")
print(chocolates)
print(type(chocolates))

chocolates_list = chocolates.split(",")
print(chocolates_list)
