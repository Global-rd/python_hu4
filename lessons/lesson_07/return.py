
def add(num_1, num_2):
    sum = num_1 + num_2
    print(sum)

value = add(1,2)
print(value)
print(type(value))

print("------------")
def add(num_1, num_2): #num_1, num_2: parameters
    sum = num_1 + num_2
    return sum

value = add(1,2) #1,2: positional arguments
print(value)
print(type(value))
 
value = add(num_1=1, num_2=2) #keyword argument!

#return early


def calculate_age_in_days(age_in_years):
    if age_in_years < 0:
        print("Invalid age! Please provide a positive number!")
        return 
    age_in_days = age_in_years * 365
    return age_in_days

age_in_days = calculate_age_in_days(15)
print(age_in_days)
age_in_days = calculate_age_in_days(-1)
print(age_in_days)

# returning multiple values

def multiply_two_values(a, b):
    return a*2, b*2

print(type(multiply_two_values(1,2)))


x,y = multiply_two_values(1,2)
print(x)
print(y)

# functions:
def remove_negatives(nums):
    for n in nums[:]:
        if n < 0:
            nums.remove(n)
    
    return nums


numbers = [1, -3, 4, -5]
print(remove_negatives(numbers))


