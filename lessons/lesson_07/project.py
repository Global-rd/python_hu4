
def register_user(users, name, age):
    """
    Regsiters a user to the users list
    """
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered {user}")

def update_user_name(users, current_name, new_name):
    """
    Updates user name based on the given new_name parameter
    """
    for user in users:
        if user["name"] == current_name:
            user["name"] = new_name
            print(f"User {current_name} has been overwritten to {new_name}")
            return
    print(f"No user named {current_name} found in the list of users!")


def display_user_info(users, name):
    """Display all information of a specific user"""
    
    for user in users:
        if user["name"] == name:
            print(f"User info: {user['name']} {user['age']}")
            return
    print(f"No user named {name} found in the list")

def display_all_users(users):
    """
    Displays all information for all users

    """
    print("Registered users:")
    for id, user in enumerate(users, 1):
        print(f"{id} - Name: {user['name']}")


def main():

    users = []
    register_user(users=users, name="Alice", age=15)
    register_user(users=users, name="Bob", age=12)
    register_user(users=users, name="Tim", age=11)
    register_user(users=users, name="Jim", age=13)

    print(users)

main()
    