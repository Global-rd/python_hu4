def add(num_1, num_2):
    sum = num_1 + num_2
    print(sum)
add(5, 10)


value = add(5, 10)
print(value)
print(type(value))

print("-------------")
def add(num_1, num_2):
    sum = num_1 + num_2
    return sum

value = add(1,2)
print(value)
print(type(value))

value = add(num_1=3, num_2=4)
print(value)

print("-------------")

def calculate_age_in_days(age_in_years):
    if age_in_years < 0:
        print("Age cannot be negative.")
        return
    age_in_days = age_in_years * 365
    return age_in_days

age_in_days = calculate_age_in_days(30)
print(age_in_days)

if age_in_days is not None:
    print(f"Age in days: {age_in_days}")


def multiply_two_numbers(a, b):
    return a*2, b*2
print(type(multiply_two_numbers(1, 2)))

x,y = multiply_two_numbers(1, 2)
print(x)
print(y)

# functions:
def remove_negative_numbers(numbers):
    for n in numbers[:]:
        if n < 0:
            numbers.remove(n)

    return numbers

numbers = [1, -2, 3, -4, 5]
print(remove_negative_numbers(numbers))
#csak pozitív számok

