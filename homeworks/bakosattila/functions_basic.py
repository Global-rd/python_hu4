name_1 = "Alice"
name_2 = "Bob"
name_3 = "Charlie"


def greet_user(name):
    print(f"Hello, {name}, welcome home!")

greet_user(name_1)
greet_user(name_2)
greet_user(name_3)

print("-------------")
names = ["Alice", "Bob", "Charlie"]

for name in names:
    greet_user(name)
