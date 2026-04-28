def divide_numbers(a, b):
    return a / b

# ZERO DIVISION ERROR
result = divide_numbers(a=10, b=1)
print(result)

# VALUE ERROR
#age = int(input("How old are you? Please provide a number!"))
#print(age)


# INDEX ERROR
my_list = [1,2,3,4,5]
print(my_list[1])

#KEY ERROR

my_dict = {"a": 12,
           "b": 13}

#print(my_dict["c"])
print(my_dict.get("c",100))


#try:
#    a = float(input("first number: "))
#    b = float(input("second number: "))
#    c = a / b
#    print(c)
#except ValueError as e:
#    print(f"Value Error: {e}")
#except ZeroDivisionError as e:
#    print(f"Zero Division Error: {e}")
#except Exception as e:
#    print(f"Something unexpected happened: {e}")
#finally:
#    print("Division attempt finished.")


#bad example:
def calculate_rectangle_area(a, b):
    return a * b

print(calculate_rectangle_area(-1,8))

#good example:
def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0: #guard clause
        raise ValueError("Both params must be a positive number!")
    return length * width

try:
    area = calculate_rectangle_area(5, -1)
except ValueError as e:
    print(f"valueerror: {e}")

