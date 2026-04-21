songs = ["Warrior", "I'm a barbie girl", "Heavy is the crown", "I got options"]

id = 1
for song in songs:
    print(id, song)
    id += 1

for id, song in enumerate(songs, 1):
    print(id, song)