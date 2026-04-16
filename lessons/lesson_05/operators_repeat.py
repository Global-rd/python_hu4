#arithmetic operators

a = 1 + 2
print(7//3)

#assignment operators
x = 12
x += 5

#comparison operators
a = 2
b = 3
print(a != b)
print(a == b)

#logical operators

a = True
b = False
print(a and b)
print(a or b)
print(not a and not b)

x = 9
y = 3

print(x < 10 and y == 2)
print(x < 10 or y == 2)

#identity operators
print("-----------")
a = 10
b = 10

print(a == b)
print(a is b)

print(id(a))
print(id(b))

print("------")

x = [1,2,3]
y = [1,2,3]

print(id(x))
print(id(y))

print(x == y)
print(x is y)

######
print("---------------")
x = [1,2,3]
y = x

x.append(4)

print(id(x))
print(id(y))

print(x)
print(y)


print("-----")

a = 10
b = a

a = 11


#membership operators

print("------------")

print(1 in x)
print(1 not in x)


# operator precedence

print("-----------")

print(True or False and False)
print((True or False) and False)

#short circuit evaluation

print(False and True and False and True)