fruits = ["apple", "raspberry", "watermelon", "elderflower"]

#without walrus operator:
treshold = 3
length = len(fruits)
print(length)

if length > treshold:
    print(f"The list has {length} items which is greater than the treshold: {treshold}")


#with walrus operator

if (length := len(fruits)) > treshold:
    print(f"The list has {length} items which is greater than the treshold: {treshold}")