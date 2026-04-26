def register_user(users, name, user) -> list:
    """
    Register users to users list.
    
    """
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered successfully {user}.")


def update_user_name(users, current_name, new_name):
    """
    Update user name based on given new_name parameter.
    """
    for user in users:
        if user["name"] == current_name:
            user["name"] = new_name
            print(f"User {current_name} name updated successfully to {new_name}.")
            return
    print(f"No user name {current_name} found.")

def display_user_info(users, name):
    for user in users:
        if user["name"] == name:
            print(f"User found: {user['username']} {user['age']}")
            return
    print(f"No user name {name} found.")


def display_all_users(users):
    print("All registered users:")
    for id, user in enumerate(users, 1):
        print(f"{id}. Name: {user['name']} - Age: {user['age']}")

def main():

    users = []
    register_user(users=users, name="Alice", age=10)
    register_user(users=users, name="Laci", age=30)
    register_user(users=users, name="Tibi", age=32)
    register_user(users=users, name="Smith", age=60)

    print(users)

main()