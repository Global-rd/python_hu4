import time
songs = ["Warrior", "I'm a barbie girl", "Heavy is the crown", "I got options"]


for song in songs:
    print(f"Playing {song}")
    #time.sleep(2)

student = {
    "name": "John",
    "age": 15,
    "spec": "CS"
}

for k,v in student.items():
    print(k, v)

for k in student.keys():
    print(k)

for v in student.values():
    print(v)

#range
for id in range(0,5):
    print(id)

