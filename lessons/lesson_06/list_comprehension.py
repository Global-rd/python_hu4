import time

numbers = [1,2,3,4,5]

#for loop solution
squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

# list comprehension solution

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

# for loop solution
even_squares = []

for number in numbers:
    if number % 2 == 0:
        even_squares.append(number ** 2)

print(even_squares)

# list comprehension solution

even_squares = [number ** 2 for number in numbers if number % 2 == 0]

numbers = range(1, 1000000)
squares_loop = []
start = time.time()
print(start)
for num in numbers:
    squares_loop.append(num ** 2)

end = time.time()
print(f"For loop elapsed time: {end-start}")

start = time.time()
squares_comprehension = [num ** 2 for num in numbers]
end = time.time()
print(f"Comprehension elapsed time: {end-start}")

