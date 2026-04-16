condition = False

if condition == True:
    print("the condition is true")    
else:
    print("the condition is false")

# truthy-falsy values

print(bool(1))
print(bool(0))
print(bool("apple"))
print(bool(""))
print(bool([]))
print(bool([1,2,3]))

if condition:
    print("condition is true")
else:
    print("condition is false")


number = None

if number:
    print(f"The value is not 0: {number}")
else:
    print(f"The value is zero or None!")


my_list = [1,2,3]

if my_list:
    print("the list has items")
else:
    print("the list has no items")


#
print("------")
number = 17

if number == 15:
    print("the number is 15")
elif number == 16:
    print("the number is 16")
elif number == 17:
    print("the number is 17")
else:
    print("The value of the number is something else")


# using membership operators

fruits = ["apple", "watermelon", "raspberry", "banana"]

if "watermelon" in fruits:
    print("watermelon is present in the fruit list")

if "banana" in fruits:
    print("banana is present in the fruit list")


# identity operators

a = 2
b = 2
c = 3

if a is b:
    print("The 2 objects are the same by ID!")


#combining multiple operators:

if (a is not b and c == 4) and ("cherry" in fruits or "apple" in fruits):
    print("OK")
else:
    print("NOT OK!")


