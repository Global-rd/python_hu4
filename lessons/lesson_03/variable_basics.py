name = "Jim"
age = 25

print(age)

age = 25 + 1
print(age)

camelCaseVariableName = "" #CAMELCASE -> BAD PRACTICE PYTHON-BAN
snake_case_variable_name = "" #SNAKE CASE -> GOOD PRACTICE PYTHON-BAN

#CONSTANTS / KONSTANSOK

PI = 3.14
MAX_ROUNDS = 3

# DYNAMICALLY TYPED / DINAMIKUS TÍPUSOSSÁG

#int x = 25
x = 25

x = "appletree"
print(x)
print(x*3)


#reference

print("---------")
my_var = 10
my_var2 = 10

print(id(my_var))
print(id(my_var2))

#my_var -> 10
#my_var2 -> 10

print("---------")

x = 11
y = x #11

print(id(x))
print(id(y))
print(x)
print(y)

x = 10

print(id(x))
print(id(y))
print(x)
print(y)


#GARBAGE COLLECTION / REFERENCE COUNTING
x = 1000 # 1000's reference count: 1
x = 2000 # 1000's reference count: 0