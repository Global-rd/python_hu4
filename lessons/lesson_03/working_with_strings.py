fruit = "banana and apple"
fruit_length = len(fruit)
print(fruit_length)

first_name = "Istvan Gabor"
last_name = "Nagy"

# concatenation / konkatenálás
full_name = first_name + " " + last_name
print(full_name)
introduction = "My name is " + first_name + " " + last_name + "."
print(introduction)

#interpolated string / f-string
introduction = f"My name is {first_name} {last_name}."
print(introduction)

#indexing,slicing,striding
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[-1])
print("------------")
print(fruit[1:3]) # 1: inclusive, 3: exclusive
print(fruit[3:])
print(fruit[-2:])
print(fruit[-1::-1])


#string methods
#metódus: az amit egy objektum csinálni tud / amit az objektummal csinálni lehet 
#attribútum: az ami jellemzi az objektumot

#objektum: kutya
#metódus: ugat, eszik, alszik, csahol
#attribútum: fajta, életkor, név, szőre színe

print("-------")
print(fruit)
print(fruit.capitalize())
print(fruit.upper())
print(fruit.title())

print(fruit.replace("a", "*"))

fruit = "    apple   "
print(fruit.strip())

#method chaining

print(fruit.upper()
           .replace("A", "#")
           .strip())

fruit = "abbbaaa"
print(fruit.strip("a"))